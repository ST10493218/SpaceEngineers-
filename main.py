#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Space Engineers Build Planner")
    app.setApplicationVersion("1.0.0")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()