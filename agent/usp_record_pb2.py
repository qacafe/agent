# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: usp-record.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='usp-record.proto',
  package='usp_record',
  syntax='proto3',
  serialized_pb=_b('\n\x10usp-record.proto\x12\nusp_record\"\xdc\x02\n\x06Record\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\r\n\x05to_id\x18\x02 \x01(\t\x12\x0f\n\x07\x66rom_id\x18\x03 \x01(\t\x12<\n\x10payload_security\x18\x04 \x01(\x0e\x32\".usp_record.Record.PayloadSecurity\x12\x15\n\rmac_signature\x18\x05 \x01(\x0c\x12\x13\n\x0bsender_cert\x18\x06 \x01(\x0c\x12@\n\x12no_session_context\x18\x07 \x01(\x0b\x32\".usp_record.NoSessionContextRecordH\x00\x12;\n\x0fsession_context\x18\x08 \x01(\x0b\x32 .usp_record.SessionContextRecordH\x00\")\n\x0fPayloadSecurity\x12\r\n\tPLAINTEXT\x10\x00\x12\x07\n\x03TLS\x10\x01\x42\r\n\x0brecord_type\")\n\x16NoSessionContextRecord\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"\xde\x02\n\x14SessionContextRecord\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x13\n\x0bsequence_id\x18\x02 \x01(\x04\x12\x13\n\x0b\x65xpected_id\x18\x03 \x01(\x04\x12\x15\n\rretransmit_id\x18\x04 \x01(\x04\x12K\n\x11payload_sar_state\x18\x05 \x01(\x0e\x32\x30.usp_record.SessionContextRecord.PayloadSARState\x12N\n\x14payloadrec_sar_state\x18\x06 \x01(\x0e\x32\x30.usp_record.SessionContextRecord.PayloadSARState\x12\x0f\n\x07payload\x18\x07 \x03(\x0c\"C\n\x0fPayloadSARState\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x42\x45GIN\x10\x01\x12\r\n\tINPROCESS\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\x62\x06proto3')
)



_RECORD_PAYLOADSECURITY = _descriptor.EnumDescriptor(
  name='PayloadSecurity',
  full_name='usp_record.Record.PayloadSecurity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLAINTEXT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TLS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=325,
  serialized_end=366,
)
_sym_db.RegisterEnumDescriptor(_RECORD_PAYLOADSECURITY)

_SESSIONCONTEXTRECORD_PAYLOADSARSTATE = _descriptor.EnumDescriptor(
  name='PayloadSARState',
  full_name='usp_record.SessionContextRecord.PayloadSARState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEGIN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INPROCESS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=710,
  serialized_end=777,
)
_sym_db.RegisterEnumDescriptor(_SESSIONCONTEXTRECORD_PAYLOADSARSTATE)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='usp_record.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='usp_record.Record.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_id', full_name='usp_record.Record.to_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_id', full_name='usp_record.Record.from_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload_security', full_name='usp_record.Record.payload_security', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mac_signature', full_name='usp_record.Record.mac_signature', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_cert', full_name='usp_record.Record.sender_cert', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_session_context', full_name='usp_record.Record.no_session_context', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_context', full_name='usp_record.Record.session_context', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECORD_PAYLOADSECURITY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='record_type', full_name='usp_record.Record.record_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=33,
  serialized_end=381,
)


_NOSESSIONCONTEXTRECORD = _descriptor.Descriptor(
  name='NoSessionContextRecord',
  full_name='usp_record.NoSessionContextRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='usp_record.NoSessionContextRecord.payload', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=424,
)


_SESSIONCONTEXTRECORD = _descriptor.Descriptor(
  name='SessionContextRecord',
  full_name='usp_record.SessionContextRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='usp_record.SessionContextRecord.session_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_id', full_name='usp_record.SessionContextRecord.sequence_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected_id', full_name='usp_record.SessionContextRecord.expected_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retransmit_id', full_name='usp_record.SessionContextRecord.retransmit_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload_sar_state', full_name='usp_record.SessionContextRecord.payload_sar_state', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payloadrec_sar_state', full_name='usp_record.SessionContextRecord.payloadrec_sar_state', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='usp_record.SessionContextRecord.payload', index=6,
      number=7, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SESSIONCONTEXTRECORD_PAYLOADSARSTATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=777,
)

_RECORD.fields_by_name['payload_security'].enum_type = _RECORD_PAYLOADSECURITY
_RECORD.fields_by_name['no_session_context'].message_type = _NOSESSIONCONTEXTRECORD
_RECORD.fields_by_name['session_context'].message_type = _SESSIONCONTEXTRECORD
_RECORD_PAYLOADSECURITY.containing_type = _RECORD
_RECORD.oneofs_by_name['record_type'].fields.append(
  _RECORD.fields_by_name['no_session_context'])
_RECORD.fields_by_name['no_session_context'].containing_oneof = _RECORD.oneofs_by_name['record_type']
_RECORD.oneofs_by_name['record_type'].fields.append(
  _RECORD.fields_by_name['session_context'])
_RECORD.fields_by_name['session_context'].containing_oneof = _RECORD.oneofs_by_name['record_type']
_SESSIONCONTEXTRECORD.fields_by_name['payload_sar_state'].enum_type = _SESSIONCONTEXTRECORD_PAYLOADSARSTATE
_SESSIONCONTEXTRECORD.fields_by_name['payloadrec_sar_state'].enum_type = _SESSIONCONTEXTRECORD_PAYLOADSARSTATE
_SESSIONCONTEXTRECORD_PAYLOADSARSTATE.containing_type = _SESSIONCONTEXTRECORD
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['NoSessionContextRecord'] = _NOSESSIONCONTEXTRECORD
DESCRIPTOR.message_types_by_name['SessionContextRecord'] = _SESSIONCONTEXTRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), dict(
  DESCRIPTOR = _RECORD,
  __module__ = 'usp_record_pb2'
  # @@protoc_insertion_point(class_scope:usp_record.Record)
  ))
_sym_db.RegisterMessage(Record)

NoSessionContextRecord = _reflection.GeneratedProtocolMessageType('NoSessionContextRecord', (_message.Message,), dict(
  DESCRIPTOR = _NOSESSIONCONTEXTRECORD,
  __module__ = 'usp_record_pb2'
  # @@protoc_insertion_point(class_scope:usp_record.NoSessionContextRecord)
  ))
_sym_db.RegisterMessage(NoSessionContextRecord)

SessionContextRecord = _reflection.GeneratedProtocolMessageType('SessionContextRecord', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONCONTEXTRECORD,
  __module__ = 'usp_record_pb2'
  # @@protoc_insertion_point(class_scope:usp_record.SessionContextRecord)
  ))
_sym_db.RegisterMessage(SessionContextRecord)


# @@protoc_insertion_point(module_scope)
