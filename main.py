import os
import sys

from PyQt5.QtGui import QFont

# Get the absolute path of the current script file
script_path = os.path.abspath(__file__)

# Get the root directory by going up one level from the script directory
project_root = os.path.dirname(os.path.dirname(script_path))

sys.path.insert(0, project_root)
sys.path.insert(0, os.getcwd())  # Add the current directory as well

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QComboBox, QVBoxLayout, QWidget, QTextEdit, QLabel
from PyQt5.QtCore import Qt, QCoreApplication

from qt_material import apply_stylesheet
from settingsDialog import SettingsDialog

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Qt Material Theme Playground (Change theme in Runtime)')
        lbl = QLabel('Select Theme')
        materialCmbBox = QComboBox()
        materialCmbBox.addItems(
            ['dark_amber.xml',
             'dark_blue.xml',
             'dark_cyan.xml',
             'dark_lightgreen.xml',
             'dark_pink.xml',
             'dark_purple.xml',
             'dark_red.xml',
             'dark_teal.xml',
             'dark_yellow.xml',
             'light_amber.xml',
             'light_blue.xml',
             'light_cyan.xml',
             'light_cyan_500.xml',
             'light_lightgreen.xml',
             'light_pink.xml',
             'light_purple.xml',
             'light_red.xml',
             'light_teal.xml',
             'light_yellow.xml']
        )
        materialCmbBox.currentTextChanged.connect(self.apply_theme_in_runtime)
        materialCmbBox.setCurrentText('light_blue.xml')

        self.__middleWidget = QTextEdit()

        btn = QPushButton('Run')
        btn.clicked.connect(self.__run)

        lay = QVBoxLayout()
        lay.addWidget(lbl)
        lay.addWidget(materialCmbBox)
        lay.addWidget(self.__middleWidget)
        lay.addWidget(btn)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

    def __run(self):
        dialog = SettingsDialog()
        reply = dialog.exec()

    def apply_theme_in_runtime(self, value):
        extra = {
            # Button colors
            'danger': '#dc3545',
            'warning': '#ffc107',
            'success': '#17a2b8',

            # Font doesn't work
            'line_height': '12px',

            # Density Scale
            'density_scale': '0',
            'font_size': '1px'
        }

        apply_stylesheet(app, theme=value, extra=extra)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    QApplication.setFont(QFont('Arial', 12))
    w = MainWindow()
    w.show()
    sys.exit(app.exec())