# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/game/gameiap/responses/redeem_apple_receipt_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/game/gameiap/responses/redeem_apple_receipt_response.proto',
  package='pogoprotos.networking.responses.game.gameiap.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nZpogoprotos/networking/responses/game/gameiap/responses/redeem_apple_receipt_response.proto\x12\x36pogoprotos.networking.responses.game.gameiap.responses\"s\n\x1aRedeemAppleReceiptResponse\x12&\n\x1eprovisioned_transaction_tokens\x18\x01 \x03(\t\"-\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3')
)



_REDEEMAPPLERECEIPTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.game.gameiap.responses.RedeemAppleReceiptResponse.Status',
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
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=220,
  serialized_end=265,
)
_sym_db.RegisterEnumDescriptor(_REDEEMAPPLERECEIPTRESPONSE_STATUS)


_REDEEMAPPLERECEIPTRESPONSE = _descriptor.Descriptor(
  name='RedeemAppleReceiptResponse',
  full_name='pogoprotos.networking.responses.game.gameiap.responses.RedeemAppleReceiptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provisioned_transaction_tokens', full_name='pogoprotos.networking.responses.game.gameiap.responses.RedeemAppleReceiptResponse.provisioned_transaction_tokens', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REDEEMAPPLERECEIPTRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=265,
)

_REDEEMAPPLERECEIPTRESPONSE_STATUS.containing_type = _REDEEMAPPLERECEIPTRESPONSE
DESCRIPTOR.message_types_by_name['RedeemAppleReceiptResponse'] = _REDEEMAPPLERECEIPTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedeemAppleReceiptResponse = _reflection.GeneratedProtocolMessageType('RedeemAppleReceiptResponse', (_message.Message,), dict(
  DESCRIPTOR = _REDEEMAPPLERECEIPTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.game.gameiap.responses.redeem_apple_receipt_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.game.gameiap.responses.RedeemAppleReceiptResponse)
  ))
_sym_db.RegisterMessage(RedeemAppleReceiptResponse)


# @@protoc_insertion_point(module_scope)
