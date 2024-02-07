# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.v1 import inventory_pb2, inventory_pb2_grpc


def get_inventory(address):
    try:
        with grpc.insecure_channel(address) as channel:
            stub = inventory_pb2_grpc.InventoryServiceStub(channel)
            res = stub.GetInventory(request=inventory_pb2.GetInventoryRequest())
            return res
    except grpc.RpcError as e:
        print(e)
