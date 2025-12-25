from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class LogLevel(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

class LogComponent(str, Enum):
    UserAuth = "UserAuth"
    GeoIP = "GeoIP"
    Payment = "Payment"

class Log(BaseModel):
    id: str
    timestamp: datetime
    level: LogLevel
    component: LogComponent
    message: str

class LogStats(BaseModel):
    total_logs: int
    log_count_per_level: dict[LogLevel, int]
    log_count_per_component: dict[LogComponent, int]
