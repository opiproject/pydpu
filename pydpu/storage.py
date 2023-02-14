# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import uuid

import grpc

from .proto.v1 import (
    frontend_nvme_pcie_pb2,
    frontend_nvme_pcie_pb2_grpc,
    object_key_pb2,
    opicommon_pb2,
    uuid_pb2,
)


class NvmeSubsystem:
    """An object representing NVMe subsystem.
    Args:
        nqn:    per NVMe spec each subsystem has an NVMe Qualified Name.
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
            res = stub.CreateNVMeSubsystem(
                request=frontend_nvme_pcie_pb2.CreateNVMeSubsystemRequest(
                    nv_me_subsystem=frontend_nvme_pcie_pb2.NVMeSubsystem(
                        spec=frontend_nvme_pcie_pb2.NVMeSubsystemSpec(
                            id=object_key_pb2.ObjectKey(value=str(self.id)),
                            model_number=self.model,
                            serial_number=self.serial,
                            max_namespaces=self.ns,
                            nqn=self.nqn,
                        )
                    )
                )
            )
            return res

    def update(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNVMeSubsystem(
                request=frontend_nvme_pcie_pb2.UpdateNVMeSubsystemRequest(
                    nv_me_subsystem=frontend_nvme_pcie_pb2.NVMeSubsystem(
                        spec=frontend_nvme_pcie_pb2.NVMeSubsystemSpec(
                            id=object_key_pb2.ObjectKey(value=str(self.id)),
                            model_number=self.model,
                            serial_number=self.serial,
                            max_namespaces=self.ns,
                            nqn=self.nqn,
                        )
                    )
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.ListNVMeSubsystems(
                request=frontend_nvme_pcie_pb2.ListNVMeSubsystemsRequest()
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNVMeSubsystem(
                request=frontend_nvme_pcie_pb2.DeleteNVMeSubsystemRequest(
                    name=str(self.id),
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNVMeSubsystem(
                request=frontend_nvme_pcie_pb2.GetNVMeSubsystemRequest(
                    name=str(self.id),
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.NVMeSubsystemStats(
                request=frontend_nvme_pcie_pb2.NVMeSubsystemStatsRequest(
                    subsystem_id=object_key_pb2.ObjectKey(value=str(self.id))
                )
            )
            return res


class NvmeController:
    """An object representing NVMe controller.
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
            res = stub.CreateNVMeController(
                request=frontend_nvme_pcie_pb2.CreateNVMeControllerRequest(
                    nv_me_controller=frontend_nvme_pcie_pb2.NVMeController(
                        spec=frontend_nvme_pcie_pb2.NVMeControllerSpec(
                            id=object_key_pb2.ObjectKey(value=str(self.id)),
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
                    )
                )
            )
            return res

    def update(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNvmeController(
                request=frontend_nvme_pcie_pb2.UpdateNvmeControllerRequest(
                    nv_me_controller=frontend_nvme_pcie_pb2.NVMeController(
                        spec=frontend_nvme_pcie_pb2.NVMeControllerSpec(
                            id=object_key_pb2.ObjectKey(value=str(self.id)),
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
                    )
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.ListNVMeControllers(
                request=frontend_nvme_pcie_pb2.ListNVMeControllersRequest(
                    parent=str(self.subsystem.id)
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNVMeController(
                request=frontend_nvme_pcie_pb2.DeleteNVMeControllerRequest(
                    name=str(self.id),
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNVMeController(
                request=frontend_nvme_pcie_pb2.GetNVMeControllerRequest(
                    name=str(self.id),
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.NVMeControllerStats(
                request=frontend_nvme_pcie_pb2.NVMeControllerStatsRequest(
                    id=object_key_pb2.ObjectKey(value=str(self.id))
                )
            )
            return res


class NvmeNamespace:
    """An object representing NVMe namespace.
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
            res = stub.CreateNVMeNamespace(
                request=frontend_nvme_pcie_pb2.CreateNVMeNamespaceRequest(
                    nv_me_namespace=frontend_nvme_pcie_pb2.NVMeNamespace(
                        spec=frontend_nvme_pcie_pb2.NVMeNamespaceSpec(
                            id=object_key_pb2.ObjectKey(value=str(self.id)),
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
                    )
                )
            )
            return res

    def update(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNVMeNamespace(
                request=frontend_nvme_pcie_pb2.UpdateNVMeNamespaceRequest(
                    nv_me_namespace=frontend_nvme_pcie_pb2.NVMeNamespace(
                        spec=frontend_nvme_pcie_pb2.NVMeNamespaceSpec(
                            id=object_key_pb2.ObjectKey(value=str(self.id)),
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
                    )
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.ListNVMeNamespaces(
                request=frontend_nvme_pcie_pb2.ListNVMeNamespacesRequest(
                    parent=str(self.subsystem.id)
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNVMeNamespace(
                request=frontend_nvme_pcie_pb2.DeleteNVMeNamespaceRequest(
                    name=str(self.id),
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNVMeNamespace(
                request=frontend_nvme_pcie_pb2.GetNVMeNamespaceRequest(
                    name=str(self.id),
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.NVMeNamespaceStats(
                request=frontend_nvme_pcie_pb2.NVMeNamespaceStatsRequest(
                    namespace_id=object_key_pb2.ObjectKey(value=str(self.id))
                )
            )
            return res


def list_nvme_subsystems(address):
    print(
        "tbd",
        address,
        grpc.StatusCode.UNIMPLEMENTED,
        frontend_nvme_pcie_pb2.ListNVMeSubsystemsRequest(),
    )


def create_nvme_subsystem(address):
    try:
        s = NvmeSubsystem(
            nqn="nqn.2022-09.io.spdk:opi1", model="OPI Model", serial="OPI SN"
        )
        print(s)
        res = s.create(address)
        print(res)
    except grpc.RpcError as e:
        print(e)


def create_nvme_controller(address):
    try:
        s = NvmeSubsystem(
            nqn="nqn.2022-09.io.spdk:opi1", model="OPI Model", serial="OPI SN"
        )
        print(s)
        c = NvmeController(subsystem=s, queue=1024)
        print(c)
        res = c.create(address)
        print(res)
    except grpc.RpcError as e:
        print(e)


def create_nvme_namespace(address):
    try:
        s = NvmeSubsystem(
            nqn="nqn.2022-09.io.spdk:opi1", model="OPI Model", serial="OPI SN"
        )
        print(s)
        n = NvmeNamespace(subsystem=s, volume="Malloc1")
        print(n)
        res = n.create(address)
        print(res)
    except grpc.RpcError as e:
        print(e)
