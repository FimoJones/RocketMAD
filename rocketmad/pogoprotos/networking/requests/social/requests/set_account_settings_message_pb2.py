# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/requests/set_account_settings_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings import account_settings_pb2 as pogoprotos_dot_settings_dot_account__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/social/requests/set_account_settings_message.proto',
  package='pogoprotos.networking.requests.social.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nQpogoprotos/networking/requests/social/requests/set_account_settings_message.proto\x12.pogoprotos.networking.requests.social.requests\x1a*pogoprotos/settings/account_settings.proto\"S\n\x19SetAccountSettingsMessage\x12\x36\n\x08settings\x18\x01 \x01(\x0b\x32$.pogoprotos.settings.AccountSettingsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_account__settings__pb2.DESCRIPTOR,])




_SETACCOUNTSETTINGSMESSAGE = _descriptor.Descriptor(
  name='SetAccountSettingsMessage',
  full_name='pogoprotos.networking.requests.social.requests.SetAccountSettingsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='pogoprotos.networking.requests.social.requests.SetAccountSettingsMessage.settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=177,
  serialized_end=260,
)

_SETACCOUNTSETTINGSMESSAGE.fields_by_name['settings'].message_type = pogoprotos_dot_settings_dot_account__settings__pb2._ACCOUNTSETTINGS
DESCRIPTOR.message_types_by_name['SetAccountSettingsMessage'] = _SETACCOUNTSETTINGSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetAccountSettingsMessage = _reflection.GeneratedProtocolMessageType('SetAccountSettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _SETACCOUNTSETTINGSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.requests.set_account_settings_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.requests.SetAccountSettingsMessage)
  ))
_sym_db.RegisterMessage(SetAccountSettingsMessage)


# @@protoc_insertion_point(module_scope)
