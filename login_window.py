from PySide6.QtWidgets import QMainWindow

from ui_py.ui_login_window import Ui_MainWindow


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.menu_window = None

        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.exit)

    def login(self):
        from menu_window import MenuWindow

        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.exit()

    def exit(self):
        self.close()
