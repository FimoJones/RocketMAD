# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/analytics/client_telemetry_record.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.analytics import client_telemetry_common_filter_pb2 as pogoprotos_dot_data_dot_analytics_dot_client__telemetry__common__filter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/analytics/client_telemetry_record.proto',
  package='pogoprotos.data.analytics',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7pogoprotos/data/analytics/client_telemetry_record.proto\x12\x19pogoprotos.data.analytics\x1a>pogoprotos/data/analytics/client_telemetry_common_filter.proto\"\xc3\x01\n\x15\x43lientTelemetryRecord\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x17\n\x0f\x65ncoded_message\x18\x02 \x01(\x0c\x12\x1b\n\x13\x63lient_timestamp_ms\x18\x03 \x01(\x03\x12\x11\n\tmetric_id\x18\x04 \x01(\x03\x12N\n\x0e\x63ommon_filters\x18\x05 \x01(\x0b\x32\x36.pogoprotos.data.analytics.ClientTelemetryCommonFilterb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_analytics_dot_client__telemetry__common__filter__pb2.DESCRIPTOR,])




_CLIENTTELEMETRYRECORD = _descriptor.Descriptor(
  name='ClientTelemetryRecord',
  full_name='pogoprotos.data.analytics.ClientTelemetryRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_id', full_name='pogoprotos.data.analytics.ClientTelemetryRecord.record_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_message', full_name='pogoprotos.data.analytics.ClientTelemetryRecord.encoded_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_timestamp_ms', full_name='pogoprotos.data.analytics.ClientTelemetryRecord.client_timestamp_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_id', full_name='pogoprotos.data.analytics.ClientTelemetryRecord.metric_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='common_filters', full_name='pogoprotos.data.analytics.ClientTelemetryRecord.common_filters', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=346,
)

_CLIENTTELEMETRYRECORD.fields_by_name['common_filters'].message_type = pogoprotos_dot_data_dot_analytics_dot_client__telemetry__common__filter__pb2._CLIENTTELEMETRYCOMMONFILTER
DESCRIPTOR.message_types_by_name['ClientTelemetryRecord'] = _CLIENTTELEMETRYRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryRecord = _reflection.GeneratedProtocolMessageType('ClientTelemetryRecord', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYRECORD,
  __module__ = 'pogoprotos.data.analytics.client_telemetry_record_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.analytics.ClientTelemetryRecord)
  ))
_sym_db.RegisterMessage(ClientTelemetryRecord)


# @@protoc_insertion_point(module_scope)
