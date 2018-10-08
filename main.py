import ui
import sys
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ui.Ui_Form()
    ui.show()
    sys.exit(app.exec_())
