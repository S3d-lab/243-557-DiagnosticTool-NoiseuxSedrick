class Actuator:
    def __init__(
            self,
            name: str,
            state: bool = False,
    ) -> None:
        self.name = name
        self.state = state

    def read_state(self) -> bool:
         return self.state

    def change_state(self) -> None:
        self.state ^= True

    def state_true(self) -> None:
        self.state = True

    def state_false(self) -> None:
            self.state = False