# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys, pafy, os

# Variables ==================================================================================

p = None
name = None
total_size = None
checker = None
last = None
winsize = None
Form = None
Form1 = None
ui = None

# General Defines/Functions =================================================================

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def get_streams(pafy_obj):
    return [stream for stream in pafy_obj.streams]

def get_audiostreams(pafy_obj):
    return [s for s in pafy_obj.audiostreams]

def show_links():
    global Form
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    return True

def show_about():
    global Form1
    Form1 = QtGui.QWidget()
    ui = Ui_About()
    ui.setupUi(Form1)
    Form1.show()
    return True

def show_help():
    global Form1
    Form1 = QtGui.QWidget()
    ui = Ui_Help()
    ui.setupUi(Form1)
    Form1.show()
    return True

# ============================================================================================

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))

        if ui.audio_list is not None:
            size = 98 + len(ui.audio_list) * 58 + 10
            stats_pos = 40 + len(ui.audio_list)*58 + 10
            self.worklist = ui.audio_list
        else:
            size = 98 + len(ui.stream_list) * 58 + 10
            stats_pos = 40 + len(ui.stream_list)*58 + 10
            self.worklist = ui.stream_list
            
        Form.resize(538, size)
        self.duration_txt = QtGui.QLabel(Form)
        self.duration_txt.setGeometry(QtCore.QRect(30, 100, 61, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.duration_txt.setFont(font)
        self.duration_txt.setObjectName(_fromUtf8("duration_txt"))
        self.duration = QtGui.QLabel(Form)
        self.duration.setGeometry(QtCore.QRect(120, 100, 81, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.duration.setFont(font)
        self.duration.setObjectName(_fromUtf8("duration"))
        self.url_txt = QtGui.QLabel(Form)
        self.url_txt.setGeometry(QtCore.QRect(30, 20, 41, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.url_txt.setFont(font)
        self.url_txt.setObjectName(_fromUtf8("url_txt"))
        self.url = QtGui.QLabel(Form)
        self.url.setGeometry(QtCore.QRect(120, 20, 411, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.url.setFont(font)
        self.url.setObjectName(_fromUtf8("url"))
        self.title_txt = QtGui.QLabel(Form)
        self.title_txt.setGeometry(QtCore.QRect(30, 60, 41, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_txt.setFont(font)
        self.title_txt.setObjectName(_fromUtf8("title_txt"))
        self.title = QtGui.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(120, 60, 411, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.sep_duration = QtGui.QLabel(Form)
        self.sep_duration.setGeometry(QtCore.QRect(100, 100, 16, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sep_duration.setFont(font)
        self.sep_duration.setObjectName(_fromUtf8("sep_duration"))
        self.sep_title = QtGui.QLabel(Form)
        self.sep_title.setGeometry(QtCore.QRect(100, 60, 16, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sep_title.setFont(font)
        self.sep_title.setObjectName(_fromUtf8("sep_title"))
        self.sep_url = QtGui.QLabel(Form)
        self.sep_url.setGeometry(QtCore.QRect(100, 20, 16, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sep_url.setFont(font)
        self.sep_url.setObjectName(_fromUtf8("sep_url"))
        self.stats_txt = QtGui.QLabel(Form)
        self.stats_txt.setGeometry(QtCore.QRect(30, stats_pos, 61, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stats_txt.setFont(font)

        self.stats_txt.setObjectName(_fromUtf8("stats_txt"))
        self.stats = QtGui.QLabel(Form)
        self.stats.setGeometry(QtCore.QRect(120, stats_pos, 171, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stats.setFont(font)
        self.stats.setObjectName(_fromUtf8("stats"))
        self.sep_down = QtGui.QLabel(Form)
        self.sep_down.setGeometry(QtCore.QRect(100, stats_pos, 16, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sep_down.setFont(font)
        self.sep_down.setObjectName(_fromUtf8("sep_down"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Downloads", None))
        self.duration_txt.setText(_translate("Form", "Duration", None))
        self.duration.setText(_translate("Form", ui.video.duration, None))
        self.url_txt.setText(_translate("Form", "Url", None))
        self.url.setText(_translate("Form", ui.link.replace('https://', ''), None))
        self.title_txt.setText(_translate("Form", "Title", None))
        self.title.setText(_translate("Form", ui.video.title, None))
        self.sep_duration.setText(_translate("Form", ":", None))
        self.sep_title.setText(_translate("Form", ":", None))
        self.sep_url.setText(_translate("Form", ":", None))
        
        self.SetUpDownload(Form)
        
    def Download(self, Form, i):
        self.worklist[i].download(ui.fn+'.'+self.worklist[i].extension, quiet=True)
        
        self.stats.setText(_translate("Form", "Downloaded.", None))
        self.sep_down.setText(_translate("Form", ":", None))
        self.stats_txt.setText(_translate("Form", "Stats", None))
        return True

    def SetUpDownload(self, Form):
        Y = 140
        i = 0
        for x in self.worklist:
            self.stats_txt_2 = QtGui.QLabel(Form)
            self.stats_txt_2.setGeometry(QtCore.QRect(60, Y, 61, 30))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.stats_txt_2.setFont(font)
            self.stats_txt_2.setObjectName(_fromUtf8("stats_txt_2"))
            self.sep_down_2 = QtGui.QLabel(Form)
            self.sep_down_2.setGeometry(QtCore.QRect(120, Y, 16, 30))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.sep_down_2.setFont(font)
            self.sep_down_2.setObjectName(_fromUtf8("sep_down_2"))
            
            self.stats_2 = QtGui.QLabel(Form)
            self.stats_2.setGeometry(QtCore.QRect(140, Y, 171, 30))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.stats_2.setFont(font)
            self.stats_2.setObjectName(_fromUtf8("stats_2"))

            self.sz = QtGui.QLabel(Form)
            self.sz.setGeometry(QtCore.QRect(230, Y, 151, 30))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.sz.setFont(font)
            self.sz.setObjectName(_fromUtf8("stats_2"))

            down_b = QtGui.QPushButton('Download', Form)
            font = QtGui.QFont()
            font.setBold(True)
            down_b.setFont(font)
            down_b.setObjectName(_fromUtf8("down_button_"+str(i)))
            down_b.clicked.connect(lambda state, a=i: self.Download(Form, a))
            down_b.setGeometry(QtCore.QRect(420, Y, 81, 30))

            self.stats_txt_2.setText(_translate("Form", str(x.extension), None))
            self.sep_down_2.setText(_translate("Form", ":", None))
            if x.resolution == '0x0':
                self.stats_2.setText(_translate("Form", str(x.bitrate), None))
            else:
                self.stats_2.setText(_translate("Form", str(x.resolution), None))
            self.sz.setText(_translate("Form", 'Size: '+str(x.get_filesize())+' Bit', None))
            
            Y += 40
            i += 1

# ====================================================================================================

class Ui_About(object):
    def paypal(self, event):
        os.popen('start "" "www.paypal.me/m0ng1"')
        # End
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(532, 243)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.mousePressEvent = self.paypal
        self.label_4.setObjectName(_fromUtf8("label_4"))
        
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(230, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "About", None))
        self.label.setText(_translate("Form", "Developed By Mongi", None))
        self.label_2.setText(_translate("Form", "Donation  :", None))
        self.label_3.setText(_translate("Form", "Contact    : ", None))
        self.label_4.setText(_translate("Form", "Paypal", None))
        self.label_5.setText(_translate("Form", "saidanemongi@gmail.com", None))

# ====================================================================================================

class Ui_Help(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(550, 285)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 170, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(250, 170, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(250, 200, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Help", None))
        self.label.setText(_translate("Form", "You have to select a name for the Song/Video that you are willing to download", None))
        self.label_2.setText(_translate("Form", "Then you would have to write the video\'s url.", None))
        self.label_3.setText(_translate("Form", "You would be asked to select the quality that you are willing to download", None))
        self.label_4.setText(_translate("Form", "By clicking on \'Download\' button, The download would start", None))
        self.label_5.setText(_translate("Form", "You would be informed whenever the download is finished", None))
        self.label_6.setText(_translate("Form", "The download speed depends on :", None))
        self.label_7.setText(_translate("Form", "- Your network speed", None))
        self.label_8.setText(_translate("Form", "- Size of the file (Depends on Quality)", None))

# ====================================================================================================

class Ui_MainWindow(object):
    def Audio_Button(self, url, fname):
        if "watch?v=" in url:
            self.video = pafy.new(url)
            self.link = url
            self.fn = fname
        
            self.audio_list = get_audiostreams(self.video)
            self.stream_list = None
            show_links()
        # End

    def Video_Button(self, url, fname):
        if "watch?v=" in url:
            self.video = pafy.new(url)
            self.link = url
            self.fn = fname
        
            self.stream_list = get_streams(self.video)
            self.audio_list = None
            show_links()
        # End
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(663, 404)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.url_txt = QtGui.QLabel(self.centralwidget)
        self.url_txt.setGeometry(QtCore.QRect(50, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.url_txt.setFont(font)
        self.url_txt.setObjectName(_fromUtf8("url_txt"))
        self.Title = QtGui.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(250, 20, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName(_fromUtf8("Title"))
        self.audio_get = QtGui.QPushButton(self.centralwidget)
        self.audio_get.setGeometry(QtCore.QRect(360, 280, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.audio_get.setFont(font)
        self.audio_get.clicked.connect(lambda: self.Audio_Button(str(self.url.text()), str(self.file_name.text())))
        self.audio_get.setObjectName(_fromUtf8("audio_get"))
        self.url = QtGui.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(190, 100, 421, 31))
        self.url.setObjectName(_fromUtf8("url"))
        self.file_name = QtGui.QLineEdit(self.centralwidget)
        self.file_name.setGeometry(QtCore.QRect(190, 170, 161, 31))
        self.file_name.setMaxLength(255)
        self.file_name.setObjectName(_fromUtf8("file_name"))
        self.filename_txt = QtGui.QLabel(self.centralwidget)
        self.filename_txt.setGeometry(QtCore.QRect(50, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.filename_txt.setFont(font)
        self.filename_txt.setObjectName(_fromUtf8("filename_txt"))
        self.sep_url = QtGui.QLabel(self.centralwidget)
        self.sep_url.setGeometry(QtCore.QRect(160, 100, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.sep_url.setFont(font)
        self.sep_url.setObjectName(_fromUtf8("sep_url"))
        self.sep_fn = QtGui.QLabel(self.centralwidget)
        self.sep_fn.setGeometry(QtCore.QRect(160, 170, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.sep_fn.setFont(font)
        self.sep_fn.setObjectName(_fromUtf8("sep_fn"))
        self.video_get = QtGui.QPushButton(self.centralwidget)
        self.video_get.setGeometry(QtCore.QRect(220, 280, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.video_get.setFont(font)
        self.video_get.clicked.connect(lambda: self.Video_Button(str(self.url.text()), str(self.file_name.text())))
        self.video_get.setObjectName(_fromUtf8("video_get"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout.triggered.connect(lambda: show_about())
        
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionHelp.triggered.connect(lambda: show_help())
        
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader", None))
        self.url_txt.setText(_translate("MainWindow", "Youtube Url", None))
        self.Title.setText(_translate("MainWindow", "Youtube Downloader", None))
        self.audio_get.setText(_translate("MainWindow", "Audio", None))
        self.filename_txt.setText(_translate("MainWindow", "File Name   ", None))
        self.sep_url.setText(_translate("MainWindow", ":", None))
        self.sep_fn.setText(_translate("MainWindow", ":", None))
        self.video_get.setText(_translate("MainWindow", "Video", None))
        self.menuAbout.setTitle(_translate("MainWindow", "?", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))

# ====================================================================================================

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

