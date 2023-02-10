# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.v1 import frontend_nvme_pcie_pb2


def nvme_subsystems(address):
    print(
        "tbd",
        address,
        grpc.StatusCode.UNIMPLEMENTED,
        frontend_nvme_pcie_pb2.ListNVMeSubsystemsRequest(),
    )
