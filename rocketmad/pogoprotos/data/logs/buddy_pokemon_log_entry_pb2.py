# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/buddy_pokemon_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/buddy_pokemon_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2pogoprotos/data/logs/buddy_pokemon_log_entry.proto\x12\x14pogoprotos.data.logs\x1a!pogoprotos/enums/pokemon_id.proto\x1a%pogoprotos/data/pokemon_display.proto\"\x90\x02\n\x14\x42uddyPokemonLogEntry\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.pogoprotos.data.logs.BuddyPokemonLogEntry.Result\x12\x31\n\x0cpokemon_type\x18\x02 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05\x12\x38\n\x0fpokemon_display\x18\x04 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\x12\x12\n\npokemon_id\x18\x05 \x01(\x06\"$\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0f\n\x0b\x43\x41NDY_FOUND\x10\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,])



_BUDDYPOKEMONLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.logs.BuddyPokemonLogEntry.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANDY_FOUND', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=387,
  serialized_end=423,
)
_sym_db.RegisterEnumDescriptor(_BUDDYPOKEMONLOGENTRY_RESULT)


_BUDDYPOKEMONLOGENTRY = _descriptor.Descriptor(
  name='BuddyPokemonLogEntry',
  full_name='pogoprotos.data.logs.BuddyPokemonLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.logs.BuddyPokemonLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_type', full_name='pogoprotos.data.logs.BuddyPokemonLogEntry.pokemon_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='pogoprotos.data.logs.BuddyPokemonLogEntry.amount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.data.logs.BuddyPokemonLogEntry.pokemon_display', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.logs.BuddyPokemonLogEntry.pokemon_id', index=4,
      number=5, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BUDDYPOKEMONLOGENTRY_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=423,
)

_BUDDYPOKEMONLOGENTRY.fields_by_name['result'].enum_type = _BUDDYPOKEMONLOGENTRY_RESULT
_BUDDYPOKEMONLOGENTRY.fields_by_name['pokemon_type'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_BUDDYPOKEMONLOGENTRY.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_BUDDYPOKEMONLOGENTRY_RESULT.containing_type = _BUDDYPOKEMONLOGENTRY
DESCRIPTOR.message_types_by_name['BuddyPokemonLogEntry'] = _BUDDYPOKEMONLOGENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuddyPokemonLogEntry = _reflection.GeneratedProtocolMessageType('BuddyPokemonLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _BUDDYPOKEMONLOGENTRY,
  __module__ = 'pogoprotos.data.logs.buddy_pokemon_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.BuddyPokemonLogEntry)
  ))
_sym_db.RegisterMessage(BuddyPokemonLogEntry)


# @@protoc_insertion_point(module_scope)
