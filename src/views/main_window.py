from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QWidget

from src.hardware.simulation_hardware import SimulationHardware
from src.models.actuator import Actuator
from src.models.sensor import Sensor
from src.views.actuator_widget import ActuatorWidget
from src.views.sensor_widget import SensorWidget


class MainWindow(QWidget):
    """Crée les objets du système et assemble leurs composants graphiques."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("243-557 — DiagnosticTool")
        self.resize(800, 450)

        self.title_label = QLabel("Logiciel de diagnostic")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet(
            """
            font-size: 28px;
            font-weight: bold;
            """
        )

        # Les trois modèles utilisent exactement le même objet matériel.
        self.hardware = SimulationHardware()
        self.distance_sensor = Sensor("Distance", "cm", self.hardware)
        self.temperature_sensor = Sensor("Température", "°C", self.hardware)
        self.diagnostic_actuator = Actuator("DEL de diagnostic", self.hardware)

        self.distance_widget = SensorWidget(self.distance_sensor)
        self.temperature_widget = SensorWidget(self.temperature_sensor)
        self.actuator_widget = ActuatorWidget(self.diagnostic_actuator)

        components_layout = QHBoxLayout()
        components_layout.setSpacing(20)
        components_layout.addWidget(self.distance_widget, 1)
        components_layout.addWidget(self.temperature_widget, 1)
        components_layout.addWidget(self.actuator_widget, 1)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(components_layout)
        self.setLayout(main_layout)
