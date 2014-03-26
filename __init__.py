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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load epsgiolookup class from file epsgiolookup
    from epsgiolookup import epsgiolookup
    return epsgiolookup(iface)
