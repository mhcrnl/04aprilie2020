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
        #-------------------------------------------------------Statusbar
        self.CreateStatusBar()
        #-------------------------------------------------------FileMenu
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_ABOUT, "&About", "Informatii despre program")
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

