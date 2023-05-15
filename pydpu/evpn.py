# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.v1 import (  # , interface_pb2, interface_pb2_grpc
    cloudrpc_pb2,
    cloudrpc_pb2_grpc,
)

# TODO: replace interface with evpn


def evpn_configure(address):
    try:
        with grpc.insecure_channel(address) as channel:
            stub = cloudrpc_pb2_grpc.CloudInfraServiceStub(channel)
            res = stub.CreateInterface(request=cloudrpc_pb2.CreateInterfaceRequest())
            return res
    except grpc.RpcError as e:
        print(e)
