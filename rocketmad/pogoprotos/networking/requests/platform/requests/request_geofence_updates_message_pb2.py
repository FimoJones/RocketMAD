# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/platform/requests/request_geofence_updates_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/platform/requests/request_geofence_updates_message.proto',
  package='pogoprotos.networking.requests.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nWpogoprotos/networking/requests/platform/requests/request_geofence_updates_message.proto\x12\x30pogoprotos.networking.requests.platform.requests\"Y\n\x1dRequestGeofenceUpdatesMessage\x12\x18\n\x10number_of_points\x18\x01 \x01(\x05\x12\x1e\n\x16minimum_point_radius_m\x18\x02 \x01(\x01\x62\x06proto3')
)




_REQUESTGEOFENCEUPDATESMESSAGE = _descriptor.Descriptor(
  name='RequestGeofenceUpdatesMessage',
  full_name='pogoprotos.networking.requests.platform.requests.RequestGeofenceUpdatesMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_of_points', full_name='pogoprotos.networking.requests.platform.requests.RequestGeofenceUpdatesMessage.number_of_points', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum_point_radius_m', full_name='pogoprotos.networking.requests.platform.requests.RequestGeofenceUpdatesMessage.minimum_point_radius_m', index=1,
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
  serialized_start=141,
  serialized_end=230,
)

DESCRIPTOR.message_types_by_name['RequestGeofenceUpdatesMessage'] = _REQUESTGEOFENCEUPDATESMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestGeofenceUpdatesMessage = _reflection.GeneratedProtocolMessageType('RequestGeofenceUpdatesMessage', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTGEOFENCEUPDATESMESSAGE,
  __module__ = 'pogoprotos.networking.requests.platform.requests.request_geofence_updates_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.platform.requests.RequestGeofenceUpdatesMessage)
  ))
_sym_db.RegisterMessage(RequestGeofenceUpdatesMessage)


# @@protoc_insertion_point(module_scope)
