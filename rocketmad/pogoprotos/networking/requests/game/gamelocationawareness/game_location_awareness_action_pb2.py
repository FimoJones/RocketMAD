# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gamelocationawareness/game_location_awareness_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gamelocationawareness/game_location_awareness_action.proto',
  package='pogoprotos.networking.requests.game.gamelocationawareness',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n^pogoprotos/networking/requests/game/gamelocationawareness/game_location_awareness_action.proto\x12\x39pogoprotos.networking.requests.game.gamelocationawareness*\x87\x01\n\x1bGameLocationAwarenessAction\x12*\n&UNKNOWN_GAME_LOCATION_AWARENESS_ACTION\x10\x00\x12\x1e\n\x18REQUEST_GEOFENCE_UPDATES\x10\xc0\xfc\x15\x12\x1c\n\x16UPDATE_PLAYER_LOCATION\x10\xc1\xfc\x15\x62\x06proto3')
)

_GAMELOCATIONAWARENESSACTION = _descriptor.EnumDescriptor(
  name='GameLocationAwarenessAction',
  full_name='pogoprotos.networking.requests.game.gamelocationawareness.GameLocationAwarenessAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_GAME_LOCATION_AWARENESS_ACTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_GEOFENCE_UPDATES', index=1, number=360000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_PLAYER_LOCATION', index=2, number=360001,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=158,
  serialized_end=293,
)
_sym_db.RegisterEnumDescriptor(_GAMELOCATIONAWARENESSACTION)

GameLocationAwarenessAction = enum_type_wrapper.EnumTypeWrapper(_GAMELOCATIONAWARENESSACTION)
UNKNOWN_GAME_LOCATION_AWARENESS_ACTION = 0
REQUEST_GEOFENCE_UPDATES = 360000
UPDATE_PLAYER_LOCATION = 360001


DESCRIPTOR.enum_types_by_name['GameLocationAwarenessAction'] = _GAMELOCATIONAWARENESSACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
