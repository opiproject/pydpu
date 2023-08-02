# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frontend_virtio_blk.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import opicommon_pb2 as opicommon__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x66rontend_virtio_blk.proto\x12\x12opi_api.storage.v1\x1a\x0fopicommon.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a google/protobuf/field_mask.proto\"\xc1\x02\n\tVirtioBlk\x12\x35\n\x04name\x18\x01 \x01(\tB\'\xe0\x41\x03\xe0\x41\x05\xfa\x41\x1e\n\x1copi_api.storage.v1/VirtioBlk\x12\x30\n\x07pcie_id\x18\x02 \x01(\x0b\x32\x1f.opi_api.storage.v1.PciEndpoint\x12\x1c\n\x0fvolume_name_ref\x18\x03 \x01(\tB\x03\xe0\x41\x02\x12\x12\n\nmax_io_qps\x18\x04 \x01(\x03\x12/\n\tmin_limit\x18\x05 \x01(\x0b\x32\x1c.opi_api.storage.v1.QosLimit\x12/\n\tmax_limit\x18\x06 \x01(\x0b\x32\x1c.opi_api.storage.v1.QosLimit:7\xea\x41\x34\n storage.opiproject.org/VirtioBlk\x12\x10volumes/{volume}\"g\n\x16\x43reateVirtioBlkRequest\x12\x36\n\nvirtio_blk\x18\x01 \x01(\x0b\x32\x1d.opi_api.storage.v1.VirtioBlkB\x03\xe0\x41\x02\x12\x15\n\rvirtio_blk_id\x18\x02 \x01(\t\"c\n\x16\x44\x65leteVirtioBlkRequest\x12\x32\n\x04name\x18\x01 \x01(\tB$\xe0\x41\x02\xfa\x41\x1e\n\x1copi_api.storage.v1/VirtioBlk\x12\x15\n\rallow_missing\x18\x02 \x01(\x08\"\x93\x01\n\x16UpdateVirtioBlkRequest\x12\x31\n\nvirtio_blk\x18\x01 \x01(\x0b\x32\x1d.opi_api.storage.v1.VirtioBlk\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x15\n\rallow_missing\x18\x03 \x01(\x08\"t\n\x15ListVirtioBlksRequest\x12\x34\n\x06parent\x18\x01 \x01(\tB$\xe0\x41\x02\xfa\x41\x1e\n\x1copi_api.storage.v1/VirtioBlk\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"e\n\x16ListVirtioBlksResponse\x12\x32\n\x0bvirtio_blks\x18\x01 \x03(\x0b\x32\x1d.opi_api.storage.v1.VirtioBlk\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"I\n\x13GetVirtioBlkRequest\x12\x32\n\x04name\x18\x01 \x01(\tB$\xe0\x41\x02\xfa\x41\x1e\n\x1copi_api.storage.v1/VirtioBlk\"K\n\x15StatsVirtioBlkRequest\x12\x32\n\x04name\x18\x01 \x01(\tB$\xe0\x41\x02\xfa\x41\x1e\n\x1copi_api.storage.v1/VirtioBlk\"H\n\x16StatsVirtioBlkResponse\x12.\n\x05stats\x18\x01 \x01(\x0b\x32\x1f.opi_api.storage.v1.VolumeStats2\x8e\x07\n\x18\x46rontendVirtioBlkService\x12\x98\x01\n\x0f\x43reateVirtioBlk\x12*.opi_api.storage.v1.CreateVirtioBlkRequest\x1a\x1d.opi_api.storage.v1.VirtioBlk\":\x82\xd3\xe4\x93\x02\x19\"\x0b/v1/volumes:\nvirtio_blk\xda\x41\x18virtio_blk,virtio_blk_id\x12}\n\x0f\x44\x65leteVirtioBlk\x12*.opi_api.storage.v1.DeleteVirtioBlkRequest\x1a\x16.google.protobuf.Empty\"&\x82\xd3\xe4\x93\x02\x19*\x17/v1/{name=VirtioBlks/*}\xda\x41\x04name\x12\xab\x01\n\x0fUpdateVirtioBlk\x12*.opi_api.storage.v1.UpdateVirtioBlkRequest\x1a\x1d.opi_api.storage.v1.VirtioBlk\"M\x82\xd3\xe4\x93\x02.2 /v1/{virtio_blk.name=subsystems}:\nvirtio_blk\xda\x41\x16virtio_blk,update_mask\x12\x91\x01\n\x0eListVirtioBlks\x12).opi_api.storage.v1.ListVirtioBlksRequest\x1a*.opi_api.storage.v1.ListVirtioBlksResponse\"(\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/{parent=subsystems}\xda\x41\x06parent\x12~\n\x0cGetVirtioBlk\x12\'.opi_api.storage.v1.GetVirtioBlkRequest\x1a\x1d.opi_api.storage.v1.VirtioBlk\"&\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/{name=VirtioBlks/*}\xda\x41\x04name\x12\x95\x01\n\x0eStatsVirtioBlk\x12).opi_api.storage.v1.StatsVirtioBlkRequest\x1a*.opi_api.storage.v1.StatsVirtioBlkResponse\",\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/{name=VirtioBlks/*}:stats\xda\x41\x04nameBe\n\x12opi_api.storage.v1B\x16\x46rontendVirtioBlkProtoP\x01Z5github.com/opiproject/opi-api/storage/v1alpha1/gen/gob\x06proto3')



