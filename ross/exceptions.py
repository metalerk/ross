class RossBaseException(Exception):
    pass


class RossHTTPNot200(BaseException):
    pass


class RossWriteFileException(RossBaseException):
    pass
