# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/responses/update_friendship_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/responses/update_friendship_response.proto',
  package='pogoprotos.networking.responses.social.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nQpogoprotos/networking/responses/social/responses/update_friendship_response.proto\x12\x30pogoprotos.networking.responses.social.responses\"\xa8\x02\n\x18UpdateFriendshipResponse\x12\x61\n\x06result\x18\x01 \x01(\x0e\x32Q.pogoprotos.networking.responses.social.responses.UpdateFriendshipResponse.Result\"\xa8\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x14\n\x10\x45RROR_NOT_FRIEND\x10\x03\x12\x1f\n\x1b\x45RROR_NICKNAME_WRONG_FORMAT\x10\x04\x12\x1b\n\x17\x45RROR_FILTERED_NICKNAME\x10\x05\x12\x1f\n\x1b\x45RROR_EXCEEDED_CHANGE_LIMIT\x10\x06\x62\x06proto3')
)



_UPDATEFRIENDSHIPRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.responses.UpdateFriendshipResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_FRIEND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NICKNAME_WRONG_FORMAT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FILTERED_NICKNAME', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_EXCEEDED_CHANGE_LIMIT', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=264,
  serialized_end=432,
)
_sym_db.RegisterEnumDescriptor(_UPDATEFRIENDSHIPRESPONSE_RESULT)


_UPDATEFRIENDSHIPRESPONSE = _descriptor.Descriptor(
  name='UpdateFriendshipResponse',
  full_name='pogoprotos.networking.responses.social.responses.UpdateFriendshipResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.responses.UpdateFriendshipResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPDATEFRIENDSHIPRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=432,
)

_UPDATEFRIENDSHIPRESPONSE.fields_by_name['result'].enum_type = _UPDATEFRIENDSHIPRESPONSE_RESULT
_UPDATEFRIENDSHIPRESPONSE_RESULT.containing_type = _UPDATEFRIENDSHIPRESPONSE
DESCRIPTOR.message_types_by_name['UpdateFriendshipResponse'] = _UPDATEFRIENDSHIPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateFriendshipResponse = _reflection.GeneratedProtocolMessageType('UpdateFriendshipResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFRIENDSHIPRESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.responses.update_friendship_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.responses.UpdateFriendshipResponse)
  ))
_sym_db.RegisterMessage(UpdateFriendshipResponse)


# @@protoc_insertion_point(module_scope)
