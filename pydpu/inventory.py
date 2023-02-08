# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.v1 import inventory_pb2, inventory_pb2_grpc


def get_inventory():
    print(
        "tbd",
        grpc.StatusCode.UNIMPLEMENTED,
        inventory_pb2.InventoryGetRequest(),
        inventory_pb2_grpc.InventorySvcStub(),
    )
