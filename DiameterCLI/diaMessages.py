import pyDiameter
from pyDiameter.pyDiaAVPTools import address_to_bytes, bytes_to_address, time_to_bytes, bytes_to_time
from pyDiameter.pyDiaAVPPath import DiaAVPPath
from pyDiameter.pyDiaAVPBasicTypes import DiaAVPStr

#from diaDecoder import visitAVP, visitMessage

from pyDiameter.pyDiaMessage import DiaMessage
from pyDiameter.pyDiaAVPBasicTypes import DiaAVPStr, DiaAVPUInt32, DiaAVPUInt64
from pyDiameter.pyDiaAVPTypes import DiaAVPGroup
from pyDiameter.pyDiaAVPPath import DiaAVPPath

# создаём CEA сообщение
def buildCEA(hbh_id,e2e_id):
    msg = DiaMessage()
    msg.setCommandCode(257)  # Capabilities-Exchange-Request
    msg.setApplicationID(0)  # Diameter Common Messages
    msg.setHBHID(hbh_id)  # любой уникальный ID
    msg.setE2EID(e2e_id)  # любой уникальный ID

    # Result-Code = 268 (DIAMETER_SUCCESS)
    result_code_avp = DiaAVPUInt32()
    result_code_avp.setAVPCode(268)
    result_code_avp.setAVPMandatoryFlag()
    result_code_avp.setAVPValue(2001)  # DIAMETER_SUCCESS
    
    # Origin-Host
    origin_host_avp = DiaAVPStr()
    origin_host_avp.setAVPCode(264)
    origin_host_avp.setAVPMandatoryFlag()
    origin_host_avp.setAVPValue(b'mme3.nbiot.epc.mnc054.mcc999.3gppnetwork.org')

    # Origin-Realm
    origin_realm_avp = DiaAVPStr()
    origin_realm_avp.setAVPCode(296)
    origin_realm_avp.setAVPMandatoryFlag()
    origin_realm_avp.setAVPValue(b'epc.mnc054.mcc999.3gppnetwork.org')

    # Vendor-Id
    vendor_id_avp = DiaAVPUInt32()
    vendor_id_avp.setAVPCode(266)
    vendor_id_avp.setAVPMandatoryFlag()
    vendor_id_avp.setAVPValue(10415)

    # Product-Name
    product_name_avp = DiaAVPStr()
    product_name_avp.setAVPCode(269)
    product_name_avp.setAVPValue(b'MME')

    # Auth-Application-Id (4)
    auth_app_id_4 = DiaAVPUInt32()
    auth_app_id_4.setAVPCode(258)
    auth_app_id_4.setAVPMandatoryFlag()
    auth_app_id_4.setAVPValue(4)

    # Auth-Application-Id (16777251)
    auth_app_id_3gpp_s6a = DiaAVPUInt32()
    auth_app_id_3gpp_s6a.setAVPCode(258)
    auth_app_id_3gpp_s6a.setAVPMandatoryFlag()
    auth_app_id_3gpp_s6a.setAVPValue(16777251)

    # Auth-Application-Id (16777346)
    auth_app_id_3gpp_t6a = DiaAVPUInt32()
    auth_app_id_3gpp_t6a.setAVPCode(258)
    auth_app_id_3gpp_t6a.setAVPMandatoryFlag()
    auth_app_id_3gpp_t6a.setAVPValue(16777346)

    # Auth-Application-Id (Relay 4294967295)
    auth_app_id_relay = DiaAVPUInt32()
    auth_app_id_relay.setAVPCode(258)
    auth_app_id_relay.setAVPMandatoryFlag()
    auth_app_id_relay.setAVPValue(4294967295)

    # Inband-Security-Id = 0 (NO_INBAND_SECURITY)
    inband_security_avp = DiaAVPUInt32()
    inband_security_avp.setAVPCode(299)
    inband_security_avp.setAVPMandatoryFlag()
    inband_security_avp.setAVPValue(0)

 # Vendor-Specific-Application-Id (Grouped)
    vendor_app_id_avp = DiaAVPGroup()
    vendor_app_id_avp.setAVPCode(260)
    vendor_app_id_avp.setAVPMandatoryFlag()

    # Vendor-Id = 10415
    vendor_id_avp = DiaAVPUInt32()
    vendor_id_avp.setAVPCode(266)
    vendor_id_avp.setAVPMandatoryFlag()
    vendor_id_avp.setAVPValue(10415)

    # Auth-Application-Id = 16777251 (3GPP S6a/S6d)
    auth_app_id_avp = DiaAVPUInt32()
    auth_app_id_avp.setAVPCode(258)
    auth_app_id_avp.setAVPMandatoryFlag()
    auth_app_id_avp.setAVPValue(16777251)

    # Сборка группы Vendor-Specific-Application-Id
    vendor_app_id_avp.addAVP(vendor_id_avp)
    vendor_app_id_avp.addAVP(auth_app_id_avp)
    
    # добавляем AVP в сообщение
    path = DiaAVPPath()
    path.setPath('')

    msg.addAVPByPath(path, result_code_avp)
    msg.addAVPByPath(path, origin_host_avp)
    msg.addAVPByPath(path, origin_realm_avp)
    msg.addAVPByPath(path, vendor_id_avp)
    msg.addAVPByPath(path, product_name_avp)
    msg.addAVPByPath(path, auth_app_id_4)
    msg.addAVPByPath(path, auth_app_id_3gpp_s6a)
    msg.addAVPByPath(path, auth_app_id_3gpp_t6a)
    msg.addAVPByPath(path, auth_app_id_relay)
    msg.addAVPByPath(path, inband_security_avp)
    msg.addAVPByPath(path, vendor_app_id_avp)
    
    #visitMessage(msg)
    return(msg)

