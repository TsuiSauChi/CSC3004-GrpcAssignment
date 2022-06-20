# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tracking_pb2 as tracking__pb2


class TrackingServiceStub(object):
    """Procedure Needed
    1. Perform Individual Check-in
    2. Perform Individual Check-out
    3. Perform Group Check-in
    4. Perform Group Check-out
    5. Create Groups
    6. Add User to Groups
    7. Trigger Covid Cases 7.5 Send Notificiation to users
    8. List all SafeEntry locations
    9. Create report covid case
    10. Listing of Location
    11. Get Groups By User
    12. Get Lastest Location and Group (For checking-out)

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/SafeEntry.TrackingService/Login',
                request_serializer=tracking__pb2.User.SerializeToString,
                response_deserializer=tracking__pb2.Status.FromString,
                )
        self.CreateCheckInIndividual = channel.unary_unary(
                '/SafeEntry.TrackingService/CreateCheckInIndividual',
                request_serializer=tracking__pb2.CheckInIndividual.SerializeToString,
                response_deserializer=tracking__pb2.Status.FromString,
                )
        self.CreateCheckOutIndividual = channel.unary_unary(
                '/SafeEntry.TrackingService/CreateCheckOutIndividual',
                request_serializer=tracking__pb2.CheckInIndividual.SerializeToString,
                response_deserializer=tracking__pb2.Status.FromString,
                )
        self.CreateCheckInGroup = channel.unary_unary(
                '/SafeEntry.TrackingService/CreateCheckInGroup',
                request_serializer=tracking__pb2.CheckInGroup.SerializeToString,
                response_deserializer=tracking__pb2.Status.FromString,
                )
        self.CreateCheckOutGroup = channel.unary_unary(
                '/SafeEntry.TrackingService/CreateCheckOutGroup',
                request_serializer=tracking__pb2.CheckInGroup.SerializeToString,
                response_deserializer=tracking__pb2.Status.FromString,
                )
        self.CreateGroup = channel.unary_unary(
                '/SafeEntry.TrackingService/CreateGroup',
                request_serializer=tracking__pb2.Group.SerializeToString,
                response_deserializer=tracking__pb2.Status.FromString,
                )
        self.AddUserToGroup = channel.stream_unary(
                '/SafeEntry.TrackingService/AddUserToGroup',
                request_serializer=tracking__pb2.User.SerializeToString,
                response_deserializer=tracking__pb2.Status.FromString,
                )
        self.GetSafeEntry = channel.unary_stream(
                '/SafeEntry.TrackingService/GetSafeEntry',
                request_serializer=tracking__pb2.Empty.SerializeToString,
                response_deserializer=tracking__pb2.SafeEntry.FromString,
                )
        self.CreateReportCovidCase = channel.unary_unary(
                '/SafeEntry.TrackingService/CreateReportCovidCase',
                request_serializer=tracking__pb2.Case.SerializeToString,
                response_deserializer=tracking__pb2.Status.FromString,
                )
        self.GetAllLocations = channel.unary_stream(
                '/SafeEntry.TrackingService/GetAllLocations',
                request_serializer=tracking__pb2.Empty.SerializeToString,
                response_deserializer=tracking__pb2.Location.FromString,
                )
        self.GetGroupsByUser = channel.unary_stream(
                '/SafeEntry.TrackingService/GetGroupsByUser',
                request_serializer=tracking__pb2.Empty.SerializeToString,
                response_deserializer=tracking__pb2.Group.FromString,
                )
        self.GetUserRole = channel.unary_unary(
                '/SafeEntry.TrackingService/GetUserRole',
                request_serializer=tracking__pb2.Empty.SerializeToString,
                response_deserializer=tracking__pb2.Role.FromString,
                )


class TrackingServiceServicer(object):
    """Procedure Needed
    1. Perform Individual Check-in
    2. Perform Individual Check-out
    3. Perform Group Check-in
    4. Perform Group Check-out
    5. Create Groups
    6. Add User to Groups
    7. Trigger Covid Cases 7.5 Send Notificiation to users
    8. List all SafeEntry locations
    9. Create report covid case
    10. Listing of Location
    11. Get Groups By User
    12. Get Lastest Location and Group (For checking-out)

    """

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCheckInIndividual(self, request, context):
        """1
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCheckOutIndividual(self, request, context):
        """2; Need duplicate Here? 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCheckInGroup(self, request, context):
        """3; Need to come back here
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCheckOutGroup(self, request, context):
        """4. Need duplicate Here? 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateGroup(self, request, context):
        """5.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUserToGroup(self, request_iterator, context):
        """6. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSafeEntry(self, request, context):
        """7. (Come back here)

        8
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateReportCovidCase(self, request, context):
        """9. Self report covid case
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllLocations(self, request, context):
        """10. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGroupsByUser(self, request, context):
        """11.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserRole(self, request, context):
        """12. Check user roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrackingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=tracking__pb2.User.FromString,
                    response_serializer=tracking__pb2.Status.SerializeToString,
            ),
            'CreateCheckInIndividual': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCheckInIndividual,
                    request_deserializer=tracking__pb2.CheckInIndividual.FromString,
                    response_serializer=tracking__pb2.Status.SerializeToString,
            ),
            'CreateCheckOutIndividual': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCheckOutIndividual,
                    request_deserializer=tracking__pb2.CheckInIndividual.FromString,
                    response_serializer=tracking__pb2.Status.SerializeToString,
            ),
            'CreateCheckInGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCheckInGroup,
                    request_deserializer=tracking__pb2.CheckInGroup.FromString,
                    response_serializer=tracking__pb2.Status.SerializeToString,
            ),
            'CreateCheckOutGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCheckOutGroup,
                    request_deserializer=tracking__pb2.CheckInGroup.FromString,
                    response_serializer=tracking__pb2.Status.SerializeToString,
            ),
            'CreateGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGroup,
                    request_deserializer=tracking__pb2.Group.FromString,
                    response_serializer=tracking__pb2.Status.SerializeToString,
            ),
            'AddUserToGroup': grpc.stream_unary_rpc_method_handler(
                    servicer.AddUserToGroup,
                    request_deserializer=tracking__pb2.User.FromString,
                    response_serializer=tracking__pb2.Status.SerializeToString,
            ),
            'GetSafeEntry': grpc.unary_stream_rpc_method_handler(
                    servicer.GetSafeEntry,
                    request_deserializer=tracking__pb2.Empty.FromString,
                    response_serializer=tracking__pb2.SafeEntry.SerializeToString,
            ),
            'CreateReportCovidCase': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateReportCovidCase,
                    request_deserializer=tracking__pb2.Case.FromString,
                    response_serializer=tracking__pb2.Status.SerializeToString,
            ),
            'GetAllLocations': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAllLocations,
                    request_deserializer=tracking__pb2.Empty.FromString,
                    response_serializer=tracking__pb2.Location.SerializeToString,
            ),
            'GetGroupsByUser': grpc.unary_stream_rpc_method_handler(
                    servicer.GetGroupsByUser,
                    request_deserializer=tracking__pb2.Empty.FromString,
                    response_serializer=tracking__pb2.Group.SerializeToString,
            ),
            'GetUserRole': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserRole,
                    request_deserializer=tracking__pb2.Empty.FromString,
                    response_serializer=tracking__pb2.Role.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SafeEntry.TrackingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrackingService(object):
    """Procedure Needed
    1. Perform Individual Check-in
    2. Perform Individual Check-out
    3. Perform Group Check-in
    4. Perform Group Check-out
    5. Create Groups
    6. Add User to Groups
    7. Trigger Covid Cases 7.5 Send Notificiation to users
    8. List all SafeEntry locations
    9. Create report covid case
    10. Listing of Location
    11. Get Groups By User
    12. Get Lastest Location and Group (For checking-out)

    """

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.TrackingService/Login',
            tracking__pb2.User.SerializeToString,
            tracking__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCheckInIndividual(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.TrackingService/CreateCheckInIndividual',
            tracking__pb2.CheckInIndividual.SerializeToString,
            tracking__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCheckOutIndividual(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.TrackingService/CreateCheckOutIndividual',
            tracking__pb2.CheckInIndividual.SerializeToString,
            tracking__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCheckInGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.TrackingService/CreateCheckInGroup',
            tracking__pb2.CheckInGroup.SerializeToString,
            tracking__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCheckOutGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.TrackingService/CreateCheckOutGroup',
            tracking__pb2.CheckInGroup.SerializeToString,
            tracking__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.TrackingService/CreateGroup',
            tracking__pb2.Group.SerializeToString,
            tracking__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUserToGroup(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/SafeEntry.TrackingService/AddUserToGroup',
            tracking__pb2.User.SerializeToString,
            tracking__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSafeEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/SafeEntry.TrackingService/GetSafeEntry',
            tracking__pb2.Empty.SerializeToString,
            tracking__pb2.SafeEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateReportCovidCase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.TrackingService/CreateReportCovidCase',
            tracking__pb2.Case.SerializeToString,
            tracking__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/SafeEntry.TrackingService/GetAllLocations',
            tracking__pb2.Empty.SerializeToString,
            tracking__pb2.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGroupsByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/SafeEntry.TrackingService/GetGroupsByUser',
            tracking__pb2.Empty.SerializeToString,
            tracking__pb2.Group.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.TrackingService/GetUserRole',
            tracking__pb2.Empty.SerializeToString,
            tracking__pb2.Role.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