_VIRTIOBLK = DESCRIPTOR.message_types_by_name['VirtioBlk']
_CREATEVIRTIOBLKREQUEST = DESCRIPTOR.message_types_by_name['CreateVirtioBlkRequest']
_DELETEVIRTIOBLKREQUEST = DESCRIPTOR.message_types_by_name['DeleteVirtioBlkRequest']
_UPDATEVIRTIOBLKREQUEST = DESCRIPTOR.message_types_by_name['UpdateVirtioBlkRequest']
_LISTVIRTIOBLKSREQUEST = DESCRIPTOR.message_types_by_name['ListVirtioBlksRequest']
_LISTVIRTIOBLKSRESPONSE = DESCRIPTOR.message_types_by_name['ListVirtioBlksResponse']
_GETVIRTIOBLKREQUEST = DESCRIPTOR.message_types_by_name['GetVirtioBlkRequest']
_STATSVIRTIOBLKREQUEST = DESCRIPTOR.message_types_by_name['StatsVirtioBlkRequest']
_STATSVIRTIOBLKRESPONSE = DESCRIPTOR.message_types_by_name['StatsVirtioBlkResponse']
VirtioBlk = _reflection.GeneratedProtocolMessageType('VirtioBlk', (_message.Message,), {
  'DESCRIPTOR' : _VIRTIOBLK,
  '__module__' : 'frontend_virtio_blk_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.VirtioBlk)
  })
_sym_db.RegisterMessage(VirtioBlk)

CreateVirtioBlkRequest = _reflection.GeneratedProtocolMessageType('CreateVirtioBlkRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVIRTIOBLKREQUEST,
  '__module__' : 'frontend_virtio_blk_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.CreateVirtioBlkRequest)
  })
_sym_db.RegisterMessage(CreateVirtioBlkRequest)

DeleteVirtioBlkRequest = _reflection.GeneratedProtocolMessageType('DeleteVirtioBlkRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEVIRTIOBLKREQUEST,
  '__module__' : 'frontend_virtio_blk_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.DeleteVirtioBlkRequest)
  })
_sym_db.RegisterMessage(DeleteVirtioBlkRequest)

UpdateVirtioBlkRequest = _reflection.GeneratedProtocolMessageType('UpdateVirtioBlkRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVIRTIOBLKREQUEST,
  '__module__' : 'frontend_virtio_blk_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.UpdateVirtioBlkRequest)
  })
_sym_db.RegisterMessage(UpdateVirtioBlkRequest)

ListVirtioBlksRequest = _reflection.GeneratedProtocolMessageType('ListVirtioBlksRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVIRTIOBLKSREQUEST,
  '__module__' : 'frontend_virtio_blk_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.ListVirtioBlksRequest)
  })
_sym_db.RegisterMessage(ListVirtioBlksRequest)

ListVirtioBlksResponse = _reflection.GeneratedProtocolMessageType('ListVirtioBlksResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVIRTIOBLKSRESPONSE,
  '__module__' : 'frontend_virtio_blk_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.ListVirtioBlksResponse)
  })
_sym_db.RegisterMessage(ListVirtioBlksResponse)

GetVirtioBlkRequest = _reflection.GeneratedProtocolMessageType('GetVirtioBlkRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVIRTIOBLKREQUEST,
  '__module__' : 'frontend_virtio_blk_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.GetVirtioBlkRequest)
  })
_sym_db.RegisterMessage(GetVirtioBlkRequest)

StatsVirtioBlkRequest = _reflection.GeneratedProtocolMessageType('StatsVirtioBlkRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATSVIRTIOBLKREQUEST,
  '__module__' : 'frontend_virtio_blk_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.StatsVirtioBlkRequest)
  })
_sym_db.RegisterMessage(StatsVirtioBlkRequest)

StatsVirtioBlkResponse = _reflection.GeneratedProtocolMessageType('StatsVirtioBlkResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATSVIRTIOBLKRESPONSE,
  '__module__' : 'frontend_virtio_blk_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.StatsVirtioBlkResponse)
  })