# создаём DWA сообщение
def buildDWA(hbh_id,e2e_id):
    msg = DiaMessage()
    msg.setCommandCode(280)  # Device-Watchdog Answer
    msg.setApplicationID(0)  # Diameter Common Messages
    msg.setHBHID(hbh_id)  # любой уникальный ID
    msg.setE2EID(e2e_id)  # любой уникальный ID

    # Result-Code = 268 (DIAMETER_SUCCESS)
    result_code_avp = DiaAVPUInt32()
    result_code_avp.setAVPCode(268)
    result_code_avp.setAVPMandatoryFlag()
    result_code_avp.setAVPValue(2001)  # DIAMETER_SUCCESS

    # Origin-Host
    origin_host_avp = DiaAVPStr()
    origin_host_avp.setAVPCode(264)
    origin_host_avp.setAVPMandatoryFlag()
    origin_host_avp.setAVPValue(b'mme3.nbiot.epc.mnc054.mcc999.3gppnetwork.org')

    # Origin-Realm
    origin_realm_avp = DiaAVPStr()
    origin_realm_avp.setAVPCode(296)
    origin_realm_avp.setAVPMandatoryFlag()
    origin_realm_avp.setAVPValue(b'epc.mnc054.mcc999.3gppnetwork.org')

    # Origin-State-Id
    origin_state_avp = DiaAVPUInt32()
    origin_state_avp.setAVPCode(278)
    origin_state_avp.setAVPMandatoryFlag()
    origin_state_avp.setAVPValue(0)

     # добавляем AVP в сообщение
    path = DiaAVPPath()
    path.setPath('')

    msg.addAVPByPath(path, result_code_avp)
    msg.addAVPByPath(path, origin_host_avp)
    msg.addAVPByPath(path, origin_realm_avp)
    msg.addAVPByPath(path, origin_state_avp)

    return(msg)

