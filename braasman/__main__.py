import sys
from PyQt6.QtWidgets import QApplication, QLabel

def main() -> None:
    app = QApplication(sys.argv)
    lbl = QLabel("BraaSMAN stub running on PyQt6")
    lbl.resize(300, 60)
    lbl.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
