# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tracking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etracking.proto\x12\tSafeEntry\"%\n\x11\x43heckInIndividual\x12\x10\n\x08location\x18\x02 \x01(\t\".\n\x0c\x43heckInGroup\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\"\"\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04nric\x18\x02 \x01(\t\"\x15\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\".\n\tSafeEntry\x12\x0f\n\x07\x63heckin\x18\x02 \x01(\t\x12\x10\n\x08\x63heckout\x18\x03 \x01(\t\"\x19\n\x06Status\x12\x0f\n\x07message\x18\x01 \x01(\t2\xce\x04\n\x0fTrackingService\x12-\n\x05Login\x12\x0f.SafeEntry.User\x1a\x11.SafeEntry.Status\"\x00\x12L\n\x17\x43reateCheckInIndividual\x12\x1c.SafeEntry.CheckInIndividual\x1a\x11.SafeEntry.Status\"\x00\x12M\n\x18\x43reateCheckOutIndividual\x12\x1c.SafeEntry.CheckInIndividual\x1a\x11.SafeEntry.Status\"\x00\x12\x42\n\x12\x43reateCheckInGroup\x12\x17.SafeEntry.CheckInGroup\x1a\x11.SafeEntry.Status\"\x00\x12\x43\n\x13\x43reateCheckOutGroup\x12\x17.SafeEntry.CheckInGroup\x1a\x11.SafeEntry.Status\"\x00\x12\x34\n\x0b\x43reateGroup\x12\x10.SafeEntry.Group\x1a\x11.SafeEntry.Status\"\x00\x12\x36\n\x0e\x41\x64\x64UserToGroup\x12\x0f.SafeEntry.User\x1a\x11.SafeEntry.Status\"\x00\x12\x39\n\x0cGetSafeEntry\x12\x0f.SafeEntry.User\x1a\x14.SafeEntry.SafeEntry\"\x00\x30\x01\x12=\n\x15\x43reateReportCovidCase\x12\x0f.SafeEntry.User\x1a\x11.SafeEntry.Status\"\x00\x62\x06proto3')



_CHECKININDIVIDUAL = DESCRIPTOR.message_types_by_name['CheckInIndividual']
_CHECKINGROUP = DESCRIPTOR.message_types_by_name['CheckInGroup']
_USER = DESCRIPTOR.message_types_by_name['User']
_GROUP = DESCRIPTOR.message_types_by_name['Group']
_SAFEENTRY = DESCRIPTOR.message_types_by_name['SafeEntry']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
CheckInIndividual = _reflection.GeneratedProtocolMessageType('CheckInIndividual', (_message.Message,), {
  'DESCRIPTOR' : _CHECKININDIVIDUAL,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.CheckInIndividual)
  })
_sym_db.RegisterMessage(CheckInIndividual)

CheckInGroup = _reflection.GeneratedProtocolMessageType('CheckInGroup', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINGROUP,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.CheckInGroup)
  })
_sym_db.RegisterMessage(CheckInGroup)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.User)
  })
_sym_db.RegisterMessage(User)

Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), {
  'DESCRIPTOR' : _GROUP,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.Group)
  })
_sym_db.RegisterMessage(Group)

SafeEntry = _reflection.GeneratedProtocolMessageType('SafeEntry', (_message.Message,), {
  'DESCRIPTOR' : _SAFEENTRY,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.SafeEntry)
  })
_sym_db.RegisterMessage(SafeEntry)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.Status)
  })
_sym_db.RegisterMessage(Status)

_TRACKINGSERVICE = DESCRIPTOR.services_by_name['TrackingService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHECKININDIVIDUAL._serialized_start=29
  _CHECKININDIVIDUAL._serialized_end=66
  _CHECKINGROUP._serialized_start=68
  _CHECKINGROUP._serialized_end=114
  _USER._serialized_start=116
  _USER._serialized_end=150
  _GROUP._serialized_start=152
  _GROUP._serialized_end=173
  _SAFEENTRY._serialized_start=175
  _SAFEENTRY._serialized_end=221
  _STATUS._serialized_start=223
  _STATUS._serialized_end=248
  _TRACKINGSERVICE._serialized_start=251
  _TRACKINGSERVICE._serialized_end=841
# @@protoc_insertion_point(module_scope)
