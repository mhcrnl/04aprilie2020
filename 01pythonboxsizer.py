#!/usr/bin/env python
import wx

class MyForm(wx.Frame):

    #global fahrTC

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="MyForm")

        self.panel = wx.Panel(self, wx.ID_ANY)
        #------------------------------------------------------------
        fahrLB = wx.StaticText(self.panel, wx.ID_ANY, "Fahrenheit")
        self.fahrTC = wx.TextCtrl(self.panel, wx.ID_ANY, "")
        #------------------------------------------------------------
        calcBT = wx.Button(self.panel, wx.ID_ANY, "CALCULEAZA")
        self.Bind(wx.EVT_BUTTON, self.OnCalculeaza, calcBT)

        celsLB = wx.StaticText(self.panel, wx.ID_ANY, "Celsius")
        self.celsTC = wx.TextCtrl(self.panel, wx.ID_ANY, "")
        #----------------------------------------------------------
        closeBT= wx.Button(self.panel, wx.ID_ANY, "CLOSE")
        self.Bind(wx.EVT_BUTTON, self.OnClose, closeBT)

        vBoxSizer = wx.BoxSizer(wx.VERTICAL)
        
        vBoxSizer.Add(fahrLB,  0, wx.ALL|wx.EXPAND, 5)
        vBoxSizer.Add(self.fahrTC,  0, wx.ALL|wx.EXPAND, 5)
        vBoxSizer.Add(calcBT,  0, wx.ALL|wx.EXPAND, 5)
        vBoxSizer.Add(celsLB,  0, wx.ALL|wx.EXPAND, 5)
        vBoxSizer.Add(self.celsTC,  0, wx.ALL|wx.EXPAND, 5)
        vBoxSizer.Add(closeBT, 0, wx.ALL|wx.EXPAND, 5)

        
        self.panel.SetSizer(vBoxSizer)
        vBoxSizer.Fit(self)
    #--------------------------------------------------------------
    def OnClose(self, event):
        self.Close()
    #--------------------------------------------------------------
    def OnCalculeaza(self, event):
        fahr = float(self.fahrTC.GetValue())
        cels =str((fahr-32)*5/9)
        print(self.fahrTC.GetValue())
        self.celsTC.SetValue(cels)
    #--------------------------------------------------------------
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()

    
