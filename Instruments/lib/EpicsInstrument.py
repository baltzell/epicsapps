#!/usr/bin/python

import wx
import sys

sys.path.insert(0, '.')

from InstrumentApp import InstrumentFrame

app = wx.PyApp()
frame = InstrumentFrame(conf=None, dbname=None)
frame.Show()        
app.MainLoop()
