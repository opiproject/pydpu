# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import ipaddress
import uuid

import grpc
from google.protobuf import field_mask_pb2, wrappers_pb2

from .proto.v1 import (
    backend_nvme_pb2,
    backend_nvme_pb2_grpc,
    frontend_nvme_pb2,
    frontend_nvme_pb2_grpc,
    opicommon_pb2,
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
        self.id = "opi-" + str(uuid.uuid1())
        self.name = "nvmeSubsystems/" + str(self.id)
        self.nqn = nqn
        self.model = model
        self.serial = serial
        self.ns = ns

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNvmeSubsystem(
                request=frontend_nvme_pb2.CreateNvmeSubsystemRequest(
                    nvme_subsystem_id=str(self.id),
                    nvme_subsystem=frontend_nvme_pb2.NvmeSubsystem(
                        spec=frontend_nvme_pb2.NvmeSubsystemSpec(
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
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNvmeSubsystem(
                request=frontend_nvme_pb2.UpdateNvmeSubsystemRequest(
                    update_mask=field_mask_pb2.FieldMask(paths=["*"]),
                    nvme_subsystem=frontend_nvme_pb2.NvmeSubsystem(
                        name=self.name,
                        spec=frontend_nvme_pb2.NvmeSubsystemSpec(
                            model_number=self.model,
                            serial_number=self.serial,
                            max_namespaces=self.ns,
                            nqn=self.nqn,
                        ),
                    ),
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.ListNvmeSubsystems(
                request=frontend_nvme_pb2.ListNvmeSubsystemsRequest()
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNvmeSubsystem(
                request=frontend_nvme_pb2.DeleteNvmeSubsystemRequest(
                    name=self.name,
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNvmeSubsystem(
                request=frontend_nvme_pb2.GetNvmeSubsystemRequest(
                    name=self.name,
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.StatsNvmeSubsystem(
                request=frontend_nvme_pb2.StatsNvmeSubsystemRequest(
                    name=self.name,
                )
            )
            return res


class NvmeController:
    """An object representing Nvme controller.
    Args:
        subsystem: substsem name that controller belongs to.
        queue:     queue depth for both SQ (submition) and CQ (completion).
        pf:        physical_function of PciEndpoint.
        vf:        virtual_function of PciEndpoint.
        port:      port_id of PciEndpoint.
        max_nsq:   maximum number of host submission queues allowed.
                   For 0 the xPU will provide a default.
        max_ncq:   maximum number of host completion queues allowed.
                   For 0 the xPU will provide a default.
    """

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}({str(self.id)}, nqn={str(self.queue)}, "
            + f"port={str(self.port)}, pf={str(self.pf)}, vf={self.vf}, "
            + f"max_nsq={str(self.max_nsq)}, max_ncq={self.max_ncq})"
        )

    def __init__(
        self,
        subsystem: NvmeSubsystem,
        queue: int,
        pf: int,
        vf: int,
        port: int = 0,
        max_nsq: int = 0,
        max_ncq: int = 0,
    ) -> None:
        self.id = "opi-" + str(uuid.uuid1())
        self.name = "nvmeSubsystems/{}/nvmeControllers/{}".format(subsystem.id, self.id)
        self.subsystem = subsystem
        self.queue = queue
        self.pf = pf
        self.vf = vf
        self.port = port
        self.max_nsq = max_nsq
        self.max_ncq = max_ncq

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNvmeController(
                request=frontend_nvme_pb2.CreateNvmeControllerRequest(
                    parent=str(self.subsystem.name),
                    nvme_controller_id=str(self.id),
                    nvme_controller=frontend_nvme_pb2.NvmeController(
                        spec=frontend_nvme_pb2.NvmeControllerSpec(
                            trtype=opicommon_pb2.NVME_TRANSPORT_TYPE_PCIE,
                            pcie_id=opicommon_pb2.PciEndpoint(
                                physical_function=wrappers_pb2.Int32Value(
                                    value=self.pf
                                ),
                                virtual_function=wrappers_pb2.Int32Value(value=self.vf),
                                port_id=wrappers_pb2.Int32Value(value=self.port),
                            ),
                            max_nsq=self.max_nsq,
                            max_ncq=self.max_ncq,
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
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNvmeController(
                request=frontend_nvme_pb2.UpdateNvmeControllerRequest(
                    update_mask=field_mask_pb2.FieldMask(paths=["*"]),
                    nvme_controller=frontend_nvme_pb2.NvmeController(
                        name=self.name,
                        spec=frontend_nvme_pb2.NvmeControllerSpec(
                            pcie_id=opicommon_pb2.PciEndpoint(
                                physical_function=1, virtual_function=2, port_id=3
                            ),
                            max_nsq=5,
                            max_ncq=6,
                            sqes=7,
                            cqes=8,
                            nvme_controller_id=1,
                        ),
                    ),
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.ListNvmeControllers(
                request=frontend_nvme_pb2.ListNvmeControllersRequest(
                    parent=str(self.subsystem.name)
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNvmeController(
                request=frontend_nvme_pb2.DeleteNvmeControllerRequest(
                    name=self.name,
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNvmeController(
                request=frontend_nvme_pb2.GetNvmeControllerRequest(
                    name=self.name,
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.StatsNvmeController(
                request=frontend_nvme_pb2.StatsNvmeControllerRequest(
                    name=self.name,
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
        self.id = "opi-" + str(uuid.uuid1())
        self.name = "nvmeSubsystems/{}/nvmeNamespaces/{}".format(subsystem.id, self.id)
        self.subsystem = subsystem
        self.volume = volume

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNvmeNamespace(
                request=frontend_nvme_pb2.CreateNvmeNamespaceRequest(
                    parent=str(self.subsystem.name),
                    nvme_namespace_id=str(self.id),
                    nvme_namespace=frontend_nvme_pb2.NvmeNamespace(
                        spec=frontend_nvme_pb2.NvmeNamespaceSpec(
                            volume_name_ref=self.volume,
                            uuid="1b4e28ba-2fa1-11d2-883f-b9a761bde3fb",
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
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNvmeNamespace(
                request=frontend_nvme_pb2.UpdateNvmeNamespaceRequest(
                    update_mask=field_mask_pb2.FieldMask(paths=["*"]),
                    nvme_namespace=frontend_nvme_pb2.NvmeNamespace(
                        name=self.name,
                        spec=frontend_nvme_pb2.NvmeNamespaceSpec(
                            volume_name_ref="Malloc1",
                            uuid="1b4e28ba-2fa1-11d2-883f-b9a761bde3fb",
                            nguid="1b4e28ba-2fa1-11d2-883f-b9a761bde3fb",
                            eui64=1967554867335598546,
                            host_nsid=1,
                        ),
                    ),
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.ListNvmeNamespaces(
                request=frontend_nvme_pb2.ListNvmeNamespacesRequest(
                    parent=str(self.subsystem.name)
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNvmeNamespace(
                request=frontend_nvme_pb2.DeleteNvmeNamespaceRequest(
                    name=self.name,
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNvmeNamespace(
                request=frontend_nvme_pb2.GetNvmeNamespaceRequest(
                    name=self.name,
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.StatsNvmeNamespace(
                request=frontend_nvme_pb2.StatsNvmeNamespaceRequest(
                    name=self.name,
                )
            )
            return res


class NvmeRemoteController:
    """An object representing Nvme remote controller.
    Args:
        multipath:  multipath mode:
            backend_nvme_pb2.NVME_MULTIPATH_DISABLE,
            backend_nvme_pb2.NVME_MULTIPATH_FAILOVER,
            backend_nvme_pb2.NVME_MULTIPATH_MULTIPATH
        hdgst:      header digest
        ddgst:      data digest
    """

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}({str(self.id)}, "
            + f"multipath={str(self.multipath)}, hdgst={str(self.hdgst)}, "
            + f"ddgst={str(self.ddgst)})"
        )

    def __init__(self, multipath: int, hdgst: bool, ddgst: bool) -> None:
        self.id = "opi-" + str(uuid.uuid1())
        self.multipath = multipath
        self.hdgst = hdgst
        self.ddgst = ddgst
        self.name = "nvmeRemoteControllers/{}".format(self.id)

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.CreateNvmeRemoteController(
                request=backend_nvme_pb2.CreateNvmeRemoteControllerRequest(
                    nvme_remote_controller_id=self.id,
                    nvme_remote_controller=backend_nvme_pb2.NvmeRemoteController(
                        multipath=self.multipath,
                        tcp=backend_nvme_pb2.TcpController(
                            hdgst=self.hdgst,
                            ddgst=self.ddgst,
                        ),
                    ),
                )
            )
            return res

    def update(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.UpdateNvmeRemoteController(
                request=backend_nvme_pb2.UpdateNvmeRemoteControllerRequest(
                    update_mask=field_mask_pb2.FieldMask(paths=["*"]),
                    nvme_remote_controller=backend_nvme_pb2.NvmeRemoteController(
                        name=self.name,
                        multipath=self.multipath,
                        tcp=backend_nvme_pb2.TcpController(
                            hdgst=self.hdgst,
                            ddgst=self.ddgst,
                        ),
                    ),
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.ListNvmeRemoteControllers(
                request=backend_nvme_pb2.ListNvmeRemoteControllersRequest()
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.DeleteNvmeRemoteController(
                request=backend_nvme_pb2.DeleteNvmeRemoteControllerRequest(
                    name=self.name,
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.GetNvmeRemoteController(
                request=backend_nvme_pb2.GetNvmeRemoteControllerRequest(
                    name=self.name,
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.StatsNvmeRemoteController(
                request=backend_nvme_pb2.StatsNvmeRemoteControllerRequest(
                    name=self.name,
                )
            )
            return res


ip_to_grpc_version = {
    4: opicommon_pb2.NVME_ADDRESS_FAMILY_IPV4,
    6: opicommon_pb2.NVME_ADDRESS_FAMILY_IPV6,
}


class NvmeTcpPath:
    """An object representing Nvme TCP path.
    Args:
        ip:         ip address to target controller
        port:       port of target controller
        subnqn:     subsystem nqn
        hostnqn:    host nqn
    """

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}({str(self.id)}, ip={str(self.ip)}, "
            + f"adrfam={str(self.adrfam)}, port={str(self.port)}), "
            + f"subnqn={str(self.subnqn)}, hostnqn={str(self.hostnqn)}"
        )

    def __init__(
        self,
        remote_controller: NvmeRemoteController,
        ip: str,
        port: int,
        subnqn: str,
        hostnqn: str = "",
    ) -> None:
        self.id = "opi-" + str(uuid.uuid1())
        self.controller = remote_controller
        self.ip = ip
        self.port = port
        self.subnqn = subnqn
        self.hostnqn = hostnqn
        self.name = "nvmeRemoteControllers/{}/nvmePaths/{}".format(
            remote_controller.id, self.id
        )
        self.adrfam = ip_to_grpc_version[ipaddress.ip_address(self.ip).version]

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.CreateNvmePath(
                request=backend_nvme_pb2.CreateNvmePathRequest(
                    parent=self.controller.name,
                    nvme_path_id=self.id,
                    nvme_path=backend_nvme_pb2.NvmePath(
                        trtype=opicommon_pb2.NVME_TRANSPORT_TYPE_TCP,
                        traddr=self.ip,
                        fabrics=backend_nvme_pb2.FabricsPath(
                            trsvcid=self.port,
                            subnqn=self.subnqn,
                            adrfam=self.adrfam,
                            hostnqn=self.hostnqn,
                        ),
                    ),
                )
            )
            return res

    def update(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.UpdateNvmePath(
                request=backend_nvme_pb2.UpdateNvmePathRequest(
                    update_mask=field_mask_pb2.FieldMask(paths=["*"]),
                    nvme_path=backend_nvme_pb2.NvmePath(
                        name=self.name,
                        trtype=opicommon_pb2.NVME_TRANSPORT_TYPE_TCP,
                        traddr=self.ip,
                        fabrics=backend_nvme_pb2.FabricsPath(
                            trsvcid=self.port,
                            subnqn=self.subnqn,
                            adrfam=self.adrfam,
                            hostnqn=self.hostnqn,
                        ),
                    ),
                )
            )
            return res

    def list(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.ListNvmePaths(
                request=backend_nvme_pb2.ListNvmePathsRequest(
                    parent=self.controller.name
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.DeleteNvmePath(
                request=backend_nvme_pb2.DeleteNvmePathRequest(
                    name=self.name,
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.GetNvmePath(
                request=backend_nvme_pb2.GetNvmePathRequest(
                    name=self.name,
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(channel)
            res = stub.StatsNvmePath(
                request=backend_nvme_pb2.StatsNvmePathRequest(
                    name=self.name,
                )
            )
            return res
