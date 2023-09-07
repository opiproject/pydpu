# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.v1 import (
    l2_xpu_infra_mgr_pb2,
    l2_xpu_infra_mgr_pb2_grpc,
    l3_xpu_infra_mgr_pb2,
    l3_xpu_infra_mgr_pb2_grpc,
)


def bridge_create(address):
    try:
        with grpc.insecure_channel(address) as channel:
            stub = l2_xpu_infra_mgr_pb2_grpc.LogicalBridgeServiceStub(channel)
            res = stub.CreateLogicalBridge(
                request=l2_xpu_infra_mgr_pb2.CreateLogicalBridgeRequest()
            )
            return res
    except grpc.RpcError as e:
        print(e)


def port_create(address):
    try:
        with grpc.insecure_channel(address) as channel:
            stub = l2_xpu_infra_mgr_pb2_grpc.BridgePortServiceStub(channel)
            res = stub.CreateBridgePort(
                request=l2_xpu_infra_mgr_pb2.CreateBridgePortRequest()
            )
            return res
    except grpc.RpcError as e:
        print(e)


def vrf_create(address):
    try:
        with grpc.insecure_channel(address) as channel:
            stub = l3_xpu_infra_mgr_pb2_grpc.VrfServiceStub(channel)
            res = stub.CreateVrf(request=l3_xpu_infra_mgr_pb2.CreateVrfRequest())
            return res
    except grpc.RpcError as e:
        print(e)


def svi_create(address):
    try:
        with grpc.insecure_channel(address) as channel:
            stub = l3_xpu_infra_mgr_pb2_grpc.SviServiceStub(channel)
            res = stub.CreateSvi(request=l3_xpu_infra_mgr_pb2.CreateSviRequest())
            return res
    except grpc.RpcError as e:
        print(e)
