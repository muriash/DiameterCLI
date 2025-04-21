import sctp
import socket
import threading
from pyDiameter.pyDiaMessage import *

from diaMessages import buildCEA, buildDWA, buildCMR, buildDPR, buildCMR_Release

class DiameterSCTPServer:
    def __init__(self, host='192.168.10.22', port=3680):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_conn = None
        self.running = False
        self.flag = False

    def start(self):
        sk = sctp.sctpsocket_tcp(socket.AF_INET)
        self.server_socket = sctp.sctpsocket(socket.AF_INET, socket.SOCK_SEQPACKET, sk)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = True
        print(f"[INFO] SCTP сервер слушает {self.host}:{self.port}")

        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        try:
            while self.running:
                conn, addr = self.server_socket.accept()
                self.client_conn = conn
                threading.Thread(target=self.handle_client, args=(conn,), daemon=True).start()
        except Exception as e:
            print(f"[ERROR] in accept_connections: {e}")

    def handle_client(self, conn):
        try:
            while True:
                data = conn.recv(4096)

                msg = DiaMessage()
                msg.decode(data)
                hbh_id = msg.getHBHID()
                e2e_id = msg.getE2EID()

                if msg.getCommandCode() == 280:  # Device-Watchdog Request
                    response = buildDWA(hbh_id, e2e_id).encode()
                    conn.sctp_send(response)

                elif msg.getCommandCode() == 257:  # CER
                    response = buildCEA(hbh_id, e2e_id).encode()
                    conn.sctp_send(response)
                
                elif msg.getCommandCode() == 8388732:
                    print(f"[RX] Получено:")
                    print(f"\tCommand Code: {msg.getCommandCode()}")
                    print(f"\t{msg.getAVPs()[1].getAVPName()}: {msg.getAVPs()[1].getAVPValue()}")
                    self.flag = True
                
                elif msg.getCommandCode() == 8388733:
                    print(f"[RX] Получено:")
                    print(f"\tCommand Code: {msg.getCommandCode()}")
                    print(f"\t{msg.getAVPs()[1].getAVPName()}: {msg.getAVPs()[1].getAVPValue()}")
                    self.flag = True

        except Exception as e:
            print(f"[ERROR] in handle_client: {e}")
        finally:
            conn.close()
            print("[INFO] Соединение с клиентом закрыто.")

    def send_dpr_and_close(self):
        if self.client_conn:
            try:
                msg = buildCMR_Release().encode()
                self.client_conn.sctp_send(msg)
                data = self.client_conn.recv(4096)
                
                msg = buildDPR().encode()
                self.client_conn.sctp_send(msg)
                data = self.client_conn.recv(4096)
            except Exception as e:
                print(f"[ERROR] in send_dpr_and_close: {e}")
            finally:
                self.client_conn.close()
        if self.server_socket:
            self.server_socket.close()
            print("[INFO] Сокеты закрыты, выход.")

if __name__ == '__main__':
    server = DiameterSCTPServer()
    server.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[INFO] Завершение по Ctrl+C")
        server.send_dpr_and_close()
