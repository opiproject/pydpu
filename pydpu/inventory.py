# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.v1 import inventory_pb2


def get_inventory(address):
    print(
        "tbd",
        address,
        grpc.StatusCode.UNIMPLEMENTED,
        inventory_pb2.InventoryGetRequest(),
    )
