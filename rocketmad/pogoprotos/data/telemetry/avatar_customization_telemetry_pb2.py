# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/avatar_customization_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/avatar_customization_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>pogoprotos/data/telemetry/avatar_customization_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"\xe0\x01\n\x1c\x41vatarCustomizationTelemetry\x12X\n\x1d\x61vatar_customization_click_id\x18\x01 \x01(\x0e\x32\x31.pogoprotos.enums.AvatarCustomizationTelemetryIds\x12\x12\n\nasset_name\x18\x02 \x01(\t\x12\x0b\n\x03sku\x18\x03 \x01(\t\x12\x18\n\x10has_enough_coins\x18\x04 \x01(\x08\x12\x12\n\ngroup_name\x18\x05 \x01(\t\x12\x17\n\x0f\x63olor_choice_id\x18\x06 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_AVATARCUSTOMIZATIONTELEMETRY = _descriptor.Descriptor(
  name='AvatarCustomizationTelemetry',
  full_name='pogoprotos.data.telemetry.AvatarCustomizationTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatar_customization_click_id', full_name='pogoprotos.data.telemetry.AvatarCustomizationTelemetry.avatar_customization_click_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_name', full_name='pogoprotos.data.telemetry.AvatarCustomizationTelemetry.asset_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sku', full_name='pogoprotos.data.telemetry.AvatarCustomizationTelemetry.sku', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_enough_coins', full_name='pogoprotos.data.telemetry.AvatarCustomizationTelemetry.has_enough_coins', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='pogoprotos.data.telemetry.AvatarCustomizationTelemetry.group_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_choice_id', full_name='pogoprotos.data.telemetry.AvatarCustomizationTelemetry.color_choice_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=132,
  serialized_end=356,
)

_AVATARCUSTOMIZATIONTELEMETRY.fields_by_name['avatar_customization_click_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._AVATARCUSTOMIZATIONTELEMETRYIDS
DESCRIPTOR.message_types_by_name['AvatarCustomizationTelemetry'] = _AVATARCUSTOMIZATIONTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvatarCustomizationTelemetry = _reflection.GeneratedProtocolMessageType('AvatarCustomizationTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _AVATARCUSTOMIZATIONTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.avatar_customization_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.AvatarCustomizationTelemetry)
  ))
_sym_db.RegisterMessage(AvatarCustomizationTelemetry)


# @@protoc_insertion_point(module_scope)
