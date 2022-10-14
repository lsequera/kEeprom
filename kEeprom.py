#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eeprom.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.label.setObjectName("label")

        self.eepromChooser = QtWidgets.QComboBox(self.centralwidget)
        self.eepromChooser.setGeometry(QtCore.QRect(120, 10, 86, 30))
        self.eepromChooser.setEditable(False)
        self.eepromChooser.setObjectName("eepromChooser")

        self.readE = QtWidgets.QPushButton(self.centralwidget)
        self.readE.setGeometry(QtCore.QRect(700, 10, 91, 31))
        self.readE.setObjectName("readE")

        self.writeE = QtWidgets.QPushButton(self.centralwidget)
        self.writeE.setGeometry(QtCore.QRect(700, 50, 91, 30))
        self.writeE.setObjectName("writeE")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 130, 781, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 777, 497))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.eepromFile = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.eepromFile.setGeometry(QtCore.QRect(0, 0, 401, 401))
        self.eepromFile.setObjectName("eepromFile")
        self.eepromFile.setReadOnly(True)
        self.eepromFile.setFont(QtGui.QFont('Hack',10))

        self.outputLog = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.outputLog.setGeometry(QtCore.QRect(400, 0, 381, 401))
        self.outputLog.setObjectName("outputLog")
        self.outputLog.setReadOnly(True)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 241, 31))
        self.label_2.setObjectName("label_2")

        self.loadFile = QtWidgets.QPushButton(self.centralwidget)
        self.loadFile.setGeometry(QtCore.QRect(10, 60, 121, 38))
        self.loadFile.setObjectName("loadFile")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 10, 231, 36))
        self.lineEdit.setObjectName("lineEdit")

        self.verifyE = QtWidgets.QPushButton(self.centralwidget)
        self.verifyE.setGeometry(QtCore.QRect(700, 90, 91, 30))
        self.verifyE.setObjectName("verifyE")

        self.eraseE = QtWidgets.QPushButton(self.centralwidget)
        self.eraseE.setGeometry(QtCore.QRect(700, 540, 91, 30))
        self.eraseE.setObjectName("eraseE")

        self.filenamelabel = QtWidgets.QLabel(self.centralwidget)
        self.filenamelabel.setGeometry(QtCore.QRect(140, 60, 551, 41))
        self.filenamelabel.setObjectName("filenamelabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 34))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
       
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        #self.actionSave = QtWidgets.QAction(MainWindow)
        #self.actionSave.setObjectName("actionSave")

        self.actionAcerca_de_Eeprom = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de_Eeprom.setObjectName("actionAcerca_de_Eeprom")

        self.menuFile.addAction(self.actionOpen)
        #self.menuFile.addAction(self.actionSave)
        self.menuHelp_2.addAction(self.actionAcerca_de_Eeprom)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())
        
        self.trans = QtCore.QTranslator()
        
        self.trans.load("es-eng")
        QtCore.QCoreApplication.instance().installTranslator(self.trans)

        #MainWindow.setWindowIcon(QtGui.QIcon.fromTheme('cpu'))
        MainWindow.setWindowIcon(QtGui.QIcon('sop8.svg'))
        
        Eeproms = ["25qXX","24c01","24c02","24c04","24c08","24c16","24c32","24c64","24c128","24c256","24c512","24c1024"]
        self.eepromChooser.addItems(Eeproms)
        
        self.loadFile.clicked.connect(self.getFile)
        
        self.readE.clicked.connect(self.readEeprom)

        self.writeE.clicked.connect(self.writeEeprom)

        self.verifyE.clicked.connect(self.verifyEeprom)

        self.eraseE.clicked.connect(self.eraseEeprom)

        self.actionOpen.triggered.connect(self.getFile)

        self.actionAcerca_de_Eeprom.triggered.connect(self.showAbout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "kEeprom"))
        self.label.setText(_translate("MainWindow", "Elegir Eeprom:"))
        self.readE.setText(_translate("MainWindow", "Leer"))
        self.writeE.setText(_translate("MainWindow", "Escribir"))
        self.label_2.setText(_translate("MainWindow", "Nombre de Archivo para Guardar:"))
        self.loadFile.setText(_translate("MainWindow", "Cargar Archivo"))
        self.verifyE.setText(_translate("MainWindow", "Verificar"))
        self.eraseE.setText(_translate("MainWindow", "Borrar"))
        self.filenamelabel.setText(_translate("MainWindow", "No se ha cargado un archivo!"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionOpen.setText(_translate("MainWindow", "Abrir"))
        #self.actionSave.setText(_translate("MainWindow", "Guardar"))
        self.actionAcerca_de_Eeprom.setText(_translate("MainWindow", "Acerca de kEeprom"))

    fileName = ''

    def getFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(parent=MainWindow, caption="Seleccionar Archivo", directory=os.getcwd(), filter="Data File (*.bin)")
        print(fname)
        self.fileName = fname[0]
        self.loadFileDoc(fname[0])
        return fname

    def readbytes(self,filename):
        bytes = []
        with open(filename,'rb') as f:
            while True:
                b = f.read(1)
                if not b:
                    break
                bytes.append(int.from_bytes(b, byteorder='big'))
        return bytes

    def loadFileDoc(self,filename):
        b = self.readbytes(filename)
        print(b)
        self.outputLog.insertPlainText('El archivo tiene tamaño de: '+str(len(b))+'KiB\n')
        self.eepromFile.setPlainText('')
        x = 15
        for i in range(len(b)):
            self.eepromFile.insertPlainText('{0:02X}'.format(b[i])+' ')
            if i == x:
                self.eepromFile.insertPlainText('\n')
                x+=16
        self.filenamelabel.setText('Se ha cargado el archivo: '+filename)

    def checkDevice(self):
        x = ''
        try:
            x = str(subprocess.check_output(['lsusb','-d','1a86:5512']),encoding='utf-8')
            self.outputLog.insertPlainText(x+'\n')
        except subprocess.CalledProcessError as err:
            self.outputLog.insertPlainText(str(err)+'\n')
        if not x == '':
            print(x)
            y = True
        else:
            y = False
        return y

    def readEeprom(self):
        print('Leyendo Eeprom')
        self.statusbar.showMessage('Leyendo Eeprom')
        y = self.checkDevice()
        filetoSave = self.lineEdit.text()
        size = self.eepromChooser.currentText()
        #print("Archivo: "+ filetoSave + ", Eeprom: " + size)
        if y == True:
            if not filetoSave == '':
                if size == '25qXX':
                    try:
                        self.outputLog.insertPlainText(str(subprocess.check_output(['flashrom','-p','ch341a_spi','-r',filetoSave+'.bin','-V']),encoding='utf-8'))
                    except subprocess.CalledProcessError as err:
                        self.outputLog.insertPlainText(str(err)+'\n')
                else:
                    try:
                        self.outputLog.insertPlainText(str(subprocess.check_output(['./ch341eeprom','-s',size,'-r',filetoSave+'.bin']),encoding='utf-8'))
                    except subprocess.CalledProcessError as err:
                        self.outputLog.insertPlainText(str(err)+'\n')
                self.outputLog.insertPlainText('Se ha guardado el archivo: '+filetoSave+'.bin\n')
                self.loadFileDoc(filetoSave+'.bin')
                self.fileName = filetoSave+'.bin'
            else:
                self.outputLog.insertPlainText('Debe introducir un nombre de Archivo para Guardar\n')
        else:
            self.outputLog.insertPlainText('Debe conectar el programador a un puerto USB\n')
        #
    
    def writeEeprom(self):
        print('Escribiendo Eeprom')
        self.statusbar.showMessage('Escribiendo Eeprom')
        y = self.checkDevice()
        filetoWrite = self.fileName

        size = self.eepromChooser.currentText()
        #print("Archivo: "+ filetoSave + ", Eeprom: " + size)
        if y == True:
            if not filetoWrite == '':
                if size == '25qXX':
                    try:
                        self.outputLog.insertPlainText(str(subprocess.check_output(['flashrom','-p','ch341a_spi','-w',filetoWrite,'-V']),encoding='utf-8'))
                    except subprocess.CalledProcessError as err:
                        self.outputLog.insertPlainText(str(err)+'\n')
                    self.outputLog.insertPlainText('Se ha escrito el archivo: '+filetoWrite+' en la Eeprom: 25QXX'+'\n Se sugiere Vericar!\n')
                else:
                    try:
                        self.outputLog.insertPlainText(str(subprocess.check_output(['./ch341eeprom','-s',size,'-w',filetoWrite]),encoding='utf-8'))
                    except subprocess.CalledProcessError as err:
                        self.outputLog.insertPlainText(str(err)+'\n')
                    self.outputLog.insertPlainText('Se ha escrito el archivo: '+filetoWrite+' en la Eeprom: '+str(size)+'\n Se sugiere Vericar!\n')
            else:
                self.outputLog.insertPlainText('No se ha cargado un Archivo aun! \n Debe Cargar un Archivo para escribir en la Eeprom\n')
        else:
            self.outputLog.insertPlainText('Debe conectar el programador a un puerto USB\n')
                
    
    
    def verifyEeprom(self):
        print('Verificando Eeprom')
        self.statusbar.showMessage('Verificando Eeprom')
        y = self.checkDevice()
        filetoVerify = self.fileName
        size = self.eepromChooser.currentText()
        #print("Archivo: "+ filetoSave + ", Eeprom: " + size)
        if y == True:
            if not filetoVerify == '':
                if size == '25qXX':
                    try:
                        self.outputLog.insertPlainText(str(subprocess.check_output(['flashrom','-p','ch341a_spi','-v',filetoVerify+'.bin','-V']),encoding='utf-8'))
                    except subprocess.CalledProcessError as err:
                        self.outputLog.insertPlainText(str(err)+'\n')
                    self.outputLog.insertPlainText('Se ha verificado el archivo: '+filetoVerify+' en la Eeprom: 25QXX'+'\n Se sugiere Vericar!\n')
                else:
                    try:
                        self.outputLog.insertPlainText(str(subprocess.check_output(['./ch341eeprom','-s',size,'-v',filetoVerify]),encoding='utf-8'))
                    except subprocess.CalledProcessError as err:
                        self.outputLog.insertPlainText(str(err)+'\n')
                    self.outputLog.insertPlainText('Se ha verificado el archivo: '+filetoVerify+' en la Eeprom: '+str(size)+'\nTodo OK!\n')
            else:
                self.outputLog.insertPlainText('No se ha cargado un Archivo aun! \n Debe Cargar un Archivo para verificar en la Eeprom\n')
        else:
            self.outputLog.insertPlainText('Debe conectar el programador a un puerto USB\n')

    def eraseEeprom(self):
        print('Borrando Eeprom')
        self.statusbar.showMessage('Borrando Eeprom')
        time = str(datetime.now())
        y = self.checkDevice()
        backupFile = 'BackUp'+time+'.bin'
        size = self.eepromChooser.currentText()

        if y == True:
            if size == '25qXX':
                try:
                    self.outputLog.insertPlainText(str(subprocess.check_output(['flashrom','-p','ch341a_spi','-r',backupFile+'.bin','-V']),encoding='utf-8'))
                except subprocess.CalledProcessError as err:
                    self.outputLog.insertPlainText(str(err)+'\n')
                try:
                    self.outputLog.insertPlainText(str(subprocess.check_output(['flashrom','-p','ch341a_spi','-E','-V']),encoding='utf-8'))
                except subprocess.CalledProcessError as err:
                    self.outputLog.insertPlainText(str(err)+'\n')
                try:
                    self.outputLog.insertPlainText(str(subprocess.check_output(['flashrom','-p','ch341a_spi','-r','/tmp/erased'+time+'.bin','-V']),encoding='utf-8'))
                except subprocess.CalledProcessError as err:
                    self.outputLog.insertPlainText(str(err)+'\n')
            else:
                try:
                    self.outputLog.insertPlainText(str(subprocess.check_output(['./ch341eeprom','-s',size,'-r',backupFile+'.bin']),encoding='utf-8'))
                except subprocess.CalledProcessError as err:
                    self.outputLog.insertPlainText(str(err)+'\n')
                self.outputLog.insertPlainText('Se ha guardado el archivo de respaldo: '+backupFile+'.bin\n')
                try:
                    self.outputLog.insertPlainText(str(subprocess.check_output(['./ch341eeprom','-s',size,'-e']),encoding='utf-8'))
                except subprocess.CalledProcessError as err:
                    self.outputLog.insertPlainText(str(err)+'\n')
                try:
                    self.outputLog.insertPlainText(str(subprocess.check_output(['./ch341eeprom','-s',size,'-r','/tmp/erased'+time+'.bin']),encoding='utf-8'))
                except subprocess.CalledProcessError as err:
                    self.outputLog.insertPlainText(str(err)+'\n')
            self.loadFileDoc('/tmp/erased'+time+'.bin')
            self.outputLog.insertPlainText('Se ha borado la Eeprom: '+str(size)+'!\n')
        else:
            self.outputLog.insertPlainText('Debe conectar el programador a un puerto USB\n')

    def showAbout(self):
        aboutDlg = QtWidgets.QDialog()
        aboutDlg.setWindowTitle("Acerca de kEeprom")
        aboutDlg.setFixedSize(500,350)
        aboutDlg.setWindowFlag(QtCore.Qt.Tool)
        about = QtWidgets.QLabel(aboutDlg)
        about.setGeometry(QtCore.QRect(150, 10, 300, 300))
        #about.setObjectName("about")
        about.setText('kEeprom es un programa simple para \nLeer, Escribir, Verificar y Borrar memoria \nEeprom de la serie 24c y 25q')        
        image = QtWidgets.QLabel(aboutDlg)
        image.setGeometry(60,110,100,100)
        image.setPixmap(QtGui.QPixmap('sop8.png'))
        aboutDlg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

