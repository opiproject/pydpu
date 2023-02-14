# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

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
        name: unique name to identfy subsystem.
        nqn:  per NVMe spec each subsystem has an NVMe Qualified Name.
    """

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self.name)}, nqn={str(self.nqn)})"

    def __init__(self, name: str, nqn: str) -> None:
        self.name = name
        self.nqn = nqn

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNVMeSubsystem(
                request=frontend_nvme_pcie_pb2.CreateNVMeSubsystemRequest(
                    nv_me_subsystem=frontend_nvme_pcie_pb2.NVMeSubsystem(
                        spec=frontend_nvme_pcie_pb2.NVMeSubsystemSpec(
                            id=object_key_pb2.ObjectKey(value="opi-subsystem"),
                            model_number="OPI Model",
                            serial_number="OPI SN",
                            max_namespaces=10,
                            nqn="nqn.2022-09.io.spdk:opi1",
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
                            id=object_key_pb2.ObjectKey(value="opi-subsystem"),
                            model_number="OPI Model",
                            serial_number="OPI SN",
                            max_namespaces=10,
                            nqn="nqn.2022-09.io.spdk:opi1",
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
                    name="opi-subsystem",
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNVMeSubsystem(
                request=frontend_nvme_pcie_pb2.GetNVMeSubsystemRequest(
                    name="opi-subsystem",
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.NVMeSubsystemStats(
                request=frontend_nvme_pcie_pb2.NVMeSubsystemStatsRequest(
                    subsystem_id=object_key_pb2.ObjectKey(value="opi-subsystem")
                )
            )
            return res


class NvmeController:
    """An object representing NVMe subsystem.
    Args:
        name: unique name to identfy subsystem.
        nqn:  per NVMe spec each subsystem has an NVMe Qualified Name.
    """

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self.name)}, nqn={str(self.nqn)})"

    def __init__(self, name: str, nqn: str) -> None:
        self.name = name
        self.nqn = nqn

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNVMeController(
                request=frontend_nvme_pcie_pb2.CreateNVMeControllerRequest(
                    nv_me_controller=frontend_nvme_pcie_pb2.NVMeController(
                        spec=frontend_nvme_pcie_pb2.NVMeControllerSpec(
                            id=object_key_pb2.ObjectKey(value="opi-ctrl"),
                            subsystem_id=object_key_pb2.ObjectKey(
                                value="opi-subsystem"
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
                            id=object_key_pb2.ObjectKey(value="opi-ctrl"),
                            subsystem_id=object_key_pb2.ObjectKey(
                                value="opi-subsystem"
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
                    parent="opi-subsystem"
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNVMeController(
                request=frontend_nvme_pcie_pb2.DeleteNVMeControllerRequest(
                    name="opi-ctrl",
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNVMeController(
                request=frontend_nvme_pcie_pb2.GetNVMeControllerRequest(
                    name="opi-ctrl",
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.NVMeControllerStats(
                request=frontend_nvme_pcie_pb2.NVMeControllerStatsRequest(
                    id=object_key_pb2.ObjectKey(value="opi-ctrl")
                )
            )
            return res


class NvmeNamespace:
    """An object representing NVMe subsystem.
    Args:
        name: unique name to identfy subsystem.
        nqn:  per NVMe spec each subsystem has an NVMe Qualified Name.
    """

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self.name)}, nqn={str(self.nqn)})"

    def __init__(self, name: str, nqn: str) -> None:
        self.name = name
        self.nqn = nqn

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNVMeNamespace(
                request=frontend_nvme_pcie_pb2.CreateNVMeNamespaceRequest(
                    nv_me_namespace=frontend_nvme_pcie_pb2.NVMeNamespace(
                        spec=frontend_nvme_pcie_pb2.NVMeNamespaceSpec(
                            id=object_key_pb2.ObjectKey(value="opi-ns"),
                            subsystem_id=object_key_pb2.ObjectKey(
                                value="opi-subsystem"
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

    def update(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNVMeNamespace(
                request=frontend_nvme_pcie_pb2.UpdateNVMeNamespaceRequest(
                    nv_me_namespace=frontend_nvme_pcie_pb2.NVMeNamespace(
                        spec=frontend_nvme_pcie_pb2.NVMeNamespaceSpec(
                            id=object_key_pb2.ObjectKey(value="opi-ns"),
                            subsystem_id=object_key_pb2.ObjectKey(
                                value="opi-subsystem"
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
                    parent="opi-subsystem"
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNVMeNamespace(
                request=frontend_nvme_pcie_pb2.DeleteNVMeNamespaceRequest(
                    name="opi-ns",
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNVMeNamespace(
                request=frontend_nvme_pcie_pb2.GetNVMeNamespaceRequest(
                    name="opi-ns",
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.NVMeNamespaceStats(
                request=frontend_nvme_pcie_pb2.NVMeNamespaceStatsRequest(
                    namespace_id=object_key_pb2.ObjectKey(value="opi-ns")
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
        s = NvmeSubsystem(name="opi-subsystem", nqn="nqn.2022-09.io.spdk:opi1")
        res = s.create(address)
        print(res)
    except grpc.RpcError as e:
        print(e)


def create_nvme_controller(address):
    try:
        s = NvmeController(name="opi-ctrl", nqn="nqn.2022-09.io.spdk:opi1")
        res = s.create(address)
        print(res)
    except grpc.RpcError as e:
        print(e)


def create_nvme_namespace(address):
    try:
        s = NvmeNamespace(name="opi-ns", nqn="nqn.2022-09.io.spdk:opi1")
        res = s.create(address)
        print(res)
    except grpc.RpcError as e:
        print(e)
