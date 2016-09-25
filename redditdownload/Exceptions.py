class WrongFileTypeException(Exception):
    """Exception raised when incorrect content-type discovered"""


class FileExistsException(Exception):
    """Exception raised when file exists in specified directory"""
    def __init__(self, message):
        self.message = message


class URLDNEException(Exception):
    """Exception raised when URL does not exist"""


class WrongDataException(Exception):
    """Raised when data mismatches what's expected"""
    def __init__(self, data, message):
        self.data = data
        self.message = message
