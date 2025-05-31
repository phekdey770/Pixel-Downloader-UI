from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QPlainTextEdit, QGroupBox, QToolButton, QComboBox, QCheckBox, 
                             QVBoxLayout, QHBoxLayout, QFormLayout, QFrame, QProgressBar, QMessageBox, QDesktopWidget, QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import re
import requests
import subprocess

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 779, 547)
        self.setWindowTitle('Form')
        self.setStyleSheet('background-color: rgb(85, 170, 127);')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.center()
        
        self.btnLogs = QPushButton("O", self)
        self.btnLogs.setGeometry(630, 20, 21, 21)
        self.btnLogs.setFont(QFont("MS PGothic", 12))
        self.btnLogs.setCursor(Qt.PointingHandCursor)
        self.btnLogs.setStyleSheet("color: rgb(255, 255, 255); font: 12pt 'MS PGothic'; background-color: rgb(85, 170, 127);")
        self.btnLogs.clicked.connect(self.showLogs)

        self.btnInfo = QPushButton("?", self)
        self.btnInfo.setGeometry(670, 20, 21, 21)
        self.btnInfo.setFont(QFont("MS PGothic", 12))
        self.btnInfo.setCursor(Qt.PointingHandCursor)
        self.btnInfo.setStyleSheet("color: rgb(255, 255, 255); font: 12pt 'MS PGothic'; background-color: rgb(85, 170, 127);")
        self.btnInfo.clicked.connect(self.showInfo)
        
        # Minimize and Close Buttons
        self.btnMinimize = QPushButton('-', self)
        self.btnMinimize.setGeometry(710, 20, 21, 21)
        self.btnMinimize.setFont(QFont('MS PGothic', 12))
        self.btnMinimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMinimize.setStyleSheet('color: rgb(255, 255, 255); font: 12pt "MS PGothic"; background-color: rgb(85, 170, 127);')
        self.btnMinimize.clicked.connect(self.showMinimized)
        
        self.btnClose = QPushButton('X', self)
        self.btnClose.setGeometry(750, 20, 21, 21)
        self.btnClose.setFont(QFont('MS PGothic', 12))
        self.btnClose.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClose.setStyleSheet('color: rgb(255, 255, 255); font: 12pt "MS PGothic"; background-color: rgb(85, 170, 127);')
        self.btnClose.clicked.connect(self.confirmClose)
        
        # Title Label
        self.lbTitle = QLabel(self)
        self.lbTitle.setGeometry(10, 0, 451, 61)
        self.lbTitle.setStyleSheet('font: 18pt "Khmer OS Muol Light";')
        self.lbTitle.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600; color:#ffffff;">កម្មវិធីទាញយក</span><span style=" font-size:14pt; font-weight:600; color:#aa0000;"> PIXEL FOOTAGE VIDEO</span></p></body></html>')
        self.lbTitle.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        # Main GroupBox
        self.gbMain = QGroupBox(self)
        self.gbMain.setGeometry(10, 60, 761, 451)
        self.gbMain.setFont(QFont('', 10))
        self.gbMain.setStyleSheet('color: rgb(255, 255, 255);')
        
        # Link Videos Label
        self.lbLinkVideo = QLabel(self.gbMain)
        self.lbLinkVideo.setGeometry(10, 10, 181, 20)
        self.lbLinkVideo.setFont(QFont('', 7))
        self.lbLinkVideo.setText('<html><head/><body><p><span style=" font-size:9pt; font-weight:600; color:#550000;">Link Videos</span></p></body></html>')
        self.lbLinkVideo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        # Link Download TextEdit
        self.txtLinkDownload = QPlainTextEdit(self.gbMain)
        self.txtLinkDownload.setGeometry(10, 30, 741, 181)
        self.txtLinkDownload.setFont(QFont('Roboto', 10))
        self.txtLinkDownload.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);')
        self.txtLinkDownload.setPlaceholderText('Ex: https://www.pexels.com/video/a-person-typing-on-a-laptop-keyboard-4496268/')
        
        # Download GroupBox
        self.gbDownload = QGroupBox(' Option | Phekdey | V.1', self.gbMain)
        self.gbDownload.setGeometry(10, 220, 741, 221)
        self.gbDownload.setFont(QFont('', 8))
        self.gbDownload.setStyleSheet('color: rgb(255, 255, 255);')
        
        # Path Label
        self.lbPath = QLabel(self.gbDownload)
        self.lbPath.setGeometry(10, 70, 61, 31)
        self.lbPath.setText('<html><head/><body><p><span style=" font-weight:600; color:#ffffff;">Save Path</span></p></body></html>')
        self.lbPath.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        # Path Save TextEdit
        self.txtPathSave = QPlainTextEdit(self.gbDownload)
        self.txtPathSave.setGeometry(80, 71, 481, 71)
        self.txtPathSave.setFont(QFont('Roboto', 9))
        self.txtPathSave.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);')
        self.txtPathSave.textChanged.connect(self.check_path)
        
        # Browse Path Button
        self.btnBrowsePath = QToolButton(self.gbDownload)
        self.btnBrowsePath.setGeometry(10, 100, 61, 31)
        self.btnBrowsePath.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBrowsePath.setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);')
        self.btnBrowsePath.setText('...')
        self.btnBrowsePath.clicked.connect(self.browse_directory)
        
        # Option Line
        self.lineOption = QFrame(self.gbDownload)
        self.lineOption.setGeometry(80, 150, 651, 16)
        self.lineOption.setFrameShape(QFrame.HLine)
        self.lineOption.setFrameShadow(QFrame.Plain)
        
        # Download Button
        self.btnDownload = QToolButton(self.gbDownload)
        self.btnDownload.setGeometry(620, 173, 111, 31)
        self.btnDownload.setFont(QFont('', 11, QFont.Bold))
        self.btnDownload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDownload.setStyleSheet('color: rgb(0, 85, 0); background-color: rgb(255, 255, 255);')
        self.btnDownload.setText('Download')
        # self.btnDownload.clicked.connect(self.showLogs)
        
        # Stop Button
        self.btnStop = QToolButton(self.gbDownload)
        self.btnStop.setGeometry(500, 173, 101, 31)
        self.btnStop.setFont(QFont('', 11, QFont.Bold))
        self.btnStop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnStop.setStyleSheet('color: rgb(255, 0, 0); background-color: rgb(255, 255, 255);')
        self.btnStop.setText('Stop')
        # self.btnStop.clicked.connect(self.showLogs)
        
        # Clear Button
        self.btnClear = QToolButton(self.gbDownload)
        self.btnClear.setGeometry(80, 173, 101, 31)
        self.btnClear.setFont(QFont('', 11, QFont.Bold))
        self.btnClear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClear.setStyleSheet('color: rgb(255, 170, 0); background-color: rgb(255, 255, 255);')
        self.btnClear.setText('Clear')
        self.btnClear.clicked.connect(self.clear_code)
        
        # Amount Label
        self.lbAmount = QLabel(self.gbDownload)
        self.lbAmount.setGeometry(580, 70, 91, 31)
        self.lbAmount.setText('<html><head/><body><p><span style=" font-weight:600; color:#ffffff;">Amount Delay</span></p></body></html>')
        self.lbAmount.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        # Time Delay ComboBox
        self.comAmtDelay = QComboBox(self.gbDownload)
        self.comAmtDelay.setGeometry(670, 70, 61, 31)
        self.comAmtDelay.setFont(QFont('', 10))
        self.comAmtDelay.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);')
        self.comAmtDelay.setCursor(QCursor(Qt.PointingHandCursor))
        self.comAmtDelay.setCurrentIndex(4)
        self.comAmtDelay.addItems(['10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '200', '300', '400', '500'])
        
        # Delay Label
        self.lbDelay = QLabel(self.gbDownload)
        self.lbDelay.setGeometry(580, 110, 91, 31)
        self.lbDelay.setText('<html><head/><body><p><span style=" font-weight:600; color:#ffffff;">Time Delay (s)</span></p></body></html>')
        self.lbDelay.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        # Time Delay ComboBox
        self.comTimeDelay = QComboBox(self.gbDownload)
        self.comTimeDelay.setGeometry(670, 110, 61, 31)
        self.comTimeDelay.setFont(QFont('', 10))
        self.comTimeDelay.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);')
        self.comTimeDelay.setCursor(QCursor(Qt.PointingHandCursor))
        self.comTimeDelay.setCurrentIndex(1)
        self.comTimeDelay.addItems(['5', '10', '15', '20', '25', '30'])
        
        # API Key TextEdit
        self.txtAPIKey = QPlainTextEdit(self.gbDownload)
        self.txtAPIKey.setGeometry(80, 21, 541, 31)
        self.txtAPIKey.setFont(QFont('Roboto', 9))
        self.txtAPIKey.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);')
        
        # API Key Label
        self.lbAPIKey = QLabel(self.gbDownload)
        self.lbAPIKey.setGeometry(30, 20, 51, 31)
        self.lbAPIKey.setText('<html><head/><body><p><span style=" font-weight:600; color:#ffffff;">API Key</span></p></body></html>')
        self.lbAPIKey.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        # Version CheckBox
        self.chkBoxAPIKey = QCheckBox('Save API Key', self.gbDownload)
        self.chkBoxAPIKey.setGeometry(640, 20, 91, 31)
        self.chkBoxAPIKey.setFont(QFont('', 9))
        self.chkBoxAPIKey.setStyleSheet('color: rgb(255, 255, 255);')
        self.chkBoxAPIKey.setCursor(QCursor(Qt.PointingHandCursor))
        self.chkBoxAPIKey.setChecked(True)
        # self.chkBoxAPIKey.clicked.connect(self.isChecked)

        # Progress Bar
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(10, 520, 761, 16)
        self.progressBar.setStyleSheet('background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);')
        self.progressBar.setValue(0)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setInvertedAppearance(False)
        # self.progressBar.clicked.connect(self.isProgressBar)


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos()
            self.mouse_drag_active = True

    def mouseMoveEvent(self, event):
        if self.mouse_drag_active and event.buttons() == Qt.LeftButton:
            delta = event.globalPos() - self.drag_start_position
            self.move(self.pos() + delta)
            self.drag_start_position = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_drag_active = False


    def confirmClose(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Question)
        message_box.setWindowTitle('បញ្ជាក់ការបិទ')
        message_box.setText('តើអ្នកពិតជាចង់បិទចោលកម្មវិធីមែនឬទេ?')

        yes_button = message_box.addButton('យល់ព្រម', QtWidgets.QMessageBox.YesRole)
        yes_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        no_button = message_box.addButton('បដិសេដ', QtWidgets.QMessageBox.NoRole)
        no_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        message_box.setDefaultButton(no_button)
        reply = message_box.exec_()
        if message_box.clickedButton() == yes_button:
            QtCore.QCoreApplication.instance().quit()


    def showInfo(self):
        info_text = """
        <html>
            <body style='font-size: 10pt; color: white; background-color: gray;'>
                <h1>Owner Info</h1>
                <hr>
                <p>កម្មវិធីឈ្មោះ: Pixel Footage Video Downloader</p>
                <p>សរសេរដោយ: Phekdey PHORN | ផន ភក្ដី</p>
                <p>ទំនាក់ទំនង: 089 755 770</p>
                <p>ភាសាកូដៈ Python</p>
                <p>បង្កើតថ្ងៃៈ 08-Auguest-2024</p>
                <p>បច្ចុប្បន្នភាពចុងក្រោយៈ 08-Auguest-2024</p>
                <p>ការប្រើប្រាស់ៈ Free</p>
                <p>កំណែទម្រង់ៈ 1.0</p>
                <br>
                <h1>User Info</h1>
                <hr>
                <p>Machine ID: {current}</p>
                <p>License Key: {current}</p>
                <p>Create Key: {current}</p>
                <p>Expiry Key: {current}</p>
            </body>
        </html>
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Info")
        msg_box.setText(info_text)
        msg_box.setStyleSheet("QLabel{min-width: 600px;}")
        return_button = msg_box.addButton("ត្រលប់", QMessageBox.AcceptRole)
        return_button.setStyleSheet("color: white;")
        return_button.setCursor(Qt.PointingHandCursor)
        msg_box.exec_()
        return_button.clicked.connect(msg_box.close)


    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "សូមជ្រើសរើសទីតាំង")
        if directory:
            self.txtPathSave.setPlainText(directory)


    def check_path(self):
        path = self.txtPathSave.toPlainText().strip()
        if path and not os.path.isdir(path):
            warning_box = QMessageBox(self)
            warning_box.setWindowTitle('ទីតាំងមិនត្រឹមត្រូវ')
            warning_box.setText('សូមជ្រើសរើសទីតាំងដែលមានសុពលភាព ឬ ត្រឹមត្រូវ !')
            warning_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            warning_box.setStandardButtons(QMessageBox.Ok)
            warning_box.button(QMessageBox.Ok).setText('យល់ព្រម')
            warning_box.button(QMessageBox.Ok).setCursor(Qt.PointingHandCursor)
            warning_box.exec_()
            self.txtPathSave.clear()


    def clear_code(self):
        linkKeywordDownload = self.txtLinkDownload.toPlainText().strip()
        pathSave = self.txtPathSave.toPlainText().strip()

        if not linkKeywordDownload and not pathSave:
            warning_box = QMessageBox(self)
            warning_box.setWindowTitle('ការព្រមាន')
            warning_box.setText('មិនមានទិន្នន័យទេ!')
            warning_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            warning_box.setStandardButtons(QMessageBox.Ok)
            warning_box.button(QMessageBox.Ok).setText('យល់ព្រម')
            warning_box.button(QMessageBox.Ok).setCursor(Qt.PointingHandCursor)
            warning_box.exec_()
        elif linkKeywordDownload or pathSave:
            confirmation_box = QMessageBox(self)
            confirmation_box.setWindowTitle('បញ្ជាក់ការសម្អាត')
            confirmation_box.setText('តើអ្នកពិតជាចង់សម្អាតទម្រង់វាចោលមែនទេ?')
            confirmation_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirmation_box.button(QMessageBox.Yes).setText('យល់ព្រម')
            confirmation_box.button(QMessageBox.Yes).setCursor(Qt.PointingHandCursor)
            confirmation_box.button(QMessageBox.No).setText('បដិសេដ')
            confirmation_box.button(QMessageBox.No).setCursor(Qt.PointingHandCursor)
            
            reply = confirmation_box.exec_()
            if reply == QMessageBox.Yes:
                self.txtLinkDownload.clear()
                self.txtPathSave.clear()
                self.comAmtDelay.setCurrentIndex(4)
                self.comTimeDelay.setCurrentIndex(1)

    def showLogs(self):
        confirmation_box = QMessageBox(self)
        confirmation_box.setWindowTitle('បញ្ជាក់ការបើកមើល log')
        confirmation_box.setText('តើអ្នកពិតជាចង់មើល log មែនទេ?')
        confirmation_box.setStyleSheet("""
            QLabel { color: white; }
            QPushButton { color: white; background-color: rgb(50, 50, 50); }
        """)
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation_box.button(QMessageBox.Yes).setText('យល់ព្រម')
        confirmation_box.button(QMessageBox.Yes).setCursor(Qt.PointingHandCursor)
        confirmation_box.button(QMessageBox.No).setText('បដិសេដ')
        confirmation_box.button(QMessageBox.No).setCursor(Qt.PointingHandCursor)
        reply = confirmation_box.exec_()

        if reply == QMessageBox.Yes:
            log_dir = r"C:\Tools Data\Pixabay DL Logs"
            if os.path.exists(log_dir):
                try:
                    # Open the directory in file explorer
                    if os.name == 'nt':  # For Windows
                        os.startfile(log_dir)
                    elif os.name == 'posix':  # For Unix-like OS
                        subprocess.call(['xdg-open', log_dir])
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Unable to open log directory: {e}")
            else:
                QMessageBox.warning(self, "Path Not Found", "Log directory does not exist.")







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



