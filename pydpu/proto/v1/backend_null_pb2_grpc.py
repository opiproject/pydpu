# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import backend_null_pb2 as backend__null__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class NullDebugServiceStub(object):
    """Back End (network-facing) APIs. This is debug interface for null block devices.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateNullDebug = channel.unary_unary(
                '/opi_api.storage.v1.NullDebugService/CreateNullDebug',
                request_serializer=backend__null__pb2.CreateNullDebugRequest.SerializeToString,
                response_deserializer=backend__null__pb2.NullDebug.FromString,
                )
        self.DeleteNullDebug = channel.unary_unary(
                '/opi_api.storage.v1.NullDebugService/DeleteNullDebug',
                request_serializer=backend__null__pb2.DeleteNullDebugRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateNullDebug = channel.unary_unary(
                '/opi_api.storage.v1.NullDebugService/UpdateNullDebug',
                request_serializer=backend__null__pb2.UpdateNullDebugRequest.SerializeToString,
                response_deserializer=backend__null__pb2.NullDebug.FromString,
                )
        self.ListNullDebugs = channel.unary_unary(
                '/opi_api.storage.v1.NullDebugService/ListNullDebugs',
                request_serializer=backend__null__pb2.ListNullDebugsRequest.SerializeToString,
                response_deserializer=backend__null__pb2.ListNullDebugsResponse.FromString,
                )
        self.GetNullDebug = channel.unary_unary(
                '/opi_api.storage.v1.NullDebugService/GetNullDebug',
                request_serializer=backend__null__pb2.GetNullDebugRequest.SerializeToString,
                response_deserializer=backend__null__pb2.NullDebug.FromString,
                )
        self.NullDebugStats = channel.unary_unary(
                '/opi_api.storage.v1.NullDebugService/NullDebugStats',
                request_serializer=backend__null__pb2.NullDebugStatsRequest.SerializeToString,
                response_deserializer=backend__null__pb2.NullDebugStatsResponse.FromString,
                )


class NullDebugServiceServicer(object):
    """Back End (network-facing) APIs. This is debug interface for null block devices.
    """

    def CreateNullDebug(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNullDebug(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNullDebug(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNullDebugs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNullDebug(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NullDebugStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NullDebugServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateNullDebug': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNullDebug,
                    request_deserializer=backend__null__pb2.CreateNullDebugRequest.FromString,
                    response_serializer=backend__null__pb2.NullDebug.SerializeToString,
            ),
            'DeleteNullDebug': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNullDebug,
                    request_deserializer=backend__null__pb2.DeleteNullDebugRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateNullDebug': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNullDebug,
                    request_deserializer=backend__null__pb2.UpdateNullDebugRequest.FromString,
                    response_serializer=backend__null__pb2.NullDebug.SerializeToString,
            ),
            'ListNullDebugs': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNullDebugs,
                    request_deserializer=backend__null__pb2.ListNullDebugsRequest.FromString,
                    response_serializer=backend__null__pb2.ListNullDebugsResponse.SerializeToString,
            ),
            'GetNullDebug': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNullDebug,
                    request_deserializer=backend__null__pb2.GetNullDebugRequest.FromString,
                    response_serializer=backend__null__pb2.NullDebug.SerializeToString,
            ),
            'NullDebugStats': grpc.unary_unary_rpc_method_handler(
                    servicer.NullDebugStats,
                    request_deserializer=backend__null__pb2.NullDebugStatsRequest.FromString,
                    response_serializer=backend__null__pb2.NullDebugStatsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'opi_api.storage.v1.NullDebugService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NullDebugService(object):
    """Back End (network-facing) APIs. This is debug interface for null block devices.
    """

    @staticmethod
    def CreateNullDebug(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NullDebugService/CreateNullDebug',
            backend__null__pb2.CreateNullDebugRequest.SerializeToString,
            backend__null__pb2.NullDebug.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNullDebug(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NullDebugService/DeleteNullDebug',
            backend__null__pb2.DeleteNullDebugRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNullDebug(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NullDebugService/UpdateNullDebug',
            backend__null__pb2.UpdateNullDebugRequest.SerializeToString,
            backend__null__pb2.NullDebug.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNullDebugs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NullDebugService/ListNullDebugs',
            backend__null__pb2.ListNullDebugsRequest.SerializeToString,
            backend__null__pb2.ListNullDebugsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNullDebug(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NullDebugService/GetNullDebug',
            backend__null__pb2.GetNullDebugRequest.SerializeToString,
            backend__null__pb2.NullDebug.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NullDebugStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NullDebugService/NullDebugStats',
            backend__null__pb2.NullDebugStatsRequest.SerializeToString,
            backend__null__pb2.NullDebugStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
