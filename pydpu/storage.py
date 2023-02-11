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


def list_nvme_subsystems(address):
    print(
        "tbd",
        address,
        grpc.StatusCode.UNIMPLEMENTED,
        frontend_nvme_pcie_pb2.ListNVMeSubsystemsRequest(),
    )


def create_nvme_subsystem(address):
    channel = grpc.insecure_channel(address)
    stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
    try:
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
        print(res)
    except grpc.RpcError as e:
        print(e)


def create_nvme_controller(address):
    channel = grpc.insecure_channel(address)
    stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
    try:
        res = stub.CreateNVMeController(
            request=frontend_nvme_pcie_pb2.CreateNVMeControllerRequest(
                nv_me_controller=frontend_nvme_pcie_pb2.NVMeController(
                    spec=frontend_nvme_pcie_pb2.NVMeControllerSpec(
                        id=object_key_pb2.ObjectKey(value="opi-ctrl"),
                        subsystem_id=object_key_pb2.ObjectKey(value="opi-subsystem"),
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
        print(res)
    except grpc.RpcError as e:
        print(e)


def create_nvme_namespace(address):
    channel = grpc.insecure_channel(address)
    stub = frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(channel)
    try:
        res = stub.CreateNVMeNamespace(
            request=frontend_nvme_pcie_pb2.CreateNVMeNamespaceRequest(
                nv_me_namespace=frontend_nvme_pcie_pb2.NVMeNamespace(
                    spec=frontend_nvme_pcie_pb2.NVMeNamespaceSpec(
                        id=object_key_pb2.ObjectKey(value="opi-ns"),
                        subsystem_id=object_key_pb2.ObjectKey(value="opi-subsystem"),
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
        print(res)
    except grpc.RpcError as e:
        print(e)
