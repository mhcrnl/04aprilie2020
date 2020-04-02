#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Create by: mhcrnl@gmail.com Date: 01.04.2020 Scope: blue print for all
    wx.Python programs """ 
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title=""):
        super(MyFrame, self).__init__(parent, title=title, size=(800,650))
        #-------------------------------------------------------Add PANEL
        self.panel = wx.Panel(self)

        vBox = wx.BoxSizer(wx.VERTICAL)

        fahHBox = wx.BoxSizer(wx.HORIZONTAL)
        fahST = wx.StaticText(self.panel, wx.ID_ANY, "Fahrenheit")
        fahTC = wx.TextCtrl(self.panel, wx.ID_ANY, "")
        
        celBox = wx.BoxSizer(wx.HORIZONTAL)
        celST = wx.StaticText(self.panel, wx.ID_ANY, "Celsius    ")
        celTC = wx.TextCtrl(self.panel, wx.ID_ANY, "")
        
        fahHBox.Add(fahST, 0, wx.ALL, 5)
        fahHBox.Add(fahTC, 0, wx.ALL, 5)
        
        celBox.Add(celST, 0, wx.ALL, 5)
        celBox.Add(celTC, 0, wx.ALL, 5)

        vBox.Add(fahHBox, 0, wx.ALL, 5)
        vBox.Add(celBox, 0, wx.ALL, 5)

        self.panel.SetSizer(vBox)
        #-------------------------------------------------------Statusbar
        self.CreateStatusBar()
        #-------------------------------------------------------FileMenu
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_ABOUT,"&Calculeaza", "Calculeaza celsius")
        fileMenu.AppendSeparator()
        menuExit = fileMenu.Append(wx.ID_EXIT, "E&xit", "Inchide programul")
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit) 
        #------------------------------------------------------------------
        helpMenu = wx.Menu()
        helpMenu.Append(wx.ID_ABOUT, "&Despre", "Despre program")
        #-------------------------------------------------------HelpMenu
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)
        self.Show(True)
        #----------------------------------------------------------------
    def OnExit(self, event):
        self.Close(True)
        #----------------------------------------------------------------
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Main Frame")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()

