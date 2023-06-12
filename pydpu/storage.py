# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import uuid

import grpc
from google.protobuf import field_mask_pb2

from .proto.v1 import (
    frontend_nvme_pcie_pb2,
    frontend_nvme_pcie_pb2_grpc,
    object_key_pb2,
    opicommon_pb2,
    uuid_pb2,
)


class NvmeSubsystem:
    """An object representing Nvme subsystem.
    Args:
        nqn:    per Nvme spec each subsystem has an Nvme Qualified Name.
        model:  model number of the subsystem that will be visible to host.
        serial: serial number of the subsystem that will be visible to host.
        ns:     max amount of namespaces allowed in this subsystem.
    """

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self.id)}, nqn={str(self.nqn)})"

    def __init__(self, nqn: str, model="OPI Model", serial="OPI SN", ns=10) -> None:
        self.id = uuid.uuid1()
        self.nqn = nqn
        self.model = model
        self.serial = serial
        self.ns = ns

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNvmeSubsystem(
                request=frontend_nvme_pcie_pb2.CreateNvmeSubsystemRequest(
                    nvme_subsystem_id=str(self.id),
                    nvme_subsystem=frontend_nvme_pcie_pb2.NvmeSubsystem(
                        spec=frontend_nvme_pcie_pb2.NvmeSubsystemSpec(
                            model_number=self.model,
                            serial_number=self.serial,
                            max_namespaces=self.ns,
                            nqn=self.nqn,
                        )
                    ),
                )
            )
            return res

    def update(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNvmeSubsystem(
                request=frontend_nvme_pcie_pb2.UpdateNvmeSubsystemRequest(
                    update_mask=field_mask_pb2.FieldMask(paths=["*"]),
                    nvme_subsystem=frontend_nvme_pcie_pb2.NvmeSubsystem(
                        spec=frontend_nvme_pcie_pb2.NvmeSubsystemSpec(
                            model_number=self.model,
                            serial_number=self.serial,
                            max_namespaces=self.ns,
                            nqn=self.nqn,
                        )
                    ),
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.ListNvmeSubsystems(
                request=frontend_nvme_pcie_pb2.ListNvmeSubsystemsRequest()
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNvmeSubsystem(
                request=frontend_nvme_pcie_pb2.DeleteNvmeSubsystemRequest(
                    name=str(self.id),
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNvmeSubsystem(
                request=frontend_nvme_pcie_pb2.GetNvmeSubsystemRequest(
                    name=str(self.id),
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.NvmeSubsystemStats(
                request=frontend_nvme_pcie_pb2.NvmeSubsystemStatsRequest(
                    subsystem_id=object_key_pb2.ObjectKey(value=str(self.id))
                )
            )
            return res


class NvmeController:
    """An object representing Nvme controller.
    Args:
        subsystem: substsem name that controller belongs to.
        queue:     queue depth for both SQ (submition) and CQ (completion).
    """

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self.id)}, nqn={str(self.queue)})"

    def __init__(self, subsystem: NvmeSubsystem, queue: int) -> None:
        self.id = uuid.uuid1()
        self.subsystem = subsystem
        self.queue = queue

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNvmeController(
                request=frontend_nvme_pcie_pb2.CreateNvmeControllerRequest(
                    nvme_controller_id=str(self.id),
                    nvme_controller=frontend_nvme_pcie_pb2.NvmeController(
                        spec=frontend_nvme_pcie_pb2.NvmeControllerSpec(
                            subsystem_id=object_key_pb2.ObjectKey(
                                value=str(self.subsystem.id)
                            ),
                            pcie_id=opicommon_pb2.PciEndpoint(
                                physical_function=1, virtual_function=2, port_id=3
                            ),
                            max_nsq=5,
                            max_ncq=6,
                            sqes=7,
                            cqes=8,
                            nvme_controller_id=1,
                        )
                    ),
                )
            )
            return res

    def update(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNvmeController(
                request=frontend_nvme_pcie_pb2.UpdateNvmeControllerRequest(
                    update_mask=field_mask_pb2.FieldMask(paths=["*"]),
                    nvme_controller=frontend_nvme_pcie_pb2.NvmeController(
                        spec=frontend_nvme_pcie_pb2.NvmeControllerSpec(
                            subsystem_id=object_key_pb2.ObjectKey(
                                value=str(self.subsystem.id)
                            ),
                            pcie_id=opicommon_pb2.PciEndpoint(
                                physical_function=1, virtual_function=2, port_id=3
                            ),
                            max_nsq=5,
                            max_ncq=6,
                            sqes=7,
                            cqes=8,
                            nvme_controller_id=1,
                        )
                    ),
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.ListNvmeControllers(
                request=frontend_nvme_pcie_pb2.ListNvmeControllersRequest(
                    parent=str(self.subsystem.id)
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNvmeController(
                request=frontend_nvme_pcie_pb2.DeleteNvmeControllerRequest(
                    name=str(self.id),
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNvmeController(
                request=frontend_nvme_pcie_pb2.GetNvmeControllerRequest(
                    name=str(self.id),
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.NvmeControllerStats(
                request=frontend_nvme_pcie_pb2.NvmeControllerStatsRequest(
                    id=object_key_pb2.ObjectKey(value=str(self.id))
                )
            )
            return res


class NvmeNamespace:
    """An object representing Nvme namespace.
    Args:
        subsystem: subsystem name that controller belongs to.
        volume:    backend volume to connect the namespace to.
    """

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self.id)}, volume={str(self.volume)})"

    def __init__(self, subsystem: NvmeSubsystem, volume: str) -> None:
        self.id = uuid.uuid1()
        self.subsystem = subsystem
        self.volume = volume

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNvmeNamespace(
                request=frontend_nvme_pcie_pb2.CreateNvmeNamespaceRequest(
                    nvme_namespace_id=str(self.id),
                    nvme_namespace=frontend_nvme_pcie_pb2.NvmeNamespace(
                        spec=frontend_nvme_pcie_pb2.NvmeNamespaceSpec(
                            subsystem_id=object_key_pb2.ObjectKey(
                                value=str(self.subsystem.id)
                            ),
                            volume_id=object_key_pb2.ObjectKey(value=self.volume),
                            uuid=uuid_pb2.Uuid(
                                value="1b4e28ba-2fa1-11d2-883f-b9a761bde3fb"
                            ),
                            nguid="1b4e28ba-2fa1-11d2-883f-b9a761bde3fb",
                            eui64=1967554867335598546,
                            host_nsid=1,
                        )
                    ),
                )
            )
            return res

    def update(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNvmeNamespace(
                request=frontend_nvme_pcie_pb2.UpdateNvmeNamespaceRequest(
                    update_mask=field_mask_pb2.FieldMask(paths=["*"]),
                    nvme_namespace=frontend_nvme_pcie_pb2.NvmeNamespace(
                        spec=frontend_nvme_pcie_pb2.NvmeNamespaceSpec(
                            subsystem_id=object_key_pb2.ObjectKey(
                                value=str(self.subsystem.id)
                            ),
                            volume_id=object_key_pb2.ObjectKey(value="Malloc1"),
                            uuid=uuid_pb2.Uuid(
                                value="1b4e28ba-2fa1-11d2-883f-b9a761bde3fb"
                            ),
                            nguid="1b4e28ba-2fa1-11d2-883f-b9a761bde3fb",
                            eui64=1967554867335598546,
                            host_nsid=1,
                        )
                    ),
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.ListNvmeNamespaces(
                request=frontend_nvme_pcie_pb2.ListNvmeNamespacesRequest(
                    parent=str(self.subsystem.id)
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNvmeNamespace(
                request=frontend_nvme_pcie_pb2.DeleteNvmeNamespaceRequest(
                    name=str(self.id),
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNvmeNamespace(
                request=frontend_nvme_pcie_pb2.GetNvmeNamespaceRequest(
                    name=str(self.id),
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.NvmeNamespaceStats(
                request=frontend_nvme_pcie_pb2.NvmeNamespaceStatsRequest(
                    namespace_id=object_key_pb2.ObjectKey(value=str(self.id))
                )
            )
            return res
