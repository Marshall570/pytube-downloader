from subprocess import check_call
from os import path
from platform import system
from tkinter import *


class Ui_App_Window(object):
    # from PyQt5 import QtCore, QtGui, QtWidgets
    
    def start_download(self):
        try:
            import youtube_dl
            from plyer import notification

            download_path = path.expanduser('~') + '/Downloads/'
            link = self.txt_link.text().strip()
            option = 0

            if self.rd_vid.isChecked():
                option = 1
            else:
                option = 2

            if link.find('&list') != -1:
                download_path += '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'
            else:
                download_path += '%(title)s/%(title)s.%(ext)s'

            if system().startswith('Win'):
                download_path.replace('/', '\\')

            if option == 1:
                download_options = {
                    'quiet': True,
                    'format': 'bestvideo+bestaudio',
                    'outtmpl': download_path,
                }
            else:
                download_options = {
                    'quiet': True,
                    'format': 'bestaudio',
                    'outtmpl': download_path,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192'
                    }],
                }

            notification.notify(
                app_name='PYTUBE',
                title='BAIXANDO ARQUIVOS...',
                message='Aguarde enquanto os arquivos estão sendo baixados.\nVocê será notificado ao término do download.',
                timeout=5
            )

            with youtube_dl.YoutubeDL(download_options) as downloader:
                downloader.download([link.strip()])

        except Exception as e:
            print(e)

        finally:
            notification.notify(
                app_name='PYTUBE',
                title='DOWNLOAD CONCLUÍDO COM SUCESSO!',
                message='Arquivos disponíveis na pasta de Downloads',
                timeout=5
            )

    def setupUi(self, App_Window):
        App_Window.setObjectName("App_Window")
        App_Window.resize(650, 200)
        App_Window.setWindowTitle("PYTUBE")
        icon = QtGui.QIcon.fromTheme("youtube")
        App_Window.setWindowIcon(icon)
        App_Window.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(App_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_link = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lbl_link.sizePolicy().hasHeightForWidth())
        self.lbl_link.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_link.setFont(font)
        self.lbl_link.setText("LINK DO VÍDEO/PLAYLIST:")
        self.lbl_link.setObjectName("lbl_link")
        self.verticalLayout.addWidget(self.lbl_link)
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_link.setFont(font)
        self.txt_link.setText("")
        self.txt_link.setObjectName("txt_link")
        self.verticalLayout.addWidget(self.txt_link)
        self.gp_option = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gp_option.sizePolicy().hasHeightForWidth())
        self.gp_option.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gp_option.setFont(font)
        self.gp_option.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gp_option.setTitle("OPÇÃO DE DOWNLOAD")
        self.gp_option.setAlignment(QtCore.Qt.AlignCenter)
        self.gp_option.setObjectName("gp_option")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gp_option)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rd_vid = QtWidgets.QRadioButton(self.gp_option)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rd_vid.setFont(font)
        self.rd_vid.setText("Vídeo + Áudio")
        self.rd_vid.setChecked(True)
        self.rd_vid.setObjectName("rd_vid")
        self.horizontalLayout.addWidget(self.rd_vid)
        self.rd_audio = QtWidgets.QRadioButton(self.gp_option)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rd_audio.setFont(font)
        self.rd_audio.setText("Apenas Áudio")
        self.rd_audio.setObjectName("rd_audio")
        self.horizontalLayout.addWidget(self.rd_audio)
        self.verticalLayout.addWidget(self.gp_option)
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_download.setFont(font)
        self.btn_download.setText("BAIXAR ARQUIVOS")
        self.btn_download.setObjectName("btn_download")
        self.verticalLayout.addWidget(self.btn_download)
        App_Window.setCentralWidget(self.centralwidget)

        self.btn_download.clicked.connect(self.start_download)

        QtCore.QMetaObject.connectSlotsByName(App_Window)
        App_Window.setTabOrder(self.txt_link, self.rd_vid)
        App_Window.setTabOrder(self.rd_vid, self.rd_audio)
        App_Window.setTabOrder(self.rd_audio, self.btn_download)


if __name__ == "__main__":
    import sys
    check_call(
        [
            sys.executable,
            '-m',
            'pip',
            'install',
            'youtube-dl',
            'pyqt5',
            'plyer',
            '-q'
        ]
    )
    from PyQt5 import QtCore, QtGui, QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    App_Window = QtWidgets.QMainWindow()
    ui = Ui_App_Window()
    ui.setupUi(App_Window)
    App_Window.show()
    sys.exit(app.exec_())
