import sys
from disenno_mazmorra import Ui_MainWindow
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QHBoxLayout, QPushButton)
from PyQt6.QtCore import (QTimer, Qt)
import random
import time
from threading import Event

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._disableButton1()
        self._styleSheetButton()
        self._inicio()
        self.show()
        # Variables para usar el boton jugar
        self.estaNorte = False
        self.estaSur = False
        self.estaEste = False
        self.estaOeste = False
        # Variables para saber si una sala ha sido ganada
        self.norte = False
        self.sur = False
        self.este = False
        self.oeste = False

    def _styleSheetButton(self):
        
        self.ui.centralwidget.setStyleSheet("background-color : rgb(160, 227, 198)")
        self.ui.frame.setStyleSheet("background-color : rgb(141, 198, 174 );""border: 1px solid black;"
                             "border-radius: 10px;")
        self.ui.frame_2.setStyleSheet("background-color : rgb(141, 198, 174 );""border: 1px solid black;"
                             "border-radius: 10px;")
        self.ui.label.setStyleSheet("background-color : rgb(160, 227, 198);")
        self.ui.textEdit.setStyleSheet("background-color : rgb(160, 227, 198)")
        self.ui.radioButton.setStyleSheet("background-color : rgb(160, 227, 198);""border: 0px solid black;""border-radius: 7px;""border: 1px solid black;")
        self.ui.radioButton_2.setStyleSheet("background-color : rgb(160, 227, 198);""border: 0px solid black;""border-radius: 7px;""border: 1px solid black;")
        self.ui.radioButton_3.setStyleSheet("background-color : rgb(160, 227, 198);""border: 0px solid black;""border-radius: 7px;""border: 1px solid black;")
        self.ui.radioButton_4.setStyleSheet("background-color : rgb(160, 227, 198);""border: 0px solid black;""border-radius: 7px;""border: 1px solid black;")
        self.ui.pushButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(159, 199, 182);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(186, 236, 233);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             )
        self.ui.pushButton_2.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(159, 199, 182);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(186, 236, 233);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             )
        self.ui.pushButton_3.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(159, 199, 182);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(186, 236, 233);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             )
        self.ui.pushButton_4.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(159, 199, 182);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(186, 236, 233);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             )
        self.ui.pushButton_5.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(159, 199, 182);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(186, 236, 233);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             )
        self.ui.pushButton_6.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(159, 199, 182);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(186, 236, 233);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             )
        self.ui.pushButton_7.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(159, 199, 182);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(186, 236, 233);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             )

    def _disableButton1(self):
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton_2.setDisabled(True)
        self.ui.pushButton_4.setDisabled(True)
        self.ui.pushButton_5.setDisabled(True)
        self.ui.pushButton_6.setDisabled(True)
        self.ui.pushButton_3.setDisabled(False)
        self.ui.pushButton_7.setDisabled(False)

    def _pulsarJugar(self):
        if(self.estaNorte):
            self._atacar()
        elif(self.estaEste):
            self._tesoro()
        elif(self.estaSur):
            self._comprobarSur()
        elif(self.estaOeste):
            self._comprobarOeste()
        else:
            self._jugar()

    def _pulsarSalir(self):
        if (self.estaNorte or self.estaSur or self.estaEste or self.estaOeste):
            self.estaNorte = False;
            self.estaSur = False;
            self.estaEste = False;
            self.estaOeste = False;
            self._salirSala()
        else:
            self.close()

    def _inicio(self):
        self.ui.radioButton.setDisabled(True)
        self.ui.radioButton_2.setDisabled(True)
        self.ui.radioButton_3.setDisabled(True)
        self.ui.radioButton_4.setDisabled(True)
        self.ui.label.setText("Hola, debe elegir si desea jugar o salir")
        self.ui.pushButton_3.clicked.connect(self._pulsarJugar)
        self.ui.pushButton_7.clicked.connect(self._pulsarSalir)
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionAyuda.triggered.connect(self._botonAyuda)

    def _botonAyuda(self):

        dlg = QDialog(self)
        dlg.setWindowTitle("Ayuda")
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setText("Es un juego de cuatro salas, en cada sala tendrás un reto diferente, \nconsigue ganar todas las salas para ganar el juego.")
        self.layout.addWidget(self.label)
        dlg.setLayout(self.layout)
        dlg.exec()

    def _jugar(self):
        if (not self.sur):
            self.ui.pushButton.setDisabled(False)
        else:
            self.ui.pushButton.setDisabled(True)
        if (not self.este):
            self.ui.pushButton_2.setDisabled(False)
        else:
            self.ui.pushButton_2.setDisabled(True)
        if (not self.oeste):
            self.ui.pushButton_6.setDisabled(False)
        else:
            self.ui.pushButton_6.setDisabled(True)
        if (not self.norte):
            self.ui.pushButton_5.setDisabled(False)
        else:
            self.ui.pushButton_5.setDisabled(True)
        self.ui.pushButton_4.setDisabled(False)
        self.ui.pushButton_5.clicked.connect(self._salaNorte)
        self.ui.pushButton_2.clicked.connect(self._salaEste)
        self.ui.pushButton.clicked.connect(self._salaSur)
        self.ui.pushButton_6.clicked.connect(self._salaOeste)
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_7.setDisabled(True)

    def _salirSala(self):
        self._jugar()
        self.ui.radioButton.setDisabled(True)
        self.ui.radioButton_2.setDisabled(True)
        self.ui.radioButton_3.setDisabled(True)
        self.ui.radioButton_4.setDisabled(True)
        if(self.norte and self.sur and self.este and self.oeste):
            self.dlg = QDialog(self)
            self.dlg.setWindowTitle("Ganaste")
            self.layout3 = QHBoxLayout()
            self.botonJugar = QPushButton("Volver a jugar")
            self.botonSalir = QPushButton("Salir")
            self.layout3.addWidget(self.botonSalir)
            self.layout3.addWidget(self.botonJugar)
            self.botonJugar.clicked.connect(self._volverJugar)
            self.botonSalir.clicked.connect(self.close)
            self.layout2 = QVBoxLayout()
            self.label2 = QLabel()
            self.label2.setText("Enhorabuena, has logrado ganar las cuatro salas!!!!")
            self.layout2.addWidget(self.label2)
            self.layout2.addLayout(self.layout3)
            self.dlg.setLayout(self.layout2)
            self.dlg.exec()

    def _volverJugar(self):
        self.close()
        self.__init__()
        self.dlg.close()
    
    def _volverJugar2(self):
        self.close()
        self.__init__()
        self.dlg2.close()

    def _activarRadio(self):
        self.ui.radioButton.setDisabled(False)
        self.ui.radioButton_2.setDisabled(False)
        self.ui.radioButton_3.setDisabled(False)
        self.ui.radioButton_4.setDisabled(False)

    def _atacar(self):
        self.ataque = random.randint(0, 100)
        self.cadena2 = "Tu ataque ha sido de: "
        self.cadena2 += str(self.ataque)
        self.ui.textEdit.setText(self.cadena2)
        if (self.ataque > 60):
            self.cadena2 += "\nHURRAAAAA, Ganaste al gran dragón"
            self.ui.textEdit.setText(self.cadena2)
            self._salaNorteGanada()
            self._salirSala()
            self.estaNorte = False
        else:
            self._disableButton1()
            enemigo = random.randint(0, 100)
            self.cadena = "El poder de su ataque ha sido: "
            self.cadena += str(enemigo)
            self.ui.label.setText(self.cadena)
            if (enemigo >= 90):
                self.cadena2 = "\nHas muerto, inténtalo de nuevo"
                self.ui.textEdit.setText(self.cadena2)
                self._salirSala()
                self.estaNorte = False
                self.dlg2 = QDialog(self)
                self.dlg2.setWindowTitle("Perdiste")
                self.layout3 = QHBoxLayout()
                self.botonJugar = QPushButton("Volver a jugar")
                self.botonSalir = QPushButton("Salir")
                self.layout3.addWidget(self.botonSalir)
                self.layout3.addWidget(self.botonJugar)
                self.botonJugar.clicked.connect(self._volverJugar2)
                self.botonSalir.clicked.connect(self.close)
                self.layout2 = QVBoxLayout()
                self.label2 = QLabel()
                self.label2.setText("Lo siento, has muerto")
                self.layout2.addWidget(self.label2)
                self.layout2.addLayout(self.layout3)
                self.dlg2.setLayout(self.layout2)
                self.dlg2.exec()
            else:
                self.cadena2 += "\n¿Quieres defenderte?"
                self.ui.textEdit.setText(self.cadena2)
    
    def _salaNorteGanada(self):
        self.norte = True
        self.ui.pushButton_5.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(109, 237, 229);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(103, 147, 147);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "text-decoration:line-through;"
                             "}"
                             )
    
    def _salaEsteGanada(self):
        self.este = True
        self.ui.pushButton_2.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(109, 237, 229);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(103, 147, 147);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "text-decoration:line-through;"
                             "}"
                             )

    def _salaSurGanada(self):
        self.sur = True
        self.ui.pushButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(109, 237, 229);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(103, 147, 147);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "text-decoration:line-through;"
                             "}"
                             )
    
    def _salaOesteGanada(self):
        self.oeste = True
        self.ui.pushButton_6.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(109, 237, 229);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(5, 12, 46);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "}"
                             "QPushButton::disabled"
                             "{"
                             "background-color : rgb(103, 147, 147);"
                             "border: 1px solid black;"
                             "border-radius: 10px;"
                             "text-decoration:line-through;"
                             "}"
                             )

    def _salaNorte(self):
        self.ui.label.setText("")
        self.ui.textEdit.setText("")
        self._disableButton1()
        self.estaNorte = True
        self.ui.pushButton_7.clicked.connect(self._salirSala)
        self.ataque = 0
        self.cadena = ""
        self.cadena2 = ""
        self.cadena += "Un dragón gigante esta custodiando la sala!!!, CUIDADO TE ATACAAAA!!"
        self.ui.label.setText(self.cadena)
        enemigo = random.randint(0, 100)
        self.cadena += "\nEl poder de su ataque ha sido: "
        self.cadena += str(enemigo)
        self.ui.label.setText(self.cadena)
        if (enemigo >= 90):
            self.cadena2 = "\nHas muerto, inténtalo de nuevo"
            self.ui.textEdit.setText(self.cadena2)
            self._salirSala()
            self.estaNorte = False
        else:
            self.cadena2 = "\n¿Quieres defenderte?"
            self.ui.textEdit.setText(self.cadena2)

    def _tesoro(self):
        self.numero = random.randint(0, 100)
        self.cadena2 = "Has sacado: "
        self.cadena2 += str(self.numero)
        self.ui.textEdit.setText(self.cadena2)
        self.timer = QTimer()
        self.timer.timeout.connect(self._activarTesoro)
        if self.numero > 63:
            self.cadena2 += "\nLograste abrir el cofre, ¡Enhorabuena!"
            self.ui.textEdit.setText(self.cadena2)
            self._salaEsteGanada()
            self._salirSala()
            self.estaEste = False
            if(self.timer.isActive):
                self.timer.stop()
        else:
            self.cadena2 += "\nLo siento, no conseguiste abrir el cofre"
            self.cadena2 += "\nDebe esperar 20 segundos para volver a intentarlo"
            self.ui.textEdit.setText(self.cadena2)
            self._disableButton1()
            self.ui.pushButton_3.setDisabled(True)
            self.ui.pushButton_7.setDisabled(True)
            self.timer.start(20000)
            

    def _activarTesoro(self):
        self.ui.pushButton_3.setDisabled(False)
        self.ui.pushButton_7.setDisabled(False)

    def _salaEste(self):
        self.ui.label.setText("")
        self.ui.textEdit.setText("")
        self._disableButton1()
        self.estaEste = True
        self.cadena = "¡Que sorpresa!, un cofre dorado"
        self.cadena += "\nPara abrirlo debes sacar más de 63."
        self.ui.label.setText(self.cadena)
    

    def _salaSur(self):
        self.ui.label.setText("")
        self.ui.textEdit.setText("")
        self._disableButton1()
        self._activarRadio()
        self.estaSur = True
        self.cadena = "Buenas apuesto caballero, le apuesto tres dirhams a que no puede resolver este acertijo:"
        self.ui.label.setText(self.cadena)
        self.acertijo = ["Hay algo que, aunque te pertenezca, la gente siempre lo utiliza más que tú. ¿Qué es?",
                "Crezco a pesar de no estar vivo. No tengo pulmones, pero para vivir necesito el aire. El agua, aunque no tenga boca, me mata. ¿Qué soy?",
                "Estando roto es más útil que sin romperse. ¿Qué es?",
                "Aparato que vibra y gira, te metes en la boca unas 3 veces al día y mide unos 15 cm. ¿Qué es?",
                "Las personas siempre duermen menos en un mes del año. ¿Cuál es este mes?",
                "Estoy en todo pese a estar en nada. ¿Qué soy?",
                "Te paras cuando está verde y continúas cuando está rojo. ¿Qué es?",
                "¿Qué monte era el más alto del mundo antes de descubrir el Everest?",
                "La señora y el señor Sánchez tienen 6 hijos. Cada hijo tiene una hermana. ¿Cuántas personas hay en la familia Sánchez?",
                "Soy alto siendo joven y corto cuando soy viejo. Resplandezco con la vida y el viento es mi mayor enemigo. ¿Qué soy?"]

        self.solucion = ["mi nombre","el fuego","el huevo","un cepillo de dientes eléctrico", "febrero", 
        "la letra d","la sandía","el Everest","9","una vela"]
        self.solucion2 = ["mi nombre","el fuego","el huevo","un cepillo de dientes eléctrico", "febrero", 
        "la letra d","la sandía","el Everest","9","una vela"]
        self.numero = random.randint(0, 9)
        self.ui.label.setText(self.acertijo[self.numero])
        self.numero2 = random.randint(0, 3)
        if (self.numero2 ==  0):
            self.ui.radioButton.setText(self.solucion[self.numero])
        elif (self.numero2 == 1):
            self.ui.radioButton_2.setText(self.solucion[self.numero])
        elif (self.numero2 == 2):
            self.ui.radioButton_3.setText(self.solucion[self.numero])
        elif (self.numero2 == 3):
            self.ui.radioButton_4.setText(self.solucion[self.numero])
        self._radioButtonSur()
    
    def _radioButtonSur(self):
        self.solucion2.remove(self.solucion[self.numero])
        if (self.numero2 ==  0):
            numeroRandom = random.randint(0, 8) 
            solucionx = self.solucion2
            self.ui.radioButton_2.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 7)
            solucionx = self.solucion2
            self.ui.radioButton_3.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 6)
            solucionx = self.solucion2
            self.ui.radioButton_4.setText(self.solucion2[numeroRandom])
        elif (self.numero2 == 1):
            numeroRandom = random.randint(0, 8) 
            solucionx = self.solucion2
            self.ui.radioButton.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 7)
            solucionx = self.solucion2
            self.ui.radioButton_3.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 6)
            solucionx = self.solucion2
            self.ui.radioButton_4.setText(self.solucion2[numeroRandom])
        elif (self.numero2 == 2):
            numeroRandom = random.randint(0, 8) 
            solucionx = self.solucion2
            self.ui.radioButton.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 7)
            solucionx = self.solucion2
            self.ui.radioButton_2.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 6)
            solucionx = self.solucion2
            self.ui.radioButton_4.setText(self.solucion2[numeroRandom])
        elif (self.numero2 == 3):
            numeroRandom = random.randint(0, 8) 
            solucionx = self.solucion2
            self.ui.radioButton.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 7)
            solucionx = self.solucion2
            self.ui.radioButton_3.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 6)
            solucionx = self.solucion2
            self.ui.radioButton_2.setText(self.solucion2[numeroRandom])
    
    def _comprobarSur(self):
        if(self.ui.radioButton.isChecked() and self.numero2 == 0):
            self.ui.textEdit.setText("Has acertado")
            self.estaSur = False
            self._salaSurGanada()
            self._salirSala()
        elif(self.ui.radioButton_2.isChecked() and self.numero2 == 1):
            self.ui.textEdit.setText("Has acertado")
            self.estaSur = False
            self._salaSurGanada()
            self._salirSala()
        elif(self.ui.radioButton_3.isChecked() and self.numero2 == 2):
            self.ui.textEdit.setText("Has acertado")
            self.estaSur = False
            self._salaSurGanada()
            self._salirSala()
        elif(self.ui.radioButton_4.isChecked() and self.numero2 == 3):
            self.ui.textEdit.setText("Has acertado")
            self.estaSur = False
            self._salaSurGanada()
            self._salirSala()
        else:
            self.ui.textEdit.setText("Lo siento, no has acertado")
            self.estaSur = False
            self._salirSala()

    def _salaOeste(self):
        self.ui.label.setText("")
        self.ui.textEdit.setText("")
        self._disableButton1()
        self._activarRadio()
        self.estaOeste = True
        self.cadena = "Buenas apuesto caballero, le apuesto tres dirhams a que no puede resolver este acertijo:"
        self.ui.label.setText(self.cadena)
        self.acertijo = ["¿Cuál es el río más largo de España?","¿Cuál es el río más largo de la península ibérica?",
                "¿Cuál es el río más largo del mundo?","¿Cuál es la montaña más alta de España?",
                "¿Cuál es la montaña más alta del mundo? ","¿Cuál es el océano más grande?",
                "¿Cuál es el país con más extensión?","¿Cuál es el país más poblado?"]

        self.solucion = ["Ebro","Tajo","Amazonas","Teide","Everest","Pacífico","Rusia","India"]
        self.solucion2 = ["Ebro","Tajo","Amazonas","Teide","Everest","Pacífico","Rusia","India"]
        self.numero = random.randint(0, 7)
        self.ui.label.setText(self.acertijo[self.numero])
        self.numero2 = random.randint(0, 3)
        if (self.numero2 ==  0):
            self.ui.radioButton.setText(self.solucion[self.numero])
        elif (self.numero2 == 1):
            self.ui.radioButton_2.setText(self.solucion[self.numero])
        elif (self.numero2 == 2):
            self.ui.radioButton_3.setText(self.solucion[self.numero])
        elif (self.numero2 == 3):
            self.ui.radioButton_4.setText(self.solucion[self.numero])
        self._radioButtonOeste()
    
    def _radioButtonOeste(self):
        self.solucion2.remove(self.solucion[self.numero])
        if (self.numero2 ==  0):
            numeroRandom = random.randint(0, 6) 
            solucionx = self.solucion2
            self.ui.radioButton_2.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 5)
            solucionx = self.solucion2
            self.ui.radioButton_3.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 4)
            solucionx = self.solucion2
            self.ui.radioButton_4.setText(self.solucion2[numeroRandom])
        elif (self.numero2 == 1):
            numeroRandom = random.randint(0, 6) 
            solucionx = self.solucion2
            self.ui.radioButton.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 5)
            solucionx = self.solucion2
            self.ui.radioButton_3.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 4)
            solucionx = self.solucion2
            self.ui.radioButton_4.setText(self.solucion2[numeroRandom])
        elif (self.numero2 == 2):
            numeroRandom = random.randint(0, 6) 
            solucionx = self.solucion2
            self.ui.radioButton.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 5)
            solucionx = self.solucion2
            self.ui.radioButton_2.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 4)
            solucionx = self.solucion2
            self.ui.radioButton_4.setText(self.solucion2[numeroRandom])
        elif (self.numero2 == 3):
            numeroRandom = random.randint(0, 6) 
            solucionx = self.solucion2
            self.ui.radioButton.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 5)
            solucionx = self.solucion2
            self.ui.radioButton_3.setText(self.solucion2[numeroRandom])
            self.solucion2.remove(solucionx[numeroRandom])
            numeroRandom = random.randint(0, 4)
            solucionx = self.solucion2
            self.ui.radioButton_2.setText(self.solucion2[numeroRandom])
    
    def _comprobarOeste(self):
        
        if(self.ui.radioButton.isChecked() and self.numero2 == 0):
            self.ui.textEdit.setText("Has acertado")
            self.estaOeste = False
            self._salaOesteGanada()
            self._salirSala()
        elif(self.ui.radioButton_2.isChecked() and self.numero2 == 1):
            self.ui.textEdit.setText("Has acertado")
            self.estaOeste = False
            self._salaOesteGanada()
            self._salirSala()
        elif(self.ui.radioButton_3.isChecked() and self.numero2 == 2):
            self.ui.textEdit.setText("Has acertado")
            self.estaOester = False
            self._salaOesteGanada()
            self._salirSala()
        elif(self.ui.radioButton_4.isChecked() and self.numero2 == 3):
            self.ui.textEdit.setText("Has acertado")
            self.estaOeste = False
            self._salaOesteGanada()
            self._salirSala()
        else:
            self.ui.textEdit.setText("Lo siento, no has acertado")
            self.estaOeste = False
            self._salirSala()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = MainWindow()
    sys.exit(app.exec())