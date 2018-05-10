from kafka import KafkaConsumer
import json

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('telemetry',
                         group_id='my-group',
                         bootstrap_servers=['10.30.111.176:9092'])
# for message in consumer:
#     # message value and key are raw bytes -- decode if necessary!
#     # e.g., for unicode: `message.value.decode('utf-8')`
#     # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#     #                                       message.offset, message.key,
#     #                                       message.value))
#     msg = json.loads(message.value)
#     # print msg
#     if msg['encoding_path'] == 'openconfig-interfaces:interfaces/interface/state':
#         for interface in msg['data_json']:    # for name, age in list.items():  (for Python 3.x)
#             if interface['keys']['name'] in ['HundredGigE0/0/1/1', 'HundredGigE0/0/1/2']:
#                 print 'Int: {0}, Oper Status {1}'.format(interface['keys']['name'], interface['content']['oper-status'])
#                 # print name
#     # print msg['node_id_str'] + msg['encoding_path']

# # consume earliest available messages, don't commit offsets
# KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)
#
# # consume json messages
# KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))
#
# # consume msgpack
# KafkaConsumer(value_deserializer=msgpack.unpackb)
#
# # StopIteration if no message after 1sec
# KafkaConsumer(consumer_timeout_ms=1000)
#
# # Subscribe to a regex topic pattern
# consumer = KafkaConsumer()

