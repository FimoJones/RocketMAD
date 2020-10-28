# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/use_item_move_reroll_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/use_item_move_reroll_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCpogoprotos/networking/responses/use_item_move_reroll_response.proto\x12\x1fpogoprotos.networking.responses\x1a\"pogoprotos/data/pokemon_data.proto\"\x86\x03\n\x19UseItemMoveRerollResponse\x12Q\n\x06result\x18\x01 \x01(\x0e\x32\x41.pogoprotos.networking.responses.UseItemMoveRerollResponse.Result\x12\x35\n\x0fupdated_pokemon\x18\x02 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\"\xde\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0e\n\nNO_POKEMON\x10\x02\x12\x12\n\x0eNO_OTHER_MOVES\x10\x03\x12\r\n\tNO_PLAYER\x10\x04\x12\x13\n\x0fWRONG_ITEM_TYPE\x10\x05\x12\x19\n\x15ITEM_NOT_IN_INVENTORY\x10\x06\x12\x13\n\x0fINVALID_POKEMON\x10\x07\x12\x0f\n\x0bMOVE_LOCKED\x10\x08\x12\x1b\n\x17MOVE_CANNOT_BE_REROLLED\x10\t\x12\x16\n\x12INVALID_ELITE_MOVE\x10\nb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,])



_USEITEMMOVEREROLLRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.UseItemMoveRerollResponse.Result',
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
      name='NO_POKEMON', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_OTHER_MOVES', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_PLAYER', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_ITEM_TYPE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_NOT_IN_INVENTORY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_POKEMON', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_LOCKED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_CANNOT_BE_REROLLED', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ELITE_MOVE', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=309,
  serialized_end=531,
)
_sym_db.RegisterEnumDescriptor(_USEITEMMOVEREROLLRESPONSE_RESULT)


_USEITEMMOVEREROLLRESPONSE = _descriptor.Descriptor(
  name='UseItemMoveRerollResponse',
  full_name='pogoprotos.networking.responses.UseItemMoveRerollResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.UseItemMoveRerollResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_pokemon', full_name='pogoprotos.networking.responses.UseItemMoveRerollResponse.updated_pokemon', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USEITEMMOVEREROLLRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=531,
)

_USEITEMMOVEREROLLRESPONSE.fields_by_name['result'].enum_type = _USEITEMMOVEREROLLRESPONSE_RESULT
_USEITEMMOVEREROLLRESPONSE.fields_by_name['updated_pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_USEITEMMOVEREROLLRESPONSE_RESULT.containing_type = _USEITEMMOVEREROLLRESPONSE
DESCRIPTOR.message_types_by_name['UseItemMoveRerollResponse'] = _USEITEMMOVEREROLLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UseItemMoveRerollResponse = _reflection.GeneratedProtocolMessageType('UseItemMoveRerollResponse', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMMOVEREROLLRESPONSE,
  __module__ = 'pogoprotos.networking.responses.use_item_move_reroll_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.UseItemMoveRerollResponse)
  ))
_sym_db.RegisterMessage(UseItemMoveRerollResponse)


# @@protoc_insertion_point(module_scope)
