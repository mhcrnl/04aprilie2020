#!/usr/bin/env python
""" wxPython text editor app
    Run : python 01wxPythonTextEditor
    Author: mihai cornel mhcrnl@gmail.com
    NEXT: 1) Function for MenuBar v
          2) Adding Edit menu
"""
import wx
import os

class MyFrame(wx.Frame):
    def __init__(self, parent, title=""):
        super(MyFrame, self).__init__(parent, title=title, size=(800,800))
        self.Centre()
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.control.SetDefaultStyle(wx.TextAttr(wx.RED))
        self.control.SetBackgroundColour(wx.BLACK)
        """Adaugarea unui status bar in josul ferestrei"""
        self.CreateStatusBar()
        #Adaugarea meniului ferestrei
        self.MakeMenuBar()
        """
        filemenu = wx.Menu()
        #----------------------------------------------------------Adaugarea meniului
        openMenu = filemenu.Append(wx.ID_OPEN, "&Open", "Open file")
        self.Bind(wx.EVT_MENU, self.OnOpen, openMenu)

        saveAsMenu = filemenu.Append(wx.ID_SAVE, "&Save", "Save file")
        self.Bind(wx.EVT_MENU, self.OnSave1, saveAsMenu)
        
        aboutMenu=filemenu.Append(wx.ID_ABOUT, "&About", "Informatii despre program")
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutMenu)
        
        filemenu.AppendSeparator()
        
        exitMenu = filemenu.Append(wx.ID_EXIT, "E&xit", "Inchiderea programului")
        self.Bind(wx.EVT_MENU, self.OnExit, exitMenu)

        #-----------------------------------------------------Crearea barei de meniu
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)
        """
        # 1)---------------------------------------------------------Adding app icon 
        ico = wx.Icon("open1.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
    # 1)--------------------------------------------------------functie MakeMenuBor()
    def MakeMenuBar(self):
        # Create the menubar
        self.menubar     = wx.MenuBar()
        self.menu_FILE   = wx.Menu()
        self.menu_EDIT   = wx.Menu()
        self.menu_PREFERANCES = wx.Menu()
        self.menu_ABOUT  = wx.Menu()

        self.menu_NEW = self.menu_FILE.Append(wx.ID_ANY,'&New\tCtrl+N', "Create new tab")
        self.menu_OPEN = self.menu_FILE.Append(wx.ID_OPEN,'&Open\tCtrl+O', "Open a file")
        self.menu_FILE.AppendSeparator()
        self.menu_SAVE = self.menu_FILE.Append(wx.ID_SAVE,'&Save\tCtrl+S', "Save a file")
        self.menu_FILE.AppendSeparator()
        self.menu_SAVE_AS=self.menu_FILE.Append(wx.ID_SAVEAS,'&Save as...', "Save file as")
        self.menu_EXIT=self.menu_FILE.Append(wx.ID_EXIT,'&Exit\tCtrl+E', "Close the editor")
                    
        self.menubar.Append(self.menu_FILE, "&File")
        self.menubar.Append(self.menu_EDIT, "&Edit")
        self.menubar.Append(self.menu_PREFERANCES, "&Preferances")
        self.menubar.Append(self.menu_ABOUT, "&About")
        self.SetMenuBar(self.menubar)
 
        self.Bind(wx.EVT_MENU, self.OnNew, self.menu_NEW)
        self.Bind(wx.EVT_MENU, self.OnOpen, self.menu_OPEN)
        self.Bind(wx.EVT_MENU, self.OnSave1, self.menu_SAVE) 
        self.Bind(wx.EVT_MENU, self.OnSaveAs, self.menu_SAVE_AS) 
        self.Bind(wx.EVT_MENU, self.OnExit, self.menu_EXIT) 
    #--------------------------------------------------------functie OnNew()
    def OnNew(self, event):
        textEditor_new = TextEditor(False)
        textEditor_new.MainLoop()
    #---------------------------------------------------------functie OnSaveAs()
    def OnSaveAs(self, event):
        with wx.FileDialog(self, 
                message="Choose a file",
                defaultDir="",
                defaultFile="*.*",
                style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            itcontents = self.control.GetValue()
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w') as file:
                    file.write(itcontents)
                    file.close()
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)
        fileDialog.Destroy()
    #--------------------------------------------------------------functie OnAbout()
    def OnAbout(self, e):
        #Un dialog cu un buton de ok
        dlg=wx.MessageDialog(self, "Un text editor simplu.", "Despre editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

		
    #------------------------------------------------------------------functie OnExit()
    def OnExit(self, e):
        #Inchiderea ferestrei
        self.Close(True)
    #------------------------------------------------------------------functie OnOpen()
    def OnOpen(self, e):
        """Open a file """
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()

        dlg.Destroy()
    """    
    #-----------------------------------------------------------------functie OnSave()
    def OnSave(self, e):
        with wx.FileDialog(self, "Save file", "*.*", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w') as file:
                    self.doSaveData(file)
            except IOError:
                wx.LogError("Nu a fost salvata fila '%s'." % pathname)
    """ 
    #-----------------------------------------------------------------function OnSave1()
    def OnSave1(self, event):
        dlg = wx.FileDialog(self, "Choose a File", "", "*.*",style= wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be save
            itcontains = self.control.GetValue()
            # Open the file for write, close
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            filehandle = open(os.path.join(self.dirname, self.filename), 'w')
            filehandle.write(itcontains)
            filehandle.close()
        dlg.Destroy()
    #--------------------------------------------------------------------------------------
class TextEditor(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="wxPython Text Editor")
    	# 2)---------------------------------------------------Center the frame
        self.frame.Centre()
        self.frame.Show()
        return True

if __name__ == "__main__":
    texteditor = TextEditor(False)
    texteditor.MainLoop()



