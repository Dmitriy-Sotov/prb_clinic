from PySide6.QtWidgets import QMainWindow

from ui_py.ui_menu_window import Ui_MenuWindow


class MenuWindow(QMainWindow, Ui_MenuWindow):
    def __init__(self):
        super().__init__()

        self.login_window = None

        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.pushButton.clicked.connect(self.back)

    def back(self):
        from login_window import LoginWindow

        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