def buildCMR():
    msg = DiaMessage()
    msg.setCommandCode(8388732)  # Command-Code для CMR
    msg.setApplicationID(16777346)  # 3GPP SCEF Application ID
    msg.setRequestFlag()  # запрос
    msg.setProxyableFlag()  # проксируемый
    msg.setHBHID(4321)
    msg.setE2EID(8765)

    path = DiaAVPPath()
    path.setPath('')

    # Session-Id
    session_id = DiaAVPStr()
    session_id.setAVPCode(263)
    session_id.setAVPMandatoryFlag()
    session_id.setAVPValue(b'mme3.nbiot.epc.mnc054.mcc999.3gppnetwork.org;1733305109;17')

    # User-Identifier
    user_identifier = DiaAVPGroup()
    user_identifier.setAVPCode(3102)
    user_identifier.setAVPFlags(0xC0)  # V + M
    user_identifier.setAVPVendor(10415)

    user_name = DiaAVPStr()
    user_name.setAVPCode(1)
    user_name.setAVPMandatoryFlag()
    user_name.setAVPValue(b'999540000000598')

    user_identifier.addAVP(user_name)

    # Bearer-Identifier
    bearer_id = DiaAVPStr()
    bearer_id.setAVPCode(1020)
    bearer_id.setAVPFlags(0xC0)  # V + M
    bearer_id.setAVPVendor(10415)
    bearer_id.setAVPValue(b'\x05')

    # Auth-Session-State
    auth_state = DiaAVPUInt32()
    auth_state.setAVPCode(277)
    auth_state.setAVPMandatoryFlag()
    auth_state.setAVPValue(1)  # NO_STATE_MAINTAINED

    # Origin-Host
    origin_host_avp = DiaAVPStr()
    origin_host_avp.setAVPCode(264)
    origin_host_avp.setAVPMandatoryFlag()
    origin_host_avp.setAVPValue(b'mme3.nbiot.epc.mnc054.mcc999.3gppnetwork.org')

    # Origin-Realm
    origin_realm_avp = DiaAVPStr()
    origin_realm_avp.setAVPCode(296)
    origin_realm_avp.setAVPMandatoryFlag()
    origin_realm_avp.setAVPValue(b'epc.mnc054.mcc999.3gppnetwork.org')

    # Destination-Host
    destination_host_avp = DiaAVPStr()
    destination_host_avp.setAVPCode(293)
    destination_host_avp.setAVPMandatoryFlag()
    destination_host_avp.setAVPValue(b'scef.protei.ru')

    # Destination-Realm
    destination_realm_avp = DiaAVPStr()
    destination_realm_avp.setAVPCode(283)
    destination_realm_avp.setAVPMandatoryFlag()
    destination_realm_avp.setAVPValue(b'protei.ru')

    # Connection-Action
    conn_action = DiaAVPUInt32()
    conn_action.setAVPCode(4314)
    conn_action.setAVPFlags(0xC0)
    conn_action.setAVPVendor(10415)
    conn_action.setAVPValue(0)  # CONNECTION_ESTABLISHMENT

    # Service-Selection
    service_selection = DiaAVPStr()
    service_selection.setAVPCode(493)
    service_selection.setAVPMandatoryFlag()
    service_selection.setAVPValue(b'scef.protei.ru.mnc054.mcc999.gprs')

    # RAT-Type
    rat_type = DiaAVPUInt32()
    rat_type.setAVPCode(1032)
    rat_type.setAVPFlags(0xC0)
    rat_type.setAVPVendor(10415)
    rat_type.setAVPValue(1005)  # EUTRAN-NB-IoT

    # Terminal-Information
    terminal_info = DiaAVPGroup()
    terminal_info.setAVPCode(1401)
    terminal_info.setAVPFlags(0xC0)
    terminal_info.setAVPVendor(10415)

    imei = DiaAVPStr()
    imei.setAVPCode(1402)
    imei.setAVPFlags(0xC0)
    imei.setAVPVendor(10415)
    imei.setAVPValue(b'86157706844346')

    sw_version = DiaAVPStr()
    sw_version.setAVPCode(1403)
    sw_version.setAVPFlags(0xC0)
    sw_version.setAVPVendor(10415)
    sw_version.setAVPValue(b'90')

    terminal_info.addAVP(imei)
    terminal_info.addAVP(sw_version)

    # Visited-PLMN-Id
    plmn_id = DiaAVPStr()
    plmn_id.setAVPCode(1407)
    plmn_id.setAVPFlags(0xC0)
    plmn_id.setAVPVendor(10415)
    plmn_id.setAVPValue(b'\x99\xf9\x45')

    # Добавляем все в сообщение
    msg.addAVPByPath(path, session_id)
    msg.addAVPByPath(path, user_identifier)
    msg.addAVPByPath(path, bearer_id)
    msg.addAVPByPath(path, auth_state)
    msg.addAVPByPath(path, origin_host_avp)
    msg.addAVPByPath(path, origin_realm_avp)
    msg.addAVPByPath(path, destination_host_avp)
    msg.addAVPByPath(path, destination_realm_avp)
    msg.addAVPByPath(path, conn_action)
    msg.addAVPByPath(path, service_selection)
    msg.addAVPByPath(path, rat_type)
    msg.addAVPByPath(path, terminal_info)
    msg.addAVPByPath(path, plmn_id)

    return(msg)

