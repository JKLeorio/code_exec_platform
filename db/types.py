from enum import Enum


class ExecuteResultStatus(str, Enum):
    ACCEPTED = "Accepted"
    ERROR = "Error"
    TIMEOUT = "Timeout"


class SubmitStatus(str, Enum):
    PASSED = "Passed"
    FAILED = "Failed"
