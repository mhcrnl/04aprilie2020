#!/usr/bin/env python

import wx

class MyFrame(wx.Frame):

    def __init__ (self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 800))
        #Adaugam un TextCtrl pentru editarea textului
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        #Adaugare unui status bar in josul ferestrei

        #Adaugarea unui meniu in partea de sus a ferestrei

        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, "Text Editor")
app.MainLoop()

