# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_epsgiolookup.ui'
#
# Created: Tue Mar 25 19:27:53 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_epsgiolookup(object):
    def setupUi(self, epsgiolookup):
        epsgiolookup.setObjectName(_fromUtf8("epsgiolookup"))
        epsgiolookup.resize(653, 584)
        self.buttonBox = QtGui.QDialogButtonBox(epsgiolookup)
        self.buttonBox.setGeometry(QtCore.QRect(290, 540, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(epsgiolookup)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(epsgiolookup)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 621, 201))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setEnabled(True)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEditEPSGCode = QtGui.QLineEdit(self.tab)
        self.lineEditEPSGCode.setGeometry(QtCore.QRect(60, 30, 113, 28))
        self.lineEditEPSGCode.setObjectName(_fromUtf8("lineEditEPSGCode"))
        self.pushButton_EPSGSearch = QtGui.QPushButton(self.tab)
        self.pushButton_EPSGSearch.setGeometry(QtCore.QRect(180, 30, 87, 27))
        self.pushButton_EPSGSearch.setObjectName(_fromUtf8("pushButton_EPSGSearch"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(18, 33, 41, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 241, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_FullText = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_FullText.setGeometry(QtCore.QRect(10, 30, 221, 28))
        self.lineEdit_FullText.setObjectName(_fromUtf8("lineEdit_FullText"))
        self.pushButton_FullTextSearch = QtGui.QPushButton(self.tab_2)
        self.pushButton_FullTextSearch.setGeometry(QtCore.QRect(140, 60, 87, 27))
        self.pushButton_FullTextSearch.setObjectName(_fromUtf8("pushButton_FullTextSearch"))
        self.listWidget = QtGui.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(240, 10, 361, 141))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 581, 91))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.label_2 = QtGui.QLabel(epsgiolookup)
        self.label_2.setGeometry(QtCore.QRect(10, 250, 391, 18))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableView_Results = QtGui.QTableView(epsgiolookup)
        self.tableView_Results.setGeometry(QtCore.QRect(10, 280, 621, 221))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_Results.sizePolicy().hasHeightForWidth())
        self.tableView_Results.setSizePolicy(sizePolicy)
        self.tableView_Results.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView_Results.setObjectName(_fromUtf8("tableView_Results"))
        self.tableView_Results.horizontalHeader().setDefaultSectionSize(120)
        self.tableView_Results.horizontalHeader().setSortIndicatorShown(True)
        self.tableView_Results.horizontalHeader().setStretchLastSection(True)
        self.tableView_Results.verticalHeader().setDefaultSectionSize(50)

        self.retranslateUi(epsgiolookup)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), epsgiolookup.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), epsgiolookup.reject)
        QtCore.QMetaObject.connectSlotsByName(epsgiolookup)

    def retranslateUi(self, epsgiolookup):
        epsgiolookup.setWindowTitle(QtGui.QApplication.translate("epsgiolookup", "epsgiolookup", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("epsgiolookup", "EPSG.IO Projection Lookup", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEPSGCode.setText(QtGui.QApplication.translate("epsgiolookup", "27700", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_EPSGSearch.setText(QtGui.QApplication.translate("epsgiolookup", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("epsgiolookup", "EPSG:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("epsgiolookup", "By EPSG Code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("epsgiolookup", "Enter Text Query (e.g. Kansas)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_FullTextSearch.setText(QtGui.QApplication.translate("epsgiolookup", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("epsgiolookup", "By Full Text Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("epsgiolookup", "This widget lets you look up EPSG projection definitions using the API provided by epsg.info. You can look up using either the EPSG numeric code, or do a full text search to find a list of possible projections. Widget written by Steven Kay (@stevefaeembra)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("epsgiolookup", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("epsgiolookup", "Results - click on a cell to copy to clipboard", None, QtGui.QApplication.UnicodeUTF8))