_sym_db.RegisterMessage(StatsVirtioBlkResponse)

_FRONTENDVIRTIOBLKSERVICE = DESCRIPTOR.services_by_name['FrontendVirtioBlkService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022opi_api.storage.v1B\026FrontendVirtioBlkProtoP\001Z5github.com/opiproject/opi-api/storage/v1alpha1/gen/go'
  _VIRTIOBLK.fields_by_name['name']._options = None
  _VIRTIOBLK.fields_by_name['name']._serialized_options = b'\340A\003\340A\005\372A\036\n\034opi_api.storage.v1/VirtioBlk'
  _VIRTIOBLK.fields_by_name['volume_name_ref']._options = None
  _VIRTIOBLK.fields_by_name['volume_name_ref']._serialized_options = b'\340A\002'
  _VIRTIOBLK._options = None
  _VIRTIOBLK._serialized_options = b'\352A4\n storage.opiproject.org/VirtioBlk\022\020volumes/{volume}'
  _CREATEVIRTIOBLKREQUEST.fields_by_name['virtio_blk']._options = None
  _CREATEVIRTIOBLKREQUEST.fields_by_name['virtio_blk']._serialized_options = b'\340A\002'
  _DELETEVIRTIOBLKREQUEST.fields_by_name['name']._options = None
  _DELETEVIRTIOBLKREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\036\n\034opi_api.storage.v1/VirtioBlk'
  _LISTVIRTIOBLKSREQUEST.fields_by_name['parent']._options = None
  _LISTVIRTIOBLKSREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A\036\n\034opi_api.storage.v1/VirtioBlk'
  _GETVIRTIOBLKREQUEST.fields_by_name['name']._options = None
  _GETVIRTIOBLKREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\036\n\034opi_api.storage.v1/VirtioBlk'
  _STATSVIRTIOBLKREQUEST.fields_by_name['name']._options = None
  _STATSVIRTIOBLKREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\036\n\034opi_api.storage.v1/VirtioBlk'
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['CreateVirtioBlk']._options = None
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['CreateVirtioBlk']._serialized_options = b'\202\323\344\223\002\031\"\013/v1/volumes:\nvirtio_blk\332A\030virtio_blk,virtio_blk_id'
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['DeleteVirtioBlk']._options = None
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['DeleteVirtioBlk']._serialized_options = b'\202\323\344\223\002\031*\027/v1/{name=VirtioBlks/*}\332A\004name'
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['UpdateVirtioBlk']._options = None
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['UpdateVirtioBlk']._serialized_options = b'\202\323\344\223\002.2 /v1/{virtio_blk.name=subsystems}:\nvirtio_blk\332A\026virtio_blk,update_mask'
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['ListVirtioBlks']._options = None
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['ListVirtioBlks']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/{parent=subsystems}\332A\006parent'
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['GetVirtioBlk']._options = None
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['GetVirtioBlk']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/{name=VirtioBlks/*}\332A\004name'
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['StatsVirtioBlk']._options = None
  _FRONTENDVIRTIOBLKSERVICE.methods_by_name['StatsVirtioBlk']._serialized_options = b'\202\323\344\223\002\037\022\035/v1/{name=VirtioBlks/*}:stats\332A\004name'
  _VIRTIOBLK._serialized_start=245
  _VIRTIOBLK._serialized_end=566
  _CREATEVIRTIOBLKREQUEST._serialized_start=568
  _CREATEVIRTIOBLKREQUEST._serialized_end=671
  _DELETEVIRTIOBLKREQUEST._serialized_start=673
  _DELETEVIRTIOBLKREQUEST._serialized_end=772
  _UPDATEVIRTIOBLKREQUEST._serialized_start=775
  _UPDATEVIRTIOBLKREQUEST._serialized_end=922
  _LISTVIRTIOBLKSREQUEST._serialized_start=924
  _LISTVIRTIOBLKSREQUEST._serialized_end=1040
  _LISTVIRTIOBLKSRESPONSE._serialized_start=1042
  _LISTVIRTIOBLKSRESPONSE._serialized_end=1143
  _GETVIRTIOBLKREQUEST._serialized_start=1145
  _GETVIRTIOBLKREQUEST._serialized_end=1218
  _STATSVIRTIOBLKREQUEST._serialized_start=1220
  _STATSVIRTIOBLKREQUEST._serialized_end=1295
  _STATSVIRTIOBLKRESPONSE._serialized_start=1297
  _STATSVIRTIOBLKRESPONSE._serialized_end=1369
  _FRONTENDVIRTIOBLKSERVICE._serialized_start=1372
  _FRONTENDVIRTIOBLKSERVICE._serialized_end=2282
# @@protoc_insertion_point(module_scope)
