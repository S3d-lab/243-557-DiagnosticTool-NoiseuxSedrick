import sys
from pathlib import Path

# Conserve le lancement historique : python3 src/main.py.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from PyQt6.QtWidgets import QApplication
from src.views.main_window import MainWindow


def main() -> None:
    """Démarre l'application de diagnostic."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
