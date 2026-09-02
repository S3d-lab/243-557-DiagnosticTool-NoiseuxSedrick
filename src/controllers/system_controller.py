from enum import Enum, auto

class SystemState(Enum):
    STOPPED = auto()
    RUNNING = auto()
    ALARM = auto()


class SystemController:

    def __init__(self) -> None:
        self.state = SystemState.STOPPED

    def start(self) -> None:
        if self.state == SystemState.STOPPED:
            self.state = SystemState.RUNNING

    def stop(self) -> None:
        if self.state == SystemState.RUNNING:
            self.state = SystemState.STOPPED

    def reset(self) -> None:
        if self.state == SystemState.ALARM:
            self.state = SystemState.STOPPED

    def check_alarm(self, sensor_value: float) -> None:
        if self.state == SystemState.RUNNING and sensor_value > 80:
            self.state = SystemState.ALARM

    def read_state(self) -> str:
        return str(self.state)