#Boa:Frame:Frame1

import wx
import wx.richtext
import wx.gizmos
import os
import subprocess
import re
import xml.etree.ElementTree as ET  

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BITMAPBUTTON1, wxID_FRAME1BITMAPBUTTON2, 
 wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON6, 
 wxID_FRAME1BUTTON7, wxID_FRAME1BUTTON8, wxID_FRAME1BUTTON9, 
 wxID_FRAME1GENERICDIRCTRL1, wxID_FRAME1PANEL1, wxID_FRAME1SASHLAYOUTWINDOW1, 
 wxID_FRAME1SASHLAYOUTWINDOW2, wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTEDITOR, 
 wxID_FRAME1TEXTRETURN, 
] = [wx.NewId() for _init_ctrls in range(19)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(428, 269), size=wx.Size(1130, 702),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Android_Test')
        self.SetClientSize(wx.Size(1114, 664))
        self.Bind(wx.EVT_SIZE, self.OnFrame1Size)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(648, 0), size=wx.Size(463, 664),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetMinSize(wx.Size(455, 778))

        self.sashLayoutWindow1 = wx.SashLayoutWindow(id=wxID_FRAME1SASHLAYOUTWINDOW1,
              name='sashLayoutWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(272, 664), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashLayoutWindow1.SetExtraBorderSize(20)
        self.sashLayoutWindow1.SetAlignment(wx.LAYOUT_LEFT)
        self.sashLayoutWindow1.SetOrientation(wx.LAYOUT_VERTICAL)
        self.sashLayoutWindow1.SetSashVisible(wx.SASH_RIGHT, True)
        self.sashLayoutWindow1.SetExtraBorderSize(20)
        self.sashLayoutWindow1.SetDefaultSize(wx.Size(272, 778))
        self.sashLayoutWindow1.Bind(wx.EVT_SASH_DRAGGED,
              self.OnSashLayoutWindow1SashDragged,
              id=wxID_FRAME1SASHLAYOUTWINDOW1)

        self.sashLayoutWindow2 = wx.SashLayoutWindow(id=wxID_FRAME1SASHLAYOUTWINDOW2,
              name='sashLayoutWindow2', parent=self, pos=wx.Point(272, 0),
              size=wx.Size(378, 664), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashLayoutWindow2.SetDefaultSize(wx.Size(370, 664))
        self.sashLayoutWindow2.SetAlignment(wx.LAYOUT_LEFT)
        self.sashLayoutWindow2.SetOrientation(wx.LAYOUT_VERTICAL)
        self.sashLayoutWindow2.SetSashVisible(wx.SASH_RIGHT, True)
        self.sashLayoutWindow2.SetDefaultSize(wx.Size(378, 778))
        self.sashLayoutWindow2.Bind(wx.EVT_SASH_DRAGGED,
              self.OnSashLayoutWindow2SashDragged,
              id=wxID_FRAME1SASHLAYOUTWINDOW2)

        self.textReturn = wx.TextCtrl(id=wxID_FRAME1TEXTRETURN,
              name=u'textReturn', parent=self.panel1, pos=wx.Point(104, 0),
              size=wx.Size(1110, 1050), style=wx.TE_MULTILINE, value='')

        self.textEditor = wx.TextCtrl(id=wxID_FRAME1TEXTEDITOR,
              name=u'textEditor', parent=self.sashLayoutWindow2, pos=wx.Point(0,
              0), size=wx.Size(375, 664), style=wx.TE_MULTILINE, value='')
        self.textEditor.Bind(wx.EVT_LEFT_DOWN, self.OnTextEditorLeftDown)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'\u5355\u6b65\u6267\u884c', name='button1',
              parent=self.panel1, pos=wx.Point(8, 48), size=wx.Size(75, 24),
              style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2,
              label=u'\u6279\u91cf\u6267\u884c', name='button2',
              parent=self.panel1, pos=wx.Point(8, 128), size=wx.Size(75, 24),
              style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.genericDirCtrl1 = wx.GenericDirCtrl(defaultFilter=0, dir='.',
              filter='Fichier txt (*.txt)|*.txt', id=wxID_FRAME1GENERICDIRCTRL1,
              name='genericDirCtrl1', parent=self.sashLayoutWindow1,
              pos=wx.Point(0, 0), size=wx.Size(270, 664),
              style=wx.DIRCTRL_3D_INTERNAL | wx.SUNKEN_BORDER)
        self.genericDirCtrl1.SetMinSize(wx.Size(270, 664))
        self.genericDirCtrl1.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSel)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'\u4fdd\u5b58',
              name='button3', parent=self.panel1, pos=wx.Point(8, 248),
              size=wx.Size(75, 24), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4,
              label=u'\u53e6\u5b58\u4e3a', name='button4', parent=self.panel1,
              pos=wx.Point(8, 288), size=wx.Size(75, 24), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5,
              label=u'\u5f53\u524d\u8bbe\u5907', name='button5',
              parent=self.panel1, pos=wx.Point(8, 576), size=wx.Size(75, 24),
              style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_FRAME1BUTTON5)

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6,
              label=u'\u6e05\u7a7a\u7ed3\u679c', name='button6',
              parent=self.panel1, pos=wx.Point(8, 616), size=wx.Size(75, 24),
              style=0)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_FRAME1BUTTON6)

        self.button7 = wx.Button(id=wxID_FRAME1BUTTON7,
              label=u'\u6267\u884c\u9009\u4e2d', name='button7',
              parent=self.panel1, pos=wx.Point(8, 88), size=wx.Size(75, 24),
              style=0)
        self.button7.Bind(wx.EVT_BUTTON, self.OnButton7Button,
              id=wxID_FRAME1BUTTON7)

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.Bitmap(u'undo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BITMAPBUTTON1,
              name='bitmapButton1', parent=self.panel1, pos=wx.Point(8, 208),
              size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.bitmapButton1.Bind(wx.EVT_BUTTON, self.OnBitmapButton1Button,
              id=wxID_FRAME1BITMAPBUTTON1)

        self.bitmapButton2 = wx.BitmapButton(bitmap=wx.Bitmap(u'redo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BITMAPBUTTON2,
              name='bitmapButton2', parent=self.panel1, pos=wx.Point(56, 208),
              size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.bitmapButton2.Bind(wx.EVT_BUTTON, self.OnBitmapButton2Button,
              id=wxID_FRAME1BITMAPBUTTON2)

        self.button8 = wx.Button(id=wxID_FRAME1BUTTON8, label=u'Dump XML',
              name='button8', parent=self.panel1, pos=wx.Point(8, 384),
              size=wx.Size(75, 24), style=0)
        self.button8.Bind(wx.EVT_BUTTON, self.OnButton8Button,
              id=wxID_FRAME1BUTTON8)

        self.button9 = wx.Button(id=wxID_FRAME1BUTTON9,
              label=u'\u67e5\u627e\u8282\u70b9', name='button9',
              parent=self.panel1, pos=wx.Point(8, 464), size=wx.Size(75, 24),
              style=0)
        self.button9.Bind(wx.EVT_BUTTON, self.OnButton9Button,
              id=wxID_FRAME1BUTTON9)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(0, 424), size=wx.Size(104, 22),
              style=0, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.FileName=None
        self.LineNo_c=0

    def checkStatusRange(self, event):
        return event.GetDragStatus() != wx.SASH_STATUS_OUT_OF_RANGE

    def doLayout(self):
        wx.LayoutAlgorithm().LayoutWindow(self, self.panel1)
        self.panel1.Refresh()
        

    def adb_shell(self, cmd):
        cmd ='adb shell '+cmd
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return_code = p.poll()    
        while return_code is None:
            line = p.stdout.readline()
            return_code = p.poll()
            line = line.strip()
            if line:
                self.textReturn.AppendText(line+'\n')
        self.textReturn.AppendText('Done\n')

    def OnWxframe1Size(self, event):
        self.doLayout()

    def OnSashLayoutWindow1SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow1.SetDefaultSize(wx.Size(event.GetDragRect().width, 1000))
            self.doLayout()
        event.Skip()

    def OnSashLayoutWindow2SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow2.SetDefaultSize(wx.Size(event.GetDragRect().width, 1000))
            self.doLayout()
        event.Skip()

    def OnFrame1Size(self, event):
        self.doLayout()
        event.Skip()

        
    def OnSel(self, event):
        filename = self.genericDirCtrl1.GetFilePath()
        if os.path.isfile(filename):
            self.textEditor.LoadFile(filename) 
            self.FileName=filename
            self.SetTitle(('Notebook - %s') % filename)    
      
    def OnButton2Button(self, event):
        cmd = ''
        for i in range(0,self.textEditor.GetNumberOfLines()):
            cmd_c = self.textEditor.GetLineText(i)
            if cmd_c[0]<>'#':
                cmd = cmd + '&&' + cmd_c
        cmd = cmd[2:]
        self.adb_shell(cmd)
        event.Skip()
        
    def OnButton3Button(self, event):
        if self.FileName == None:
            return self.OnFileSaveasMenu(event)
        else:
            self.textEditor.SaveFile(self.FileName)
        event.Skip()

    def OnButton4Button(self, event):
        dlg = wx.FileDialog(self, "Save file as", ".", "", "*.*", wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                self.textEditor.SaveFile(filename) 
                self.FileName=filename
                self.SetTitle(('Notebook - %s') % filename)
        finally:
            dlg.Destroy()
        event.Skip()      

    def OnButton5Button(self, event):
        size_str = os.popen('adb shell wm size').read()
        device_str = os.popen('adb shell getprop ro.product.model').read()
        density_str = os.popen('adb shell wm density').read()
        self.textReturn.AppendText(device_str+'\n')
        self.textReturn.AppendText(size_str+'\n')
        self.textReturn.AppendText(density_str+'\n')
        event.Skip()

    def OnButton6Button(self, event):
        self.textReturn.Clear()
        event.Skip()

    def OnButton7Button(self, event):
        cmd = self.textEditor.GetStringSelection()
        self.textReturn.AppendText(cmd+'\n')
        if cmd[0]<>'#':
            self.adb_shell(cmd)
        event.Skip()

    def OnButton1Button(self, event):
        pos = self.textEditor.GetInsertionPoint()
        xy = self.textEditor.PositionToXY(pos)
        y = xy[1]
        lineno = self.textEditor.GetNumberOfLines()
        if self.LineNo_c < lineno:
            cmd = self.textEditor.GetLineText(y)
            self.textReturn.AppendText(cmd+'\n')
            if cmd[0]<>'#':
                self.adb_shell(cmd)
            y = y + 1
            self.LineNo_c = y
            pos = self.textEditor.XYToPosition(0, y)
            self.textEditor.SetInsertionPoint(pos)
        event.Skip()

    def OnTextEditorLeftDown(self, event):
        pos = self.textEditor.GetInsertionPoint()
        xy = self.textEditor.PositionToXY(pos)
        y = xy[1]
        self.LineNo_c = y
        event.Skip()

    def OnBitmapButton1Button(self, event):
        self.textEditor.Undo()
        event.Skip()

    def OnBitmapButton2Button(self, event):
        self.textEditor.Redo()
        event.Skip()

    def OnButton8Button(self, event):
        cmd ='adb shell uiautomator dump /mnt/sdcard/window_dump.xml'
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        des_path = os.getcwd()
        cmd = "adb pull /mnt/sdcard/window_dump.xml " + des_path
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.textReturn.AppendText(des_path+'\window_dump.xml\n') 
        event.Skip()
        
    def find_element(self, attrib, name):  
        des_path = os.getcwd()
        tree = ET.ElementTree(file=des_path + "\\window_dump.xml")  
        treeIter = tree.iter(tag="node")  
        for elem in treeIter:  
            if elem.attrib[attrib] == name:  
                bounds = elem.attrib["bounds"]
                self.textReturn.AppendText(name+': '+bounds+'\n') 
                coord = re.compile(r"\d+").findall(bounds)  
                Xpoint = (int(coord[2]) - int(coord[0])) / 2 + int(coord[0])  
                Ypoint = (int(coord[3]) - int(coord[1])) / 2 + int(coord[1])   
                return Xpoint, Ypoint
            
    def findElementByName(self, name):  
        pos = self.find_element("text", name) 
        if pos == None:
            pos = self.find_element("content-desc", name) 
        self.textReturn.AppendText(str(pos)+'\n')    
        return pos
                     
    def OnButton9Button(self, event):
        pos = self.findElementByName(self.textCtrl1.Value)  
        cmd = 'input tap ' + str(pos[0]) + ' ' + str(pos[1])
        self.textEditor.AppendText('#'+self.textCtrl1.Value+'\n')
        self.textEditor.AppendText(cmd+'\n')
        event.Skip()









        

