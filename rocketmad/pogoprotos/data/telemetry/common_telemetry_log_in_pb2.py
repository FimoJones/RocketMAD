# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/common_telemetry_log_in.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/common_telemetry_log_in.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7pogoprotos/data/telemetry/common_telemetry_log_in.proto\x12\x19pogoprotos.data.telemetry\",\n\x14\x43ommonTelemetryLogIn\x12\x14\n\x0ctimestamp_ms\x18\x01 \x01(\x03\x62\x06proto3')
)




_COMMONTELEMETRYLOGIN = _descriptor.Descriptor(
  name='CommonTelemetryLogIn',
  full_name='pogoprotos.data.telemetry.CommonTelemetryLogIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.data.telemetry.CommonTelemetryLogIn.timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=86,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['CommonTelemetryLogIn'] = _COMMONTELEMETRYLOGIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommonTelemetryLogIn = _reflection.GeneratedProtocolMessageType('CommonTelemetryLogIn', (_message.Message,), dict(
  DESCRIPTOR = _COMMONTELEMETRYLOGIN,
  __module__ = 'pogoprotos.data.telemetry.common_telemetry_log_in_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.CommonTelemetryLogIn)
  ))
_sym_db.RegisterMessage(CommonTelemetryLogIn)


# @@protoc_insertion_point(module_scope)