def buildMO():
    msg = DiaMessage()
    msg.setCommandCode(8388733)  # Command-Code для CMR
    msg.setApplicationID(16777346)  # 3GPP SCEF Application ID
    msg.setRequestFlag()  # запрос
    msg.setProxyableFlag()  # проксируемый
    msg.setHBHID(4322)
    msg.setE2EID(8766)

    path = DiaAVPPath()
    path.setPath('')

    # Session-Id
    session_id = DiaAVPStr()
    session_id.setAVPCode(263)
    session_id.setAVPMandatoryFlag()
    session_id.setAVPValue(b'mme3.nbiot.epc.mnc054.mcc999.3gppnetwork.org;1733305109;17')

    # User-Identifier
    user_identifier = DiaAVPGroup()
    user_identifier.setAVPCode(3102)
    user_identifier.setAVPFlags(0xC0)  # V + M
    user_identifier.setAVPVendor(10415)

    user_name = DiaAVPStr()
    user_name.setAVPCode(1)
    user_name.setAVPMandatoryFlag()
    user_name.setAVPValue(b'999540000000598')

    user_identifier.addAVP(user_name)

    # Bearer-Identifier
    bearer_id = DiaAVPStr()
    bearer_id.setAVPCode(1020)
    bearer_id.setAVPFlags(0xC0)  # V + M
    bearer_id.setAVPVendor(10415)
    bearer_id.setAVPValue(b'\x05')

    # Auth-Session-State
    auth_state = DiaAVPUInt32()
    auth_state.setAVPCode(277)
    auth_state.setAVPMandatoryFlag()
    auth_state.setAVPValue(1)  # NO_STATE_MAINTAINED

    # Origin-Host
    origin_host_avp = DiaAVPStr()
    origin_host_avp.setAVPCode(264)
    origin_host_avp.setAVPMandatoryFlag()
    origin_host_avp.setAVPValue(b'mme3.nbiot.epc.mnc054.mcc999.3gppnetwork.org')

    # Origin-Realm
    origin_realm_avp = DiaAVPStr()
    origin_realm_avp.setAVPCode(296)
    origin_realm_avp.setAVPMandatoryFlag()
    origin_realm_avp.setAVPValue(b'epc.mnc054.mcc999.3gppnetwork.org')

    # Destination-Host
    destination_host_avp = DiaAVPStr()
    destination_host_avp.setAVPCode(293)
    destination_host_avp.setAVPMandatoryFlag()
    destination_host_avp.setAVPValue(b'scef.protei.ru')

    # Destination-Realm
    destination_realm_avp = DiaAVPStr()
    destination_realm_avp.setAVPCode(283)
    destination_realm_avp.setAVPMandatoryFlag()
    destination_realm_avp.setAVPValue(b'protei.ru')

    # Non-IP Data
    non_ip_data_avp = DiaAVPStr()
    non_ip_data_avp.setAVPCode(4315)
    non_ip_data_avp.setAVPFlags(0xC0)  # V + M
    non_ip_data_avp.setAVPVendor(10415)
    non_ip_data_avp.setAVPValue(b'Hello from DiameterServer!')

    # Добавляем все в сообщение
    msg.addAVPByPath(path, session_id)
    msg.addAVPByPath(path, user_identifier)
    msg.addAVPByPath(path, bearer_id)
    msg.addAVPByPath(path, auth_state)
    msg.addAVPByPath(path, origin_host_avp)
    msg.addAVPByPath(path, origin_realm_avp)
    msg.addAVPByPath(path, destination_host_avp)
    msg.addAVPByPath(path, destination_realm_avp)
    msg.addAVPByPath(path, non_ip_data_avp)

    return(msg)

def buildCMR_Release():
    msg = DiaMessage()
    msg.setCommandCode(8388732)  # Command-Code для CMR
    msg.setApplicationID(16777346)  # 3GPP SCEF Application ID
    msg.setRequestFlag()  # запрос
    msg.setProxyableFlag()  # проксируемый
    msg.setHBHID(4322)
    msg.setE2EID(8766)

    path = DiaAVPPath()
    path.setPath('')

    # Session-Id
    session_id = DiaAVPStr()
    session_id.setAVPCode(263)
    session_id.setAVPMandatoryFlag()
    session_id.setAVPValue(b'mme3.nbiot.epc.mnc054.mcc999.3gppnetwork.org;1733305109;17')

    # User-Identifier
    user_identifier = DiaAVPGroup()
    user_identifier.setAVPCode(3102)
    user_identifier.setAVPFlags(0xC0)  # V + M
    user_identifier.setAVPVendor(10415)

    user_name = DiaAVPStr()
    user_name.setAVPCode(1)
    user_name.setAVPMandatoryFlag()
    user_name.setAVPValue(b'999540000000598')

    user_identifier.addAVP(user_name)

    # Bearer-Identifier
    bearer_id = DiaAVPStr()
    bearer_id.setAVPCode(1020)
    bearer_id.setAVPFlags(0xC0)  # V + M
    bearer_id.setAVPVendor(10415)
    bearer_id.setAVPValue(b'\x05')

    # Auth-Session-State
    auth_state = DiaAVPUInt32()
    auth_state.setAVPCode(277)
    auth_state.setAVPMandatoryFlag()
    auth_state.setAVPValue(1)  # NO_STATE_MAINTAINED

    # Origin-Host
    origin_host_avp = DiaAVPStr()
    origin_host_avp.setAVPCode(264)
    origin_host_avp.setAVPMandatoryFlag()
    origin_host_avp.setAVPValue(b'mme3.nbiot.epc.mnc054.mcc999.3gppnetwork.org')

    # Origin-Realm
    origin_realm_avp = DiaAVPStr()
    origin_realm_avp.setAVPCode(296)
    origin_realm_avp.setAVPMandatoryFlag()
    origin_realm_avp.setAVPValue(b'epc.mnc054.mcc999.3gppnetwork.org')

    # Destination-Host
    destination_host_avp = DiaAVPStr()
    destination_host_avp.setAVPCode(293)
    destination_host_avp.setAVPMandatoryFlag()
    destination_host_avp.setAVPValue(b'scef.protei.ru')

    # Destination-Realm
    destination_realm_avp = DiaAVPStr()
    destination_realm_avp.setAVPCode(283)
    destination_realm_avp.setAVPMandatoryFlag()
    destination_realm_avp.setAVPValue(b'protei.ru')

    # Connection-Action
    conn_action = DiaAVPUInt32()
    conn_action.setAVPCode(4314)
    conn_action.setAVPFlags(0xC0)
    conn_action.setAVPVendor(10415)
    conn_action.setAVPValue(1)  # CONNECTION_RELEASE

    # Добавляем все в сообщение
    msg.addAVPByPath(path, session_id)
    msg.addAVPByPath(path, user_identifier)
    msg.addAVPByPath(path, bearer_id)
    msg.addAVPByPath(path, auth_state)
    msg.addAVPByPath(path, origin_host_avp)
    msg.addAVPByPath(path, origin_realm_avp)
    msg.addAVPByPath(path, destination_host_avp)
    msg.addAVPByPath(path, destination_realm_avp)
    msg.addAVPByPath(path, conn_action)
    return(msg)

def buildDPR():
    msg = DiaMessage()
    msg.setCommandCode(282)  # Disconnect-Peer-Request
    msg.setApplicationID(0)  # Diameter Common Messages
    msg.setRequestFlag()  # запрос
    msg.setProxyableFlag()  # проксируемый
    msg.setHBHID(4321)       # уникальный HBH ID
    msg.setE2EID(8765)       # уникальный E2E ID

    # Origin-Host
    origin_host = DiaAVPStr()
    origin_host.setAVPCode(264)
    origin_host.setAVPMandatoryFlag()
    origin_host.setAVPValue(b'mme3.nbiot.epc.mnc054.mcc999.3gppnetwork.org')

    # Origin-Realm
    origin_realm = DiaAVPStr()
    origin_realm.setAVPCode(296)
    origin_realm.setAVPMandatoryFlag()
    origin_realm.setAVPValue(b'epc.mnc054.mcc999.3gppnetwork.org')

    # Disconnect-Cause: REBOOTING (0), BUSY (1), DO_NOT_WANT_TO_TALK_TO_YOU (2)
    disconnect_cause = DiaAVPUInt32()
    disconnect_cause.setAVPCode(273)  # Disconnect-Cause
    disconnect_cause.setAVPMandatoryFlag()
    disconnect_cause.setAVPValue(0)   # 0 = REBOOTING

    path = DiaAVPPath()
    path.setPath('')

    msg.addAVPByPath(path, origin_host)
    msg.addAVPByPath(path, origin_realm)
    msg.addAVPByPath(path, disconnect_cause)

    return(msg)


def sendDiaMsg(msg, socket):
    data = msg.encode()
    socket.sctp_send(data)
    return()
