# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/combat_player_profile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_public_profile_pb2 as pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2
from pogoprotos.data.combat import combat_player_preferences_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__player__preferences__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/combat_player_profile.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2pogoprotos/data/combat/combat_player_profile.proto\x12\x16pogoprotos.data.combat\x1a\x32pogoprotos/data/player/player_public_profile.proto\x1a\x36pogoprotos/data/combat/combat_player_preferences.proto\"\xfa\x02\n\x13\x43ombatPlayerProfile\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x43\n\x0epublic_profile\x18\x02 \x01(\x0b\x32+.pogoprotos.data.player.PlayerPublicProfile\x12!\n\x19\x63ombat_league_template_id\x18\x03 \x03(\t\x12\x18\n\x10\x62uddy_pokemon_id\x18\x04 \x01(\x06\x12\x46\n\x08location\x18\x05 \x01(\x0b\x32\x34.pogoprotos.data.combat.CombatPlayerProfile.Location\x12R\n\x19\x63ombat_player_preferences\x18\x06 \x01(\x0b\x32/.pogoprotos.data.combat.CombatPlayerPreferences\x1a\x32\n\x08Location\x12\x12\n\nlat_degree\x18\x01 \x01(\x01\x12\x12\n\nlng_degree\x18\x02 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_combat__player__preferences__pb2.DESCRIPTOR,])




_COMBATPLAYERPROFILE_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='pogoprotos.data.combat.CombatPlayerProfile.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat_degree', full_name='pogoprotos.data.combat.CombatPlayerProfile.Location.lat_degree', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lng_degree', full_name='pogoprotos.data.combat.CombatPlayerProfile.Location.lng_degree', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=515,
  serialized_end=565,
)

_COMBATPLAYERPROFILE = _descriptor.Descriptor(
  name='CombatPlayerProfile',
  full_name='pogoprotos.data.combat.CombatPlayerProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.data.combat.CombatPlayerProfile.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_profile', full_name='pogoprotos.data.combat.CombatPlayerProfile.public_profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_league_template_id', full_name='pogoprotos.data.combat.CombatPlayerProfile.combat_league_template_id', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_pokemon_id', full_name='pogoprotos.data.combat.CombatPlayerProfile.buddy_pokemon_id', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='pogoprotos.data.combat.CombatPlayerProfile.location', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_player_preferences', full_name='pogoprotos.data.combat.CombatPlayerProfile.combat_player_preferences', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMBATPLAYERPROFILE_LOCATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=565,
)

_COMBATPLAYERPROFILE_LOCATION.containing_type = _COMBATPLAYERPROFILE
_COMBATPLAYERPROFILE.fields_by_name['public_profile'].message_type = pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2._PLAYERPUBLICPROFILE
_COMBATPLAYERPROFILE.fields_by_name['location'].message_type = _COMBATPLAYERPROFILE_LOCATION
_COMBATPLAYERPROFILE.fields_by_name['combat_player_preferences'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__player__preferences__pb2._COMBATPLAYERPREFERENCES
DESCRIPTOR.message_types_by_name['CombatPlayerProfile'] = _COMBATPLAYERPROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatPlayerProfile = _reflection.GeneratedProtocolMessageType('CombatPlayerProfile', (_message.Message,), dict(

  Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
    DESCRIPTOR = _COMBATPLAYERPROFILE_LOCATION,
    __module__ = 'pogoprotos.data.combat.combat_player_profile_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.CombatPlayerProfile.Location)
    ))
  ,
  DESCRIPTOR = _COMBATPLAYERPROFILE,
  __module__ = 'pogoprotos.data.combat.combat_player_profile_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.CombatPlayerProfile)
  ))
_sym_db.RegisterMessage(CombatPlayerProfile)
_sym_db.RegisterMessage(CombatPlayerProfile.Location)


# @@protoc_insertion_point(module_scope)
