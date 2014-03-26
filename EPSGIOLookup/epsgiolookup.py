# -*- coding: utf-8 -*-
"""
/***************************************************************************
 epsgiolookup
                                 A QGIS plugin
 tool to query epsg.io website for projection details
                              -------------------
        begin                : 2014-03-24
        copyright            : (C) 2014 by Steven Kay
        email                : stevendkay{at}gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from epsgiolookupdialog import epsgiolookupDialog
import os.path
import urllib
import json

class epsgiolookup:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'epsgiolookup_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = epsgiolookupDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/epsgiolookup/icon.png"),
            u"EPSG.IO Lookup", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)
        
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&epsgiolookup", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&epsgiolookup", self.action)
        self.iface.removeToolBarIcon(self.action)

    def getjsonresponse(self, url):
        response = urllib.urlopen(url) 
        jsontext = response.read()
        return json.loads(jsontext)
    
    def epsgquery(self, widget):
        ''' do query based on EPSG code'''
        url = "http://epsg.io/?q=%d&format=json" % int(self.dlg.lineEditEPSGCode.text())
        resp = self.getjsonresponse(url)
        resptext = json.dumps(resp)
        header=['Key','Value']
        data_list=[]
        
        try:
            lists = resp['results'][0]
            for x in lists:
                data_list.append((x,lists[x]))
        except:
            data_list.append(("Error", "No matches found for EPSG:%s" % self.dlg.lineEditEPSGCode.text()))
                
        table_model = MyTableModel(self.dlg, data_list, header)
        self.dlg.tableView_Results.setModel(table_model)
        
    def textquery(self, widget):
        ''' do query based on text query'''
        url = "http://epsg.io/?q=%s&format=json" % self.dlg.lineEdit_FullText.text()
        resp = self.getjsonresponse(url)
        resptext = json.dumps(resp)
        header=['EPSG','Name']
        data_list=[]
        try :
            for result in resp['results']:
                lists = result
                print lists
                name = lists['name']
                code = lists['code']
                data_list.append((code, name))
        except:
            data_list.append(("Error", "No matches found for %s" % self.dlg.lineEdit_FullText.text()))
        table_model = MyTableModel(self.dlg, data_list, header)
        self.dlg.tableView_Matches.setModel(table_model)
        
    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        self.dlg.pushButton_EPSGSearch.clicked.connect(self.epsgquery)
        self.dlg.pushButton_FullTextSearch.clicked.connect(self.textquery)
        self.dlg.tableView_Results.clicked.connect(self.copytoclip)
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass
        
    def copytoclip(self, widget):
        r = widget.row()
        c = widget.column()
        cellval =  widget.child(r,c).data()
        self.dlg.plainTextEdit_Clipboard.setPlainText(str(cellval))
    
class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
    def rowCount(self, parent):
        return len(self.mylist)
    def columnCount(self, parent):
        if not self.mylist:
            return 0
        return len(self.mylist[0])
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))