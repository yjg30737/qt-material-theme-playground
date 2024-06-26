import os
import sys

# Get the absolute path of the current script file
script_path = os.path.abspath(__file__)

# Get the root directory by going up one level from the script directory
project_root = os.path.dirname(os.path.dirname(script_path))

sys.path.insert(0, project_root)
sys.path.insert(0, os.getcwd())  # Add the current directory as well

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QComboBox, QVBoxLayout, QWidget, QTextEdit, QLabel, \
    QSlider, QSpinBox
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QFont, QIcon

from qt_material import apply_stylesheet
from settingsDialog import SettingsDialog
from script import DATA

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support

class CustomButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFlat(True)

    def setIcon(self, icon):
        super().setIcon(icon)
        self.setIconSize(icon.actualSize(QSize(24, 24)))

    def setIconSize(self, size):
        super().setIconSize(size)
        self.setFixedSize(size.width() + 10, size.height() + 10)

    def setFlat(self, b):
        pass

    def setStyleSheet(self, style):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Qt Material Theme Playground (Change theme in Runtime)')
        lbl = QLabel('Select Theme')
        materialCmbBox = QComboBox()
        materialCmbBox.addItems(
            DATA.keys()
        )
        materialCmbBox.currentTextChanged.connect(self.apply_theme_in_runtime)
        materialCmbBox.setCurrentText(materialCmbBox.itemText(0))

        self.__middleWidget = QTextEdit()

        btn = QPushButton('Run')
        btn.setIcon(QIcon('ico/setting.svg'))
        btn.clicked.connect(self.__run)

        inputLineEdit = QTextEdit('Hello')
        bushBtn = CustomButton('Martha')

        self.__densityScaleSlider = QSlider()
        self.__densityScaleSlider.setOrientation(Qt.Horizontal)
        self.__densityScaleSlider.setRange(-5, 5)
        self.__densityScaleSlider.setValue(0)
        self.__densityScaleSlider.valueChanged.connect(lambda: self.apply_theme_in_runtime(materialCmbBox.currentText()))

        self.__fontSizeSpinBox = QSpinBox()
        self.__fontSizeSpinBox.setRange(8, 16)
        self.__fontSizeSpinBox.setValue(12)
        self.__fontSizeSpinBox.valueChanged.connect(lambda: self.apply_theme_in_runtime(materialCmbBox.currentText()))

        lay = QVBoxLayout()
        lay.addWidget(lbl)
        lay.addWidget(materialCmbBox)
        lay.addWidget(self.__densityScaleSlider)
        lay.addWidget(self.__fontSizeSpinBox)
        lay.addWidget(self.__middleWidget)
        lay.addWidget(inputLineEdit)
        lay.addWidget(bushBtn)
        lay.addWidget(btn)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

        self.apply_theme_in_runtime(materialCmbBox.currentText())

    def __run(self):
        dialog = SettingsDialog()
        reply = dialog.exec()

    def apply_theme_in_runtime(self, value):
        extra = {
            # Button colors
            'danger': '#dc3545',
            'warning': '#ffc107',
            'success': '#17a2b8',

            'line_height': '12px',

            # Density Scale
            'density_scale': self.__densityScaleSlider.value(),
            'font_size': self.__fontSizeSpinBox.value()
        }

        v = DATA[value]

        apply_stylesheet(app, theme=v, extra=extra, invert_secondary=True, css_file='custom.css')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())