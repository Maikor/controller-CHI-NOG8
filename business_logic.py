from telemetry_consumer import consumer
import json
import requests

server_ip = '10.30.111.176'
server_port = '5005'
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                       message.offset, message.key,
    #                                       message.value))
    msg = json.loads(message.value)
    # print msg
    if msg['encoding_path'] == 'openconfig-interfaces:interfaces/interface/state':
        for interface in msg['data_json']:    # for name, age in list.items():  (for Python 3.x)
            if interface['keys']['name'] in ['HundredGigE0/0/1/1', 'HundredGigE0/0/1/2']:

                #  ['oper-status']
                print 'Int: {0}, Oper Status {1}, Counters: {2}'.format(interface['keys']['name'],
                                                                        interface['content']['oper-status'],
                                                                        interface['content']['counters'])
                if interface['keys']['name'] == 'HundredGigE0/0/1/1' and interface['content']['oper-status'] != 'UP':
                    requests.get('http://{0}:{1}/add_second'.format(server_ip, server_port))

                if interface['keys']['name'] == 'HundredGigE0/0/1/2' and interface['content']['oper-status'] != 'UP':
                    requests.get('http://{0}:{1}/add_first'.format(server_ip, server_port))

    # print msg['node_id_str'] + msg['encoding_path']
    # print msg['node_id_str'] + msg['encoding_path']
