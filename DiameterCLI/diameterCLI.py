import time
from pyDiameter.pyDiaMessage import *
from diaMessages import buildCMR, buildDPR, buildMO

def print_header():
    print("\n" + "=" * 40)
    print("||            DiameterCLI            ||")
    print("=" * 40)

def print_menu():
    print("\nВыберите действие:")
    print("1. Отправить Connection-Management Request")
    print("2. Отправить Non-IP Data")
    print("3. Разорвать соединение и выйти")

def interactive_cli(server):
    if server.client_conn is None:
        print("[INFO] Ожидание подключения Diameter-клиента...")
        while server.client_conn is None:
            time.sleep(1)

    print("[INFO] Подключение установлено.")

    try:
        print_header()
        while True:
            print_menu()

            choice = input("Ваш выбор: ").strip()

            if choice == "1":
                msg = buildCMR().encode()
                server.client_conn.sctp_send(msg)
                print("\n[TX] Отправлено: Connection-Management Request")
                while server.flag == False:
                    pass
                server.flag = True
                time.sleep(3)

            elif choice == "2":
                msg = buildMO().encode()
                server.client_conn.sctp_send(msg)
                print("\n[TX] Отправлено: MO-Data Request")
                while server.flag == False:
                    pass
                server.flag = True
                time.sleep(3)

            elif choice == "3":
                msg = buildDPR().encode()
                server.client_conn.sctp_send(msg)
                print("\n[TX] Отправлено: Disconnect Peer Request")
                data = server.client_conn.recv(4096)
                print(f"[RX] Получено: {data.hex()}")
                break

            else:
                print("[WARN] Некорректный ввод! Введите 1, 2 или 3.")

    except KeyboardInterrupt:
        print("\n[INFO] Завершение программы по Ctrl+C.")
    
    except Exception as e:
        print(f"[ERROR]: {e}")

if __name__ == '__main__':
    from diameterServer import DiameterSCTPServer

    server = DiameterSCTPServer()
    server.start()

    interactive_cli(server)

    server.send_dpr_and_close()
