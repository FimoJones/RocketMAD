# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/gym/gym_battle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/gym/gym_battle.proto',
  package='pogoprotos.data.gym',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$pogoprotos/data/gym/gym_battle.proto\x12\x13pogoprotos.data.gym\"\\\n\tGymBattle\x12\x11\n\tbattle_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ompleted_ms\x18\x02 \x01(\x03\x12&\n\x1eincremented_gym_battle_friends\x18\x03 \x01(\x08\x62\x06proto3')
)




_GYMBATTLE = _descriptor.Descriptor(
  name='GymBattle',
  full_name='pogoprotos.data.gym.GymBattle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='battle_id', full_name='pogoprotos.data.gym.GymBattle.battle_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completed_ms', full_name='pogoprotos.data.gym.GymBattle.completed_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incremented_gym_battle_friends', full_name='pogoprotos.data.gym.GymBattle.incremented_gym_battle_friends', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=61,
  serialized_end=153,
)

DESCRIPTOR.message_types_by_name['GymBattle'] = _GYMBATTLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymBattle = _reflection.GeneratedProtocolMessageType('GymBattle', (_message.Message,), dict(
  DESCRIPTOR = _GYMBATTLE,
  __module__ = 'pogoprotos.data.gym.gym_battle_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.gym.GymBattle)
  ))
_sym_db.RegisterMessage(GymBattle)


# @@protoc_insertion_point(module_scope)
