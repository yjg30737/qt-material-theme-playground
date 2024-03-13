# qt-material-theme-playground
Qt material theme playground (changing theme during runtime)

## Requirements
* PyQt5
* qt-material

This will work in PyQt6, PySide6 as well.

## How to Run
1. git clone ~
2. pip install -r requirements.txt
3. python main.py

## Preview
### Changing theme during runtime

https://github.com/yjg30737/qt-material-theme-playground/assets/55078043/4f0d70fa-11bd-4e46-8d2b-c2012e16f01a

The creator of qt-material prefers to use QtStyleTools but i don't think it is good practice to use multiple inheritence.
Beside, changing theme in runtime is perfectly working without using that.

### If you press the run button dialog will pop up.

The theme is applied in the dialog as well.

![image](https://github.com/yjg30737/qt-material-theme-playground/assets/55078043/e5afe67d-5b66-474d-af76-1e2b3753ecdd)

### Note
font_size won't work for some reasons. So you have to set font by yourself like this:

```python
QApplication.setFont(QFont('Arial', 12))
```

If you want to switch font during runtime, you can refer to <a href="https://github.com/yjg30737/pyqt-font-dialog.git">pyqt-font-dialog</a>.
