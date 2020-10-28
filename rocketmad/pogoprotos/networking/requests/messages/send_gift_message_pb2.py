# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/send_gift_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.sticker import sticker_sent_pb2 as pogoprotos_dot_data_dot_sticker_dot_sticker__sent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/send_gift_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?pogoprotos/networking/requests/messages/send_gift_message.proto\x12\'pogoprotos.networking.requests.messages\x1a*pogoprotos/data/sticker/sticker_sent.proto\"u\n\x0fSendGiftMessage\x12\x12\n\ngiftbox_id\x18\x01 \x01(\x04\x12\x11\n\tplayer_id\x18\x02 \x01(\t\x12;\n\rstickers_sent\x18\x03 \x03(\x0b\x32$.pogoprotos.data.sticker.StickerSentb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_sticker_dot_sticker__sent__pb2.DESCRIPTOR,])




_SENDGIFTMESSAGE = _descriptor.Descriptor(
  name='SendGiftMessage',
  full_name='pogoprotos.networking.requests.messages.SendGiftMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='giftbox_id', full_name='pogoprotos.networking.requests.messages.SendGiftMessage.giftbox_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.networking.requests.messages.SendGiftMessage.player_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stickers_sent', full_name='pogoprotos.networking.requests.messages.SendGiftMessage.stickers_sent', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=152,
  serialized_end=269,
)

_SENDGIFTMESSAGE.fields_by_name['stickers_sent'].message_type = pogoprotos_dot_data_dot_sticker_dot_sticker__sent__pb2._STICKERSENT
DESCRIPTOR.message_types_by_name['SendGiftMessage'] = _SENDGIFTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendGiftMessage = _reflection.GeneratedProtocolMessageType('SendGiftMessage', (_message.Message,), dict(
  DESCRIPTOR = _SENDGIFTMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.send_gift_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SendGiftMessage)
  ))
_sym_db.RegisterMessage(SendGiftMessage)


# @@protoc_insertion_point(module_scope)
