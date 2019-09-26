"""Common exception classes, abstracted from specific contexts."""


class InvalidOperation(Exception):
    pass


class InvalidArgument(ValueError):
    pass


class EmptyArgumentException(InvalidArgument):
    
    def __init__(self, param_name: str):
        super().__init__(f"Parameter cannot be null or empty: `{param_name}`")


class AcceptedException(Exception):
    """Exception risen when an operation cannot be fully completed, but doesn't imply failure."""


class ObjectNotFound(Exception):
    """Exception risen when an object that is necessary to complete an operation is not found."""

    def __init__(self, message='Object not found'):
        super().__init__(message)


class ForbiddenException(Exception):
    pass


class UnauthorizedException(Exception):
    pass


class NotImplementedException(Exception):
    pass


class OperationFailedException(Exception):
    pass


class SystemException(Exception):
    pass
