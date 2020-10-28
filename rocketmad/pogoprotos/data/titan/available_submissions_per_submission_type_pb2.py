# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/titan/available_submissions_per_submission_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import player_submission_type_pb2 as pogoprotos_dot_enums_dot_player__submission__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/titan/available_submissions_per_submission_type.proto',
  package='pogoprotos.data.titan',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nEpogoprotos/data/titan/available_submissions_per_submission_type.proto\x12\x15pogoprotos.data.titan\x1a-pogoprotos/enums/player_submission_type.proto\"\xe5\x02\n%AvailableSubmissionsPerSubmissionType\x12\x46\n\x16player_submission_type\x18\x01 \x01(\x0e\x32&.pogoprotos.enums.PlayerSubmissionType\x12\x18\n\x10submissions_left\x18\x02 \x01(\x05\x12\x18\n\x10min_player_level\x18\x03 \x01(\x05\x12\x1a\n\x12is_feature_enabled\x18\x04 \x01(\x08\x12,\n$time_window_for_submissions_limit_ms\x18\x05 \x01(\x03\x12\"\n\x1amax_poi_distance_in_meters\x18\x06 \x01(\x05\x12\x16\n\x0e\x62lacklisted_os\x18\x07 \x03(\t\x12\x1d\n\x15\x62lacklisted_device_id\x18\x08 \x03(\t\x12\x1b\n\x13is_whitelisted_user\x18\t \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_player__submission__type__pb2.DESCRIPTOR,])




_AVAILABLESUBMISSIONSPERSUBMISSIONTYPE = _descriptor.Descriptor(
  name='AvailableSubmissionsPerSubmissionType',
  full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_submission_type', full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType.player_submission_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submissions_left', full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType.submissions_left', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_player_level', full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType.min_player_level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_feature_enabled', full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType.is_feature_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_window_for_submissions_limit_ms', full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType.time_window_for_submissions_limit_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_poi_distance_in_meters', full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType.max_poi_distance_in_meters', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blacklisted_os', full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType.blacklisted_os', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blacklisted_device_id', full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType.blacklisted_device_id', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_whitelisted_user', full_name='pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType.is_whitelisted_user', index=8,
      number=9, type=8, cpp_type=7, label=1,
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
  serialized_start=144,
  serialized_end=501,
)

_AVAILABLESUBMISSIONSPERSUBMISSIONTYPE.fields_by_name['player_submission_type'].enum_type = pogoprotos_dot_enums_dot_player__submission__type__pb2._PLAYERSUBMISSIONTYPE
DESCRIPTOR.message_types_by_name['AvailableSubmissionsPerSubmissionType'] = _AVAILABLESUBMISSIONSPERSUBMISSIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvailableSubmissionsPerSubmissionType = _reflection.GeneratedProtocolMessageType('AvailableSubmissionsPerSubmissionType', (_message.Message,), dict(
  DESCRIPTOR = _AVAILABLESUBMISSIONSPERSUBMISSIONTYPE,
  __module__ = 'pogoprotos.data.titan.available_submissions_per_submission_type_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType)
  ))
_sym_db.RegisterMessage(AvailableSubmissionsPerSubmissionType)


# @@protoc_insertion_point(module_scope)
