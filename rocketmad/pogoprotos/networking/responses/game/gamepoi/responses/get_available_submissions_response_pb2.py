# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/game/gamepoi/responses/get_available_submissions_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.titan import available_submissions_per_submission_type_pb2 as pogoprotos_dot_data_dot_titan_dot_available__submissions__per__submission__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/game/gamepoi/responses/get_available_submissions_response.proto',
  package='pogoprotos.networking.responses.game.gamepoi.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n_pogoprotos/networking/responses/game/gamepoi/responses/get_available_submissions_response.proto\x12\x36pogoprotos.networking.responses.game.gamepoi.responses\x1a\x45pogoprotos/data/titan/available_submissions_per_submission_type.proto\"\xab\x03\n\x1fGetAvailableSubmissionsResponse\x12\x18\n\x10submissions_left\x18\x01 \x01(\x05\x12\x18\n\x10min_player_level\x18\x02 \x01(\x05\x12\x17\n\x0fhas_valid_email\x18\x03 \x01(\x08\x12\x1a\n\x12is_feature_enabled\x18\x04 \x01(\x08\x12,\n$time_window_for_submissions_limit_ms\x18\x05 \x01(\x03\x12\"\n\x1amax_poi_distance_in_meters\x18\x06 \x01(\x05\x12\x16\n\x0e\x62lacklisted_os\x18\x07 \x03(\t\x12\x62\n\x1c\x61vailability_result_per_type\x18\x08 \x03(\x0b\x32<.pogoprotos.data.titan.AvailableSubmissionsPerSubmissionType\x12\x1d\n\x15\x62lacklisted_device_id\x18\t \x03(\t\x12\x32\n*max_poi_location_edit_move_distance_meters\x18\n \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_titan_dot_available__submissions__per__submission__type__pb2.DESCRIPTOR,])




_GETAVAILABLESUBMISSIONSRESPONSE = _descriptor.Descriptor(
  name='GetAvailableSubmissionsResponse',
  full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='submissions_left', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.submissions_left', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_player_level', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.min_player_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_valid_email', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.has_valid_email', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_feature_enabled', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.is_feature_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_window_for_submissions_limit_ms', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.time_window_for_submissions_limit_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_poi_distance_in_meters', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.max_poi_distance_in_meters', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blacklisted_os', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.blacklisted_os', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='availability_result_per_type', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.availability_result_per_type', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blacklisted_device_id', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.blacklisted_device_id', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_poi_location_edit_move_distance_meters', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse.max_poi_location_edit_move_distance_meters', index=9,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=227,
  serialized_end=654,
)

_GETAVAILABLESUBMISSIONSRESPONSE.fields_by_name['availability_result_per_type'].message_type = pogoprotos_dot_data_dot_titan_dot_available__submissions__per__submission__type__pb2._AVAILABLESUBMISSIONSPERSUBMISSIONTYPE
DESCRIPTOR.message_types_by_name['GetAvailableSubmissionsResponse'] = _GETAVAILABLESUBMISSIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAvailableSubmissionsResponse = _reflection.GeneratedProtocolMessageType('GetAvailableSubmissionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETAVAILABLESUBMISSIONSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.game.gamepoi.responses.get_available_submissions_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.game.gamepoi.responses.GetAvailableSubmissionsResponse)
  ))
_sym_db.RegisterMessage(GetAvailableSubmissionsResponse)


# @@protoc_insertion_point(module_scope)
