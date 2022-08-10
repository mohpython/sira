import sys
from  PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui

class FenPrincipale(QMainWindow):
    def __init__(self) -> None:
        super(FenPrincipale, self).__init__()
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.navigateur=QWebEngineView()
        self.navigateur.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.navigateur)
        self.showMaximized()


        #navbar
        navbar=QToolBar()
        self.addToolBar(navbar)

        
        accueil_btn=QAction('Accueil',self)
        accueil_btn.triggered.connect(self.Url_accueil)
        navbar.addAction(accueil_btn)

        retour_btn=QAction('Précédent',self)
        retour_btn.triggered.connect(self.navigateur.back)
        navbar.addAction(retour_btn)

        actualiser_btn=QAction('Actualiser',self)
        actualiser_btn.triggered.connect(self.navigateur.reload)
        navbar.addAction(actualiser_btn)

        avancer_btn=QAction('Suivant',self)
        avancer_btn.triggered.connect(self.navigateur.forward)
        navbar.addAction(avancer_btn)

        self.Url_bar=QLineEdit()
        self.Url_bar.returnPressed.connect(self.Navigation)
        navbar.addWidget(self.Url_bar)

        self.navigateur.urlChanged.connect(self.update_url)

        

    def Url_accueil(self):
        self.navigateur.setUrl(QUrl('http://google.com'))

    def Navigation(self):
        url=self.Url_bar.text()
        self.navigateur.setUrl(QUrl(url))

    def update_url(self, url):
        self.Url_bar.setText(url.toString())


app=QApplication(sys.argv)
QApplication.setApplicationName('Sira')

fenetre=FenPrincipale()
app.exec()