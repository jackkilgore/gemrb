# -*-python-*-
# GemRB - Infinity Engine Emulator
# Copyright (C) 2003-2004 The GemRB Project
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# $Header: /data/gemrb/cvs2svn/gemrb/gemrb/gemrb/GUIScripts/bg2/LoadScreen.py,v 1.9 2005/03/16 07:14:46 edheldil Exp $

# LoadScreen.py - display Loading screen

###################################################

import GemRB
from GUIDefines import *

LoadScreen = None

def StartLoadScreen ():
	global LoadScreen

	GemRB.LoadWindowPack ("guils", 640, 480)
	LoadScreen = GemRB.LoadWindow (0)
	GemRB.SetWindowFrame (LoadScreen)
	Middle = GemRB.GetControl (LoadScreen, 3)
	LoadPic = GemRB.GetGameString (STR_LOADMOS)
	if LoadPic == "":
		LoadPic = "GTRSK00"+str(GemRB.Roll(1,5,1) )
	GemRB.SetButtonMOS (LoadScreen, Middle, LoadPic)
	Progress = 0
	GemRB.SetVar ("Progress", Progress)
	Table = GemRB.LoadTable ("loadhint")
	tmp = GemRB.GetTableRowCount (Table)
	tmp = GemRB.Roll (1,tmp,0)
	HintStr = GemRB.GetTableValue (Table, tmp, 0)
	TextArea = GemRB.GetControl (LoadScreen, 2)
	GemRB.SetText (LoadScreen, TextArea, HintStr)
	Bar = GemRB.GetControl (LoadScreen, 0)
	GemRB.SetVarAssoc (LoadScreen, Bar, "Progress", Progress)
	GemRB.SetVisible (LoadScreen, 1)
