# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import uuid

import grpc
from google.protobuf import field_mask_pb2, wrappers_pb2

from .proto.v1 import frontend_nvme_pb2, frontend_nvme_pb2_grpc, opicommon_pb2, uuid_pb2


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
        self.fullname = "//storage.opiproject.org/subsystems/" + str(self.id)
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
                        name=self.fullname,
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
                    name=self.fullname,
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNvmeSubsystem(
                request=frontend_nvme_pb2.GetNvmeSubsystemRequest(
                    name=self.fullname,
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.StatsNvmeSubsystem(
                request=frontend_nvme_pb2.StatsNvmeSubsystemRequest(
                    name=self.fullname,
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
        self.fullname = "//storage.opiproject.org/subsystems/{}/controllers{}".format(
            subsystem.id, self.id
        )
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
                    parent=str(self.subsystem.id),
                    nvme_controller_id=str(self.id),
                    nvme_controller=frontend_nvme_pb2.NvmeController(
                        spec=frontend_nvme_pb2.NvmeControllerSpec(
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
                        name=self.fullname,
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
                    parent=str(self.subsystem.id)
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNvmeController(
                request=frontend_nvme_pb2.DeleteNvmeControllerRequest(
                    name=self.fullname,
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNvmeController(
                request=frontend_nvme_pb2.GetNvmeControllerRequest(
                    name=self.fullname,
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.StatsNvmeController(
                request=frontend_nvme_pb2.StatsNvmeControllerRequest(
                    name=self.fullname,
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
        self.fullname = "//storage.opiproject.org/subsystems/{}/namespaces{}".format(
            subsystem.id, self.id
        )
        self.subsystem = subsystem
        self.volume = volume

    def create(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.CreateNvmeNamespace(
                request=frontend_nvme_pb2.CreateNvmeNamespaceRequest(
                    parent=str(self.subsystem.id),
                    nvme_namespace_id=str(self.id),
                    nvme_namespace=frontend_nvme_pb2.NvmeNamespace(
                        spec=frontend_nvme_pb2.NvmeNamespaceSpec(
                            volume_name_ref=self.volume,
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
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.UpdateNvmeNamespace(
                request=frontend_nvme_pb2.UpdateNvmeNamespaceRequest(
                    update_mask=field_mask_pb2.FieldMask(paths=["*"]),
                    nvme_namespace=frontend_nvme_pb2.NvmeNamespace(
                        name=self.fullname,
                        spec=frontend_nvme_pb2.NvmeNamespaceSpec(
                            volume_name_ref="Malloc1",
                            uuid=uuid_pb2.Uuid(
                                value="1b4e28ba-2fa1-11d2-883f-b9a761bde3fb"
                            ),
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
                    parent=str(self.subsystem.id)
                )
            )
            return res

    def delete(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.DeleteNvmeNamespace(
                request=frontend_nvme_pb2.DeleteNvmeNamespaceRequest(
                    name=self.fullname,
                )
            )
            return res

    def get(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.GetNvmeNamespace(
                request=frontend_nvme_pb2.GetNvmeNamespaceRequest(
                    name=self.fullname,
                )
            )
            return res

    def stats(self, address):
        with grpc.insecure_channel(address) as channel:
            stub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(channel)
            res = stub.StatsNvmeNamespace(
                request=frontend_nvme_pb2.StatsNvmeNamespaceRequest(
                    name=self.fullname,
                )
            )
            return res
