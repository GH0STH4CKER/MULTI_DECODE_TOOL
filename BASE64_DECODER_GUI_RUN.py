from PyQt5.QtCore import QEvent,QPoint
from PyQt5 import QtWidgets as qt
from PyQt5 import QtGui as gui
from PyQt5 import QtCore
from BASE64_DECODER_GUI_UI import Ui_Dialog as ui
from base64 import b64encode,b64decode

class Window(qt.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()

        self.ui = ui()
        self.ui.setupUi(self) # Initalize UI

        # Connect ButtonPress event to functions
        self.ui.btnENC.clicked.connect(self.base64_encode)
        self.ui.btnDEC.clicked.connect(self.base64_decode)
        self.ui.btnCLEAR.clicked.connect(self.clearfields)
        self.ui.btnCOPY.clicked.connect(self.copy_To_Clipboard)

    def base64_encode(self):
        varIN = self.ui.txtIN.text()
        try:
            self.ui.txtOut.setText(b64encode(bytes(varIN,'utf-8')).decode('utf-8'))
        except Exception as e:
            msg1 = qt.QMessageBox()
            msg1.setIcon(qt.QMessageBox.Warning)
            msg1.setText("Invalid input!")
            msg1.setWindowTitle("Error")
            msg1.setStandardButtons(qt.QMessageBox.Ok)
            msg1.exec_()

    def base64_decode(self):
        varIN = self.ui.txtIN.text() 
        try:
            self.ui.txtOut.setText(b64decode(bytes(varIN,'utf-8')).decode('utf-8'))
        except Exception as e:
            msg2 = qt.QMessageBox()
            msg2.setIcon(qt.QMessageBox.Warning)
            msg2.setText("Invalid base64 encoded string!")
            msg2.setWindowTitle("Error")
            msg2.setStandardButtons(qt.QMessageBox.Ok)
            msg2.exec_()

    def clearfields(self):
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