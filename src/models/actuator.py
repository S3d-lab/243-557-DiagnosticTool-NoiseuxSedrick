class Actuator:
    """Représente un actionneur pouvant être actif ou inactif."""

    def __init__(self, name: str, hardware) -> None:
        self.name = name
        self.hardware = hardware
        self.is_active = False

    def activate(self) -> None:
        """Active l'actionneur et transmet la commande au matériel."""
        self.is_active = True
        self.hardware.set_actuator(self.name, self.is_active)

    def deactivate(self) -> None:
        """Désactive l'actionneur et transmet la commande au matériel."""
        self.is_active = False
        self.hardware.set_actuator(self.name, self.is_active)

    def toggle(self) -> None:
        """Inverse l'état de l'actionneur."""
        if self.is_active:
            self.deactivate()
        else:
            self.activate()
