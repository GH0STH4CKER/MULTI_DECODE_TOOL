from PyQt5.QtCore import QEvent,QPoint
from PyQt5 import QtWidgets as qt
from PyQt5 import QtGui as gui
from PyQt5 import QtCore
from MULTI_DECODER_GUI_UI import Ui_Dialog as ui
import codext

class Window(qt.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()

        self.ui = ui()
        self.ui.setupUi(self) # Initalize UI

        self.ui.btnENC.clicked.connect(self.encodeText)
        self.ui.btnDEC.clicked.connect(self.decodeText)
        self.ui.btnCLEAR.clicked.connect(self.clearText)
        self.ui.btnCOPY.clicked.connect(self.copy_To_Clipboard)
        
    def encodeText(self):
        try:
            result = codext.encode(self.ui.txtIN.text(),encoding=self.ui.ENC_METHOD.currentText())
        except Exception as e:
            msg1 = qt.QMessageBox()
            msg1.setIcon(qt.QMessageBox.Warning)
            msg1.setText(str(e))
            msg1.setWindowTitle("Error")
            msg1.setStandardButtons(qt.QMessageBox.Ok)
            msg1.exec_()
        else:
            self.ui.txtOut.setText(result)

    def decodeText(self):
        try:
            result = codext.decode(self.ui.txtIN.text(),encoding=self.ui.ENC_METHOD.currentText())
        except Exception as e:
            msg1 = qt.QMessageBox()
            msg1.setIcon(qt.QMessageBox.Warning)
            msg1.setText(str(e))
            msg1.setWindowTitle("Error")
            msg1.setStandardButtons(qt.QMessageBox.Ok)
            msg1.exec_()

        else:
            self.ui.txtOut.setText(result)

    def clearText(self):
        self.ui.txtIN.setText('')
        self.ui.txtOut.setText('')

    def copy_To_Clipboard(self):
        import clipboard
        copytext = self.ui.txtOut.text()
        if len(copytext) > 0 :
            clipboard.copy(copytext)
        

# Run Application
app = qt.QApplication([])
application = Window()
application.show()
app.exec()