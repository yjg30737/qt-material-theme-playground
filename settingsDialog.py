
from PyQt5 import Qt
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QTabWidget, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QGroupBox, QSpinBox, QSizePolicy, QFormLayout
from PyQt5.QtWidgets import QWidget, QHBoxLayout


class HourMinSecGrpBox(QGroupBox):
    def __init__(self):
        super().__init__()
        self.__settings_struct = QSettings('timerSettings.ini', QSettings.IniFormat)
        self.__hour = int(self.__settings_struct.value('hour', 0))
        self.__min = int(self.__settings_struct.value('min', 0))
        self.__sec = int(self.__settings_struct.value('sec', 0))
        self.__initUi()

    def __initUi(self):
        self.__hourSpinBox = QSpinBox()
        self.__minSpinBox = QSpinBox()
        self.__secSpinBox = QSpinBox()

        self.__hourSpinBox.setValue(self.__hour)
        self.__minSpinBox.setValue(self.__min)
        self.__secSpinBox.setValue(self.__sec)

        self.__hourSpinBox.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.__minSpinBox.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.__secSpinBox.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        self.__minSpinBox.setRange(0, 59)
        self.__secSpinBox.setRange(0, 59)

        self.__hourSpinBox.valueChanged.connect(self.__hourChanged)
        self.__minSpinBox.valueChanged.connect(self.__minChanged)
        self.__secSpinBox.valueChanged.connect(self.__secChanged)

        lay = QFormLayout()
        lay.addRow('Hour', self.__hourSpinBox)
        lay.addRow('Minute', self.__minSpinBox)
        lay.addRow('Second', self.__secSpinBox)

        self.setLayout(lay)
        self.setTitle('H/M/S Settings')

    def __hourChanged(self):
        self.__hour = self.__hourSpinBox.value()

    def __minChanged(self):
        self.__min = self.__minSpinBox.value()

    def __secChanged(self):
        self.__sec = self.__secSpinBox.value()

    def get_hour(self):
        return self.__hour

    def get_min(self):
        return self.__min

    def get_sec(self):
        return self.__sec

class TimerSettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__settings_struct = QSettings('timerSettings.ini', QSettings.IniFormat)
        self.__initUi()

    def __initUi(self):
        self.__hourMinSecGrpBox = HourMinSecGrpBox()

        lay = QHBoxLayout()
        lay.addWidget(self.__hourMinSecGrpBox)
        self.setLayout(lay)

    def get_time(self):
        hour = self.__hourMinSecGrpBox.get_hour()
        min = self.__hourMinSecGrpBox.get_min()
        sec = self.__hourMinSecGrpBox.get_sec()
        self.__settings_struct.setValue('hour', hour)
        self.__settings_struct.setValue('min', min)
        self.__settings_struct.setValue('sec', sec)
        self.__settings_struct.sync()
        return hour, min, sec



class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Settings')
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)

        self.__timerSettingsWidget = TimerSettingsWidget()

        topWidget = QTabWidget()
        topWidget.addTab(self.__timerSettingsWidget, 'Timer')

        self.__okBtn = QPushButton()
        self.__okBtn.clicked.connect(self.accept)
        self.__okBtn.setText('OK')

        closeBtn = QPushButton()
        closeBtn.clicked.connect(self.close)
        closeBtn.setText('Cancel')

        lay = QHBoxLayout()
        lay.addWidget(self.__okBtn)
        lay.addWidget(closeBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        bottomWidget = QWidget()
        bottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(topWidget)
        lay.addWidget(bottomWidget)
        self.setLayout(lay)

    def __ok(self):
        self.accept()

    def get_time(self):
        return self.__timerSettingsWidget.get_time()