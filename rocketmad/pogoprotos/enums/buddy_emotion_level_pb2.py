# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/buddy_emotion_level.proto

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
  name='pogoprotos/enums/buddy_emotion_level.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*pogoprotos/enums/buddy_emotion_level.proto\x12\x10pogoprotos.enums*\xef\x01\n\x11\x42uddyEmotionLevel\x12\x1d\n\x19\x42UDDY_EMOTION_LEVEL_UNSET\x10\x00\x12\x19\n\x15\x42UDDY_EMOTION_LEVEL_0\x10\x01\x12\x19\n\x15\x42UDDY_EMOTION_LEVEL_1\x10\x02\x12\x19\n\x15\x42UDDY_EMOTION_LEVEL_2\x10\x03\x12\x19\n\x15\x42UDDY_EMOTION_LEVEL_3\x10\x04\x12\x19\n\x15\x42UDDY_EMOTION_LEVEL_4\x10\x05\x12\x19\n\x15\x42UDDY_EMOTION_LEVEL_5\x10\x06\x12\x19\n\x15\x42UDDY_EMOTION_LEVEL_6\x10\x07\x62\x06proto3')
)

_BUDDYEMOTIONLEVEL = _descriptor.EnumDescriptor(
  name='BuddyEmotionLevel',
  full_name='pogoprotos.enums.BuddyEmotionLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUDDY_EMOTION_LEVEL_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_EMOTION_LEVEL_0', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_EMOTION_LEVEL_1', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_EMOTION_LEVEL_2', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_EMOTION_LEVEL_3', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_EMOTION_LEVEL_4', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_EMOTION_LEVEL_5', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_EMOTION_LEVEL_6', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=65,
  serialized_end=304,
)
_sym_db.RegisterEnumDescriptor(_BUDDYEMOTIONLEVEL)

BuddyEmotionLevel = enum_type_wrapper.EnumTypeWrapper(_BUDDYEMOTIONLEVEL)
BUDDY_EMOTION_LEVEL_UNSET = 0
BUDDY_EMOTION_LEVEL_0 = 1
BUDDY_EMOTION_LEVEL_1 = 2
BUDDY_EMOTION_LEVEL_2 = 3
BUDDY_EMOTION_LEVEL_3 = 4
BUDDY_EMOTION_LEVEL_4 = 5
BUDDY_EMOTION_LEVEL_5 = 6
BUDDY_EMOTION_LEVEL_6 = 7


DESCRIPTOR.enum_types_by_name['BuddyEmotionLevel'] = _BUDDYEMOTIONLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
