# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/combat_challenge.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import combat_type_pb2 as pogoprotos_dot_enums_dot_combat__type__pb2
from pogoprotos.data.combat import challenge_player_pb2 as pogoprotos_dot_data_dot_combat_dot_challenge__player__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/combat_challenge.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-pogoprotos/data/combat/combat_challenge.proto\x12\x16pogoprotos.data.combat\x1a\"pogoprotos/enums/combat_type.proto\x1a-pogoprotos/data/combat/challenge_player.proto\"\x8c\x04\n\x0f\x43ombatChallenge\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\t\x12*\n\x04type\x18\x02 \x01(\x0e\x32\x1c.pogoprotos.enums.CombatType\x12!\n\x19\x63ombat_league_template_id\x18\x03 \x01(\t\x12;\n\nchallenger\x18\x05 \x01(\x0b\x32\'.pogoprotos.data.combat.ChallengePlayer\x12\x39\n\x08opponent\x18\x06 \x01(\x0b\x32\'.pogoprotos.data.combat.ChallengePlayer\x12K\n\x05state\x18\x07 \x01(\x0e\x32<.pogoprotos.data.combat.CombatChallenge.CombatChallengeState\x12\x1c\n\x14\x63reated_timestamp_ms\x18\x08 \x01(\x03\x12\x1f\n\x17\x65xpiration_timestamp_ms\x18\x13 \x01(\x03\x12\x11\n\tcombat_id\x18\n \x01(\t\"}\n\x14\x43ombatChallengeState\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\n\n\x06OPENED\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x04\x12\x0c\n\x08\x44\x45\x43LINED\x10\x05\x12\t\n\x05READY\x10\x06\x12\x0b\n\x07TIMEOUT\x10\x07\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_combat__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_challenge__player__pb2.DESCRIPTOR,])



_COMBATCHALLENGE_COMBATCHALLENGESTATE = _descriptor.EnumDescriptor(
  name='CombatChallengeState',
  full_name='pogoprotos.data.combat.CombatChallenge.CombatChallengeState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPENED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCEPTED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECLINED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=556,
  serialized_end=681,
)
_sym_db.RegisterEnumDescriptor(_COMBATCHALLENGE_COMBATCHALLENGESTATE)


_COMBATCHALLENGE = _descriptor.Descriptor(
  name='CombatChallenge',
  full_name='pogoprotos.data.combat.CombatChallenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge_id', full_name='pogoprotos.data.combat.CombatChallenge.challenge_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.data.combat.CombatChallenge.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_league_template_id', full_name='pogoprotos.data.combat.CombatChallenge.combat_league_template_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenger', full_name='pogoprotos.data.combat.CombatChallenge.challenger', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opponent', full_name='pogoprotos.data.combat.CombatChallenge.opponent', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='pogoprotos.data.combat.CombatChallenge.state', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_timestamp_ms', full_name='pogoprotos.data.combat.CombatChallenge.created_timestamp_ms', index=6,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration_timestamp_ms', full_name='pogoprotos.data.combat.CombatChallenge.expiration_timestamp_ms', index=7,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_id', full_name='pogoprotos.data.combat.CombatChallenge.combat_id', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMBATCHALLENGE_COMBATCHALLENGESTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=681,
)

_COMBATCHALLENGE.fields_by_name['type'].enum_type = pogoprotos_dot_enums_dot_combat__type__pb2._COMBATTYPE
_COMBATCHALLENGE.fields_by_name['challenger'].message_type = pogoprotos_dot_data_dot_combat_dot_challenge__player__pb2._CHALLENGEPLAYER
_COMBATCHALLENGE.fields_by_name['opponent'].message_type = pogoprotos_dot_data_dot_combat_dot_challenge__player__pb2._CHALLENGEPLAYER
_COMBATCHALLENGE.fields_by_name['state'].enum_type = _COMBATCHALLENGE_COMBATCHALLENGESTATE
_COMBATCHALLENGE_COMBATCHALLENGESTATE.containing_type = _COMBATCHALLENGE
DESCRIPTOR.message_types_by_name['CombatChallenge'] = _COMBATCHALLENGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatChallenge = _reflection.GeneratedProtocolMessageType('CombatChallenge', (_message.Message,), dict(
  DESCRIPTOR = _COMBATCHALLENGE,
  __module__ = 'pogoprotos.data.combat.combat_challenge_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.CombatChallenge)
  ))
_sym_db.RegisterMessage(CombatChallenge)


# @@protoc_insertion_point(module_scope)
