import pdfkit, json, time, sys
import qtmodern.styles
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from qtmodern import windows
from qtmodern import styles
from template import *
from dropdown import *
from results import summary


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/login.ui", self)
        self.setWindowIcon(QtGui.QIcon("static/logo.png"))
        self.setWindowTitle("Kühllastberechnung")
        self.username = "kkl"
        self.password = "t383vjc92"
        self.login_btn.clicked.connect(self.login)

    def login(self):
        if self.password_input.text() != self.password or self.username_input.text() != self.username:
            self.info_label.setText("Falsche Anmeldedaten!")
        else:
            print("Anmeldung erfolgreich!")
            self.info_label.setText("")
            config_window = Configuration()
            widget.addWidget(config_window)
            widget.setCurrentIndex(widget.currentIndex()+1)


class Configuration(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/configuration.ui", self)

        self.sonnenschutz_sued.addItems(SONNENSCHUTZ_LIST)
        self.sonnenschutz_sued.currentTextChanged.connect(self.sued_changed)

        self.sonnenschutz_suedost.addItems(SONNENSCHUTZ_LIST)
        self.sonnenschutz_suedost.currentTextChanged.connect(self.suedost_changed)

        self.sonnenschutz_suedwest.addItems(SONNENSCHUTZ_LIST)
        self.sonnenschutz_suedwest.currentTextChanged.connect(self.suedwest_changed)

        self.sonnenschutz_ost.addItems(SONNENSCHUTZ_LIST)
        self.sonnenschutz_ost.currentTextChanged.connect(self.ost_changed)

        self.sonnenschutz_nordost.addItems(SONNENSCHUTZ_LIST)
        self.sonnenschutz_nordost.currentTextChanged.connect(self.nordost_changed)

        self.sonnenschutz_nordwest.addItems(SONNENSCHUTZ_LIST)
        self.sonnenschutz_nordwest.currentTextChanged.connect(self.nordwest_changed)

        self.sonnenschutz_west.addItems(SONNENSCHUTZ_LIST)
        self.sonnenschutz_west.currentTextChanged.connect(self.west_changed)

        self.drop_dachflaechen.addItems(DACHFLAECHEN)
        self.drop_decke.addItems(DACH)
        self.drop_personen.addItems(PERSONEN)
        self.drop_leuchtmittel.addItems(LEUCHTMITTEL)
        self.drop_beleuchtung.addItems(BELEUCHTUNG)

        self.save_raum_btn.clicked.connect(self.save_raum)
        self.save_sonstiges_btn.clicked.connect(self.save_sonstiges)
        #self.save_as_pdf_btn.clicked.connect(self.print_to_pdf)

    #def print_to_pdf(self):
    #    with open("data.json", "w") as file:
    #        json.dump(summary, file)
    #    time.sleep(2)
    #    pdfkit.from_file("data.json", "data.pdf")

    def sued_changed(self, s):
        if s == SONNENSCHUTZ_LIST[0]:
            self.suedwm3.setText("=...W/m²")
            waermeeinfall["süd"]["kuehllast"] = 0
            self.kuehllast_sued.setText("0")
        else:
            self.suedwm3.setText("=" + str(waermeeinfall["süd"][s]) + " W/m²")
            if "," in self.flaeche_sued_input.text():
                input = self.flaeche_sued_input.text().replace(",", ".")
            else:
                input = self.flaeche_sued_input.text()
            waermeeinfall["süd"]["flaeche"] = float(input)
            waermeeinfall["süd"]["kuehllast"] = round(waermeeinfall["süd"][s] * waermeeinfall["süd"]["flaeche"], 2)
            if isinstance(waermeeinfall["süd"]["kuehllast"], float):
                export = str(waermeeinfall["süd"]["kuehllast"]).replace(".", ",")
            else:
                export = str(waermeeinfall["süd"]["kuehllast"])
            self.kuehllast_sued.setText(export)

    def suedost_changed(self, s):
        if s == SONNENSCHUTZ_LIST[0]:
            self.suedostwm3.setText("=...W/m²")
            waermeeinfall["süd-ost"]["kuehllast"] = 0
            self.kuehllast_sued_ost.setText("0")
        else:
            self.suedostwm3.setText("=" + str(waermeeinfall["süd-ost"][s]) + " W/m²")
            if "," in self.flaeche_suedost_input.text():
                input = self.flaeche_suedost_input.text().replace(",", ".")
            else:
                input = self.flaeche_suedost_input.text()
            waermeeinfall["süd-ost"]["flaeche"] = float(input)
            waermeeinfall["süd-ost"]["kuehllast"] = round(waermeeinfall["süd-ost"][s] * waermeeinfall["süd-ost"]["flaeche"], 2)
            if isinstance(waermeeinfall["süd-ost"]["kuehllast"], float):
                export = str(waermeeinfall["süd-ost"]["kuehllast"]).replace(".", ",")
            else:
                export = str(waermeeinfall["süd-ost"]["kuehllast"])
            self.kuehllast_sued_ost.setText(export)

    def suedwest_changed(self, s):
        if s == SONNENSCHUTZ_LIST[0]:
            self.suedwestwm3.setText("=...W/m²")
            waermeeinfall["süd-west"]["kuehllast"] = 0
            self.kuehllast_sued_west.setText("0")
        else:
            self.suedwestwm3.setText("=" + str(waermeeinfall["süd-west"][s]) + " W/m²")
            if "," in self.flaeche_suedwest_input.text():
                input = self.flaeche_suedwest_input.text().replace(",", ".")
            else:
                input = self.flaeche_suedwest_input.text()
            waermeeinfall["süd-west"]["flaeche"] = float(input)
            waermeeinfall["süd-west"]["kuehllast"] = round(waermeeinfall["süd-west"][s] * waermeeinfall["süd-west"]["flaeche"], 2)
            if isinstance(waermeeinfall["süd-west"]["kuehllast"], float):
                export = str(waermeeinfall["süd-west"]["kuehllast"]).replace(".", ",")
            else:
                export = str(waermeeinfall["süd-west"]["kuehllast"])
            self.kuehllast_sued_west.setText(export)

    def ost_changed(self, s):
        if s == SONNENSCHUTZ_LIST[0]:
            self.ostwm3.setText("=...W/m²")
            waermeeinfall["ost"]["kuehllast"] = 0
            self.kuehllast_ost.setText("0")
        else:
            self.ostwm3.setText("=" + str(waermeeinfall["ost"][s]) + " W/m²")
            if "," in self.flaeche_ost_input.text():
                input = self.flaeche_ost_input.text().replace(",", ".")
            else:
                input = self.flaeche_ost_input.text()
            waermeeinfall["ost"]["flaeche"] = float(input)
            waermeeinfall["ost"]["kuehllast"] = round(waermeeinfall["ost"][s] * waermeeinfall["ost"]["flaeche"], 2)
            if isinstance(waermeeinfall["ost"]["kuehllast"], float):
                export = str(waermeeinfall["ost"]["kuehllast"]).replace(".", ",")
            else:
                export = str(waermeeinfall["ost"]["kuehllast"])
            self.kuehllast_ost.setText(export)

    def nordost_changed(self, s): #nordostwm3, flaeche_nordost_input, kuehllast_nord_ost
        if s == SONNENSCHUTZ_LIST[0]:
            self.nordostwm3.setText("=...W/m²")
            waermeeinfall["nord-ost"]["kuehllast"] = 0
            self.kuehllast_nord_ost.setText("0")
        else:
            self.nordostwm3.setText("=" + str(waermeeinfall["nord-ost"][s]) + " W/m²")
            if "," in self.flaeche_nordost_input.text():
                input = self.flaeche_nordost_input.text().replace(",", ".")
            else:
                input = self.flaeche_nordost_input.text()
            waermeeinfall["nord-ost"]["flaeche"] = float(input)
            waermeeinfall["nord-ost"]["kuehllast"] = round(waermeeinfall["nord-ost"][s] * waermeeinfall["nord-ost"]["flaeche"], 2)
            if isinstance(waermeeinfall["nord-ost"]["kuehllast"], float):
                export = str(waermeeinfall["nord-ost"]["kuehllast"]).replace(".", ",")
            else:
                export = str(waermeeinfall["nord-ost"]["kuehllast"])
            self.kuehllast_nord_ost.setText(export)

    def nordwest_changed(self, s): #flaeche_nordwest_input, nordwestmw3, kuehllast_nord_west
        if s == SONNENSCHUTZ_LIST[0]:
            self.nordwestmw3.setText("=...W/m²")
            waermeeinfall["nord-west"]["kuehllast"] = 0
            self.kuehllast_nord_west.setText("0")
        else:
            self.nordwestmw3.setText("=" + str(waermeeinfall["nord-west"][s]) + " W/m²")
            if "," in self.flaeche_nordwest_input.text():
                input = self.flaeche_nordwest_input.text().replace(",", ".")
            else:
                input = self.flaeche_nordwest_input.text()
            waermeeinfall["nord-west"]["flaeche"] = float(input)
            waermeeinfall["nord-west"]["kuehllast"] = round(waermeeinfall["nord-west"][s] * waermeeinfall["nord-west"]["flaeche"], 2)
            if isinstance(waermeeinfall["nord-west"]["kuehllast"], float):
                export = str(waermeeinfall["nord-west"]["kuehllast"]).replace(".", ",")
            else:
                export = str(waermeeinfall["nord-west"]["kuehllast"])
            self.kuehllast_nord_west.setText(export)

    def west_changed(self, s): #flaeche_west_input, westmw3, kuehllast_west
        if s == SONNENSCHUTZ_LIST[0]:
            self.westmw3.setText("=...W/m²")
            waermeeinfall["west"]["kuehllast"] = 0
            self.kuehllast_west.setText("0")
        else:
            self.westmw3.setText("=" + str(waermeeinfall["west"][s]) + " W/m²")
            if "," in self.flaeche_west_input.text():
                input = self.flaeche_west_input.text().replace(",", ".")
            else:
                input = self.flaeche_west_input.text()
            waermeeinfall["west"]["flaeche"] = float(input)
            waermeeinfall["west"]["kuehllast"] = round(waermeeinfall["west"][s] * waermeeinfall["west"]["flaeche"], 2)
            if isinstance(waermeeinfall["west"]["kuehllast"], float):
                export = str(waermeeinfall["west"]["kuehllast"]).replace(".", ",")
            else:
                export = str(waermeeinfall["west"]["kuehllast"])
            self.kuehllast_west.setText(export)

    def confirm_kuehllast(self):
        pass

    def save_sonstiges(self):
        self.label_sonstiges.setText(self.lineEdit_sonstiges.text())
        save_string = self.lineEdit_sonstiges.text().replace(",", ".")
        summary["sonstigekuehllast"]["sonstkuehllast"] = float(save_string)
        self.lineEdit_sonstiges.setText("")
        print(summary)

    def save_raum(self):
        self.label_kommision.setText(self.lineEdit_kommision.text())
        self.label_ort.setText(self.lineEdit_ort.text())
        self.label_objekt.setText(self.lineEdit_objekt.text())
        self.label_raumbezeichnung.setText(self.lineEdit_raumbezeichnung.text())
        self.lineEdit_kommision.setText("")
        self.lineEdit_ort.setText("")
        self.lineEdit_objekt.setText("")
        self.lineEdit_raumbezeichnung.setText("")


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
window = MainWindow()
widget.addWidget(window)
qtmodern.styles.light(app)
mw = qtmodern.windows.ModernWindow(widget)
mw.show()
app.exec_()
