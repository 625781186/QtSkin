# -*- coding=utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import win32gui
import win32con
import win32api
import ctypes
from PyQt5.Qt import Qt

WINDOWED = win32con.WS_OVERLAPPEDWINDOW | win32con.WS_CAPTION | win32con.WS_SYSMENU | win32con.WS_MINIMIZEBOX | \
        win32con.WS_MAXIMIZEBOX | win32con.WS_THICKFRAME | win32con.WS_CLIPCHILDREN | win32con.WS_SYSMENU
BORDERLESS = win32con.WS_POPUP | win32con.WS_CAPTION | win32con.WS_SYSMENU | win32con.WS_MINIMIZEBOX | \
        win32con.WS_MAXIMIZEBOX | win32con.WS_THICKFRAME | win32con.WS_CLIPCHILDREN

class MARGINS(ctypes.Structure):
  _fields_ = [("cxLeftWidth", ctypes.c_int),
              ("cxRightWidth", ctypes.c_int),
              ("cyTopHeight", ctypes.c_int),
              ("cyBottomHeight", ctypes.c_int)
             ]


class iWinWidget(QWidget):
    def __init__(self):
        super(iWinWidget, self).__init__()
        self._borderless = False
        self._visible = False
        self._resizable = True
        #hInstance = win32gui.GetModuleHandle(None)
        hbrBackground = win32gui.CreateSolidBrush(win32api.RGB(255, 255, 255))
        
        wndCls = win32gui.WNDCLASS()
        wndCls.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wndCls.hbrBackground = hbrBackground
        #wndCls.hCursor = win32gui.LoadCursor(hInstance, win32con.IDC_ARROW) 
        wndCls.lpszClassName = "iWinWidget"
        wndCls.lpfnWndProc = self.wndProc  

        wndClassAtom = win32gui.RegisterClass(wndCls)
        self.hwnd = win32gui.CreateWindow(  
                    wndClassAtom, None, WINDOWED,
                    win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,  
                    win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,  
                    0, 0, 0, None)
        
        win32gui.SetWindowLong(self.winId(), win32con.GWL_STYLE, 
                               win32con.WS_CHILD | win32con.WS_CLIPCHILDREN | 
                               win32con.WS_CLIPSIBLINGS)

        #self.window().setProperty("_q_embedded_native_parent_handle", self.hwnd)
        win32gui.SetParent(self.winId(), self.hwnd)
        #self.setParent(QWidget.find(self.hwnd))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.toggleBorderless()
        
    def wndProc(self, hwnd, msg, wParam, lParam):

        if msg == win32con.WM_NCCALCSIZE:
            if self._borderless:
                return 0
        elif msg == win32con.WM_SYSCOMMAND:
            if wParam == win32con.SC_KEYMENU:
                left, top, right, bottom = win32gui.GetWindowRect(hwnd)
                win32gui.TrackPopupMenu(win32gui.GetSystemMenu(hwnd, False ), 
                                        win32con.TPM_TOPALIGN | win32con.TPM_LEFTALIGN, 
                                        left + 5, top + 5, 0, hwnd, None)
        elif msg == win32con.WM_SETFOCUS:
            print("OnFocus")
        elif msg == win32con.WM_KILLFOCUS:
            print("OnLoseFocus")
        elif msg == win32con.WM_DESTROY:
            win32gui.PostQuitMessage(0)
        elif msg == win32con.WM_NCHITTEST:
            if self._borderless:
                if self._resizable:
                    borderWidth = 5
                    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
                    x = win32api.LOWORD(lParam)
                    y = win32api.HIWORD(lParam)
        
                    # bottom left corner
                    if x >= left and x < left + borderWidth and \
                        y < bottom and y >= bottom - borderWidth:       
                        return win32con.HTBOTTOMLEFT
                          
                    #bottom right corner
                    elif x < right and x >= right - borderWidth and \
                        y < bottom and y >= bottom - borderWidth:
                        return win32con.HTBOTTOMRIGHT

                    # top left corner
                    elif x >= left and x < left + borderWidth and \
                        y >= top and y < top + borderWidth:
                        return win32con.HTTOPLEFT

                    # top right corner
                    elif x < right and x >= right - borderWidth and \
                      y >= top and y < top + borderWidth:
                        return win32con.HTTOPRIGHT

                    # left border
                    elif x >= left and x < left + borderWidth:
                        return win32con.HTLEFT
                    
                    # right border
                    elif x < right and x >= right - borderWidth:
                        return win32con.HTRIGHT
                    
                    # bottom border
                    elif y < bottom and y >= bottom - borderWidth:
                        return win32con.HTBOTTOM

                    # top border
                    elif y >= top and y < top + borderWidth:
                        return win32con.HTTOP     
                return win32con.HTCAPTION
            
        elif msg == win32con.WM_SIZE:
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            wp = win32gui.GetWindowPlacement(hwnd)
            print(left, top, right-left, bottom-top)
            if wp[1] == win32con.SW_MAXIMIZE:
                self.setGeometry(0, 0, right - left, bottom - top)
            else:
                self.setGeometry(8, 8, right - left - 16, bottom - top - 16)
                #self.setGeometry(0, 0, right - left, bottom - top)
        '''
        elif msg == win32con.WM_GETMINMAXINFO:
            #print("WM_GETMINMAXINFO")
            
              MINMAXINFO* minMaxInfo = ( MINMAXINFO* )lParam;
              if ( window->minimumSize.required ) {
                minMaxInfo->ptMinTrackSize.x = window->getMinimumWidth();;
                minMaxInfo->ptMinTrackSize.y = window->getMinimumHeight();
              }
        
              if ( window->maximumSize.required ) {
                minMaxInfo->ptMaxTrackSize.x = window->getMaximumWidth();
                minMaxInfo->ptMaxTrackSize.y = window->getMaximumHeight();
              }
            
            return 0
        '''
        return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)
     
    def show(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)
        QWidget.show(self)
        self._visible = True
    
    def hide(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_HIDE)
        QWidget.hide(self)
        self._visible = False
        
    def toggleBorderless(self):
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE, BORDERLESS)
        self._borderless = not self._borderless
        if self._borderless:
            margins = MARGINS(1, 1, 1, 1)
            ctypes.windll.dwmapi.DwmExtendFrameIntoClientArea(self.hwnd, ctypes.byref(margins))
        win32gui.SetWindowPos(self.hwnd, 0, 0, 0, 0, 0,
                              win32con.SWP_FRAMECHANGED |
                              win32con.SWP_NOMOVE |
                              win32con.SWP_NOSIZE)
        if self._visible: self.show()

if __name__ == '__main__':
    app = QApplication([])    
    win = iWinWidget()
    win.show()
    app.exec()