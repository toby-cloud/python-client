
class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ConnectionError(Error):
    """Exception raised for errors relating network connection.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class CallbackError(Error):
    """Exception raised for errors relating to callbacks.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
