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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etracking.proto\x12\tSafeEntry\"\x07\n\x05\x45mpty\"y\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04nric\x18\x02 \x01(\t\x12\x11\n\trole_name\x18\x03 \x01(\t\x12\x1f\n\x05group\x18\x04 \x01(\x0b\x32\x10.SafeEntry.Group\x12!\n\x06status\x18\x05 \x01(\x0b\x32\x11.SafeEntry.Status\"\x15\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x18\n\x08Location\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x11\x43heckInIndividual\x12\x10\n\x08location\x18\x02 \x01(\t\".\n\x0c\x43heckInGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\".\n\tSafeEntry\x12\x0f\n\x07\x63heckin\x18\x02 \x01(\t\x12\x10\n\x08\x63heckout\x18\x03 \x01(\t\"L\n\x04\x43\x61se\x12\x1d\n\x04user\x18\x01 \x01(\x0b\x32\x0f.SafeEntry.User\x12%\n\x08location\x18\x02 \x01(\x0b\x32\x13.SafeEntry.Location2\xc8\x05\n\x0fTrackingService\x12+\n\x05Login\x12\x0f.SafeEntry.User\x1a\x0f.SafeEntry.User\"\x00\x12<\n\x0fGetAllLocations\x12\x10.SafeEntry.Empty\x1a\x13.SafeEntry.Location\"\x00\x30\x01\x12L\n\x17\x43reateCheckInIndividual\x12\x1c.SafeEntry.CheckInIndividual\x1a\x11.SafeEntry.Status\"\x00\x12M\n\x18\x43reateCheckOutIndividual\x12\x1c.SafeEntry.CheckInIndividual\x1a\x11.SafeEntry.Status\"\x00\x12\x42\n\x12\x43reateCheckInGroup\x12\x17.SafeEntry.CheckInGroup\x1a\x11.SafeEntry.Status\"\x00\x12\x43\n\x13\x43reateCheckOutGroup\x12\x17.SafeEntry.CheckInGroup\x1a\x11.SafeEntry.Status\"\x00\x12\x34\n\x0b\x43reateGroup\x12\x10.SafeEntry.Group\x1a\x11.SafeEntry.Status\"\x00\x12\x38\n\x0e\x41\x64\x64UserToGroup\x12\x0f.SafeEntry.User\x1a\x11.SafeEntry.Status\"\x00(\x01\x12:\n\x0cGetSafeEntry\x12\x10.SafeEntry.Empty\x1a\x14.SafeEntry.SafeEntry\"\x00\x30\x01\x12=\n\x15\x43reateReportCovidCase\x12\x0f.SafeEntry.Case\x1a\x11.SafeEntry.Status\"\x00\x12\x39\n\x0fGetGroupsByUser\x12\x10.SafeEntry.Empty\x1a\x10.SafeEntry.Group\"\x00\x30\x01\x62\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_USER = DESCRIPTOR.message_types_by_name['User']
_GROUP = DESCRIPTOR.message_types_by_name['Group']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
_LOCATION = DESCRIPTOR.message_types_by_name['Location']
_CHECKININDIVIDUAL = DESCRIPTOR.message_types_by_name['CheckInIndividual']
_CHECKINGROUP = DESCRIPTOR.message_types_by_name['CheckInGroup']
_SAFEENTRY = DESCRIPTOR.message_types_by_name['SafeEntry']
_CASE = DESCRIPTOR.message_types_by_name['Case']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.Empty)
  })
_sym_db.RegisterMessage(Empty)

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

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.Status)
  })
_sym_db.RegisterMessage(Status)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.Location)
  })
_sym_db.RegisterMessage(Location)

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

SafeEntry = _reflection.GeneratedProtocolMessageType('SafeEntry', (_message.Message,), {
  'DESCRIPTOR' : _SAFEENTRY,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.SafeEntry)
  })
_sym_db.RegisterMessage(SafeEntry)

Case = _reflection.GeneratedProtocolMessageType('Case', (_message.Message,), {
  'DESCRIPTOR' : _CASE,
  '__module__' : 'tracking_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.Case)
  })
_sym_db.RegisterMessage(Case)

_TRACKINGSERVICE = DESCRIPTOR.services_by_name['TrackingService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=29
  _EMPTY._serialized_end=36
  _USER._serialized_start=38
  _USER._serialized_end=159
  _GROUP._serialized_start=161
  _GROUP._serialized_end=182
  _STATUS._serialized_start=184
  _STATUS._serialized_end=208
  _LOCATION._serialized_start=210
  _LOCATION._serialized_end=234
  _CHECKININDIVIDUAL._serialized_start=236
  _CHECKININDIVIDUAL._serialized_end=273
  _CHECKINGROUP._serialized_start=275
  _CHECKINGROUP._serialized_end=321
  _SAFEENTRY._serialized_start=323
  _SAFEENTRY._serialized_end=369
  _CASE._serialized_start=371
  _CASE._serialized_end=447
  _TRACKINGSERVICE._serialized_start=450
  _TRACKINGSERVICE._serialized_end=1162
# @@protoc_insertion_point(module_scope)
