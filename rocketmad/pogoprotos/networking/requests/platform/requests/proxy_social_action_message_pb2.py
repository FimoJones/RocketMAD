# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/platform/requests/proxy_social_action_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/platform/requests/proxy_social_action_message.proto',
  package='pogoprotos.networking.requests.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nRpogoprotos/networking/requests/platform/requests/proxy_social_action_message.proto\x12\x30pogoprotos.networking.requests.platform.requests\"I\n\x18ProxySocialActionMessage\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\r\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x62\x06proto3')
)




_PROXYSOCIALACTIONMESSAGE = _descriptor.Descriptor(
  name='ProxySocialActionMessage',
  full_name='pogoprotos.networking.requests.platform.requests.ProxySocialActionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='pogoprotos.networking.requests.platform.requests.ProxySocialActionMessage.action', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='pogoprotos.networking.requests.platform.requests.ProxySocialActionMessage.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='pogoprotos.networking.requests.platform.requests.ProxySocialActionMessage.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=136,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['ProxySocialActionMessage'] = _PROXYSOCIALACTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProxySocialActionMessage = _reflection.GeneratedProtocolMessageType('ProxySocialActionMessage', (_message.Message,), dict(
  DESCRIPTOR = _PROXYSOCIALACTIONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.platform.requests.proxy_social_action_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.platform.requests.ProxySocialActionMessage)
  ))
_sym_db.RegisterMessage(ProxySocialActionMessage)


# @@protoc_insertion_point(module_scope)
