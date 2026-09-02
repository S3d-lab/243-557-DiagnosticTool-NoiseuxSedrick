from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QSlider,
    QGroupBox,
)

from models.sensor import Sensor
from models.actuator import Actuator


class MainWindow(QWidget):
    """Fenêtre principale du logiciel de diagnostic."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("243-557 — DiagnosticTool")
        self.resize(360, 220)

        self.sensor = Sensor("Distance", "cm", 35.0,)
        self.actuator = Actuator("LED")

        self.title_label = QLabel("Logiciel de diagnostic - Sedrick Noiseux")
        self.sensor_name_label = QLabel("Capteur : Distance")
        self.sensor_value_label = QLabel(f"Valeur : {self.sensor.read()}")
        self.read_button = QPushButton("Lire le capteur")

        sensor_layout = QVBoxLayout()
        sensor_layout.addWidget(self.title_label)
        sensor_layout.addWidget(self.sensor_name_label)
        sensor_layout.addWidget(self.sensor_value_label)
        sensor_layout.addWidget(self.read_button)

        self.read_button.clicked.connect(self.read_sensor)

        sensor_group = QGroupBox("Capteur")
        sensor_group.setLayout(sensor_layout)

        self.actuator_name_label = QLabel("Etat de la LED")
        self.actuator_state_label = QLabel(f"{self.actuator.read_state()}")
        self.actuator_state_set = QSlider(Qt.Orientation.Horizontal)
        self.actuator_state_set.setRange(0, 1)
        self.actuator_state_set.setValue(int(self.actuator.read_state()))
        self.actuator_toggle = QPushButton("Toggle")

        actuator_layout = QVBoxLayout()
        actuator_layout.addWidget(self.actuator_name_label)
        actuator_layout.addWidget(self.actuator_state_label)
        actuator_layout.addWidget(self.actuator_state_set)
        actuator_layout.addWidget(self.actuator_toggle)

        self.actuator_toggle.clicked.connect(self.toggle_actuator)
        self.actuator_state_set.valueChanged.connect(self.slider_changed)

        actuator_group = QGroupBox("Actionneur")
        actuator_group.setLayout(actuator_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(sensor_group)
        main_layout.addWidget(actuator_group)

        self.setLayout(main_layout)

    def read_sensor(self) -> None:
        """Simule la lecture d'un capteur de température."""
        value = self.sensor.read()

        self.sensor_value_label.setText(
            f"Valeur : {value} {self.sensor.unit}"
        )

    def toggle_actuator(self) -> None:
        self.actuator.change_state()
        self.actuator_state_set.setValue(int(self.actuator.read_state()))

    def slider_changed(self, value: int) -> None:
        if value == 1:
            self.actuator.state_true()
        else:
            self.actuator.state_false()

        self.actuator_state_label.setText(f"{self.actuator.read_state()}")