import sys

from PySide6.QtWidgets import QApplication

from data.db import init_db
from login_window import LoginWindow

if __name__ == '__main__':
    init_db()

    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
