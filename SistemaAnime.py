from tkinter import messagebox
from os import getcwd, makedirs
import pymysql
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QFile, QSize
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMessageBox)
import sys
from PyQt5 import uic, QtWidgets
import random

from PyQt5.QtWidgets import QMainWindow, QApplication


class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Buscador.ui", self)
        self.Boton_Buscar.clicked.connect(self.fn_BuscarBD)
        self.Expl.clicked.connect(self.fn_Expl)
        self.Label_Explicacion.setVisible(False)
        self.label_Explicacion2.setVisible(False)
        self.Expl.setVisible(False)
        self.boton1.clicked.connect(self.mostrar1)
        self.boton2.clicked.connect(self.mostrar2)
        self.boton1.setVisible(False)
        self.boton2.setVisible(False)
        self.fn_Combos()

        icono = QIcon()
        icono.addFile('icono/icono.ico', QSize(16, 16))
        icono.addFile('icono/icono.ico', QSize(24, 24))
        icono.addFile('icono/icono.ico', QSize(32, 32))
        icono.addFile('icono/icono.ico', QSize(48, 48))
        self.setWindowIcon(icono)

    def reiniciar(self):
        self.LabelNombre.clear()
        self.LabelNombre_2.clear()
        self.Label_Explicacion.clear()
        self.label_Explicacion2.clear()
        self.labelImagen_2.clear()
        self.labelImagen.clear()
        self.boton1.setVisible(False)
        self.boton2.setVisible(False)
        self.Label_Explicacion.setText("")

    def mostrar1(self):
        # Mostrar el texto

        if self.Label_Explicacion.isVisible():
            self.Label_Explicacion.setVisible(False)
            self.boton1.setText("Ver explicación")
        else:
            self.Label_Explicacion.setVisible(True)
            self.boton1.setText("Ocultar explicación")

    def mostrar2(self):
        # Mostrar el texto
        if self.label_Explicacion2.isVisible():
            self.label_Explicacion2.setVisible(False)
            self.boton2.setText("Ver explicación")
        else:
            self.label_Explicacion2.setVisible(True)
            self.boton2.setText("Ocultar explicación")

    def fn_volver(self):
        reply = QMessageBox.question(
            self, 'Confirmación', '¿Seguro que deseas salir?, Se perderá lo que no hayas guardado', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # Si el usuario hace clic en "sí", imprime "Hola"
        if reply == QMessageBox.Yes:
            self.fn_Buscar()

    def fn_Ingresar(self):
        self.ventana = QtWidgets.QMainWindow()
        uic.loadUi("Ingreso.ui", self)
        self.Guardar.clicked.connect(self.fn_capturar_Ingreso)
        self.volver.clicked.connect(self.fn_volver)
        self.Imagen.clicked.connect(self.seleccionar)
        self.fn_Combos()

    def fn_Buscar(self):
        self.ventana = QtWidgets.QMainWindow()
        uic.loadUi("Buscador.ui", self)
        self.Expl.clicked.connect(self.fn_Expl)
        self.Boton_Buscar.clicked.connect(self.fn_BuscarBD)
        self.reiniciar()
        self.fn_Combos()
        self.Label_Explicacion.setVisible(False)
        self.label_Explicacion2.setVisible(False)
        self.boton1.clicked.connect(self.mostrar1)
        self.boton2.clicked.connect(self.mostrar2)
        self.boton1.setVisible(False)
        self.boton2.setVisible(False)
        self.Expl.setVisible(False)

    def fn_Combos(self):
        self.Clasificacion.clear()
        self.Edad.clear()
        self.GeneroP.clear()
        self.Motivo.clear()

        bd = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="animes"
        )
        # EDADES
        sql = "SELECT DISTINCT Edad FROM anime"
        mcursor = bd.cursor()
        mcursor.execute(sql)
        resultados = mcursor.fetchall()
        for resultado in resultados:
            self.Edad.addItem(str(resultado[0]))
        # CAPITULOS
        sql = "SELECT DISTINCT Genero FROM anime"
        mcursor = bd.cursor()
        mcursor.execute(sql)
        resultados = mcursor.fetchall()
        for resultado in resultados:
            self.GeneroP.addItem(str(resultado[0]))
        # TRAMA

        sql = "SELECT DISTINCT Motivo FROM anime"
        mcursor = bd.cursor()
        mcursor.execute(sql)
        resultados = mcursor.fetchall()
        for resultado in resultados:
            self.Motivo.addItem(str(resultado[0]))

        # GENERO
        sql = "SELECT DISTINCT Clasificacion FROM anime"
        mcursor = bd.cursor()
        mcursor.execute(sql)
        resultados = mcursor.fetchall()
        for resultado in resultados:
            self.Clasificacion.addItem(str(resultado[0]))

    def fn_Desc(self):
        Edad = self.Edad.currentText()
        Genero = self.GeneroP.currentText()
        Motivo = self.Motivo.currentText()
        Clasificacion = self.Clasificacion.currentText()

        self.Label_Explicacion.clear()

        bd = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="animes"
        )

        sql = "SELECT Nombre FROM anime WHERE Edad='{0}' AND Genero='{1}' AND Motivo='{2}' AND Clasificacion='{3}'".format(
            Edad, Genero, Motivo, Clasificacion)
        mcursor = bd.cursor()
        mcursor.execute(sql)
        nombres = mcursor.fetchall()

        if len(nombres) > 0:
            nombre = nombres[0][0]
            sql2 = "SELECT DISTINCT Explicacion FROM anime WHERE Nombre='{0}'".format(
                nombre)
            mcursor2 = bd.cursor()
            mcursor2.execute(sql2)
            descripcion = mcursor2.fetchone()[0][0]

            self.Label_Explicacion.setText(descripcion)
        else:
            messagebox.showwarning(
                message="La busqueda no se ha encontrado, se habilitó el botón para el modo experto.", title="No se encontro la Rama")
            self.Expl.setVisible(True)
            # REINICIAR
            self.reiniciar()

    def fn_BuscarBD(self):
        self.reiniciar()
        Edad = self.Edad.currentText()
        Genero = self.GeneroP.currentText()
        Motivo = self.Motivo.currentText()
        Clasificacion = self.Clasificacion.currentText()

        bd = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="animes"
        )
        sql = "SELECT Nombre FROM anime WHERE Edad='{0}' AND Genero='{1}' AND Motivo='{2}' AND Clasificacion='{3}'".format(
            Edad, Genero, Motivo, Clasificacion)
        mcursor = bd.cursor()
        mcursor.execute(sql)

        sql2 = "SELECT DISTINCT Explicacion FROM anime WHERE Edad='{0}' AND Genero='{1}' AND Motivo='{2}' AND Clasificacion='{3}'".format(
            Edad, Genero, Motivo, Clasificacion)
        mcursor2 = bd.cursor()
        mcursor2.execute(sql2)

        try:
            Nombre3 = mcursor.fetchall()
            Explicacion = mcursor2.fetchone()
            Explain = str(Explicacion)
            Nombre = str(Nombre3)
            Digitos = Nombre
            Digitos2 = Explain
            Anime1 = ""
            Anime2 = ""
            Anime3 = ""
            AnimeNueva1 = ""
            AnimeNueva2 = ""
            Copia = 0
            i = 0
            o = 0
            
            for p in Digitos2:
                if p == ",":
                    Copia += 1
            for explain in Explicacion:
                if o == 0:
                    Anime12 = str(explain)
                else:
                    if o == 1:
                        Anime22 = str(explain)
                    else:
                        Anime32 = str(explain)
                o = o + 1

            for c in Digitos:
                if c == ",":
                    Copia += 1
            for nombre in Nombre3:
                if i == 0:
                    Anime1 = str(nombre)
                else:
                    if i == 1:
                        Anime2 = str(nombre)
                    else:
                        Anime3 = str(nombre)
                i = i + 1

            AnimeNueva2 = str(Anime1)

            if AnimeNueva2:
                AnimeNueva2 = AnimeNueva2.translate({ord(','): None})
                AnimeNueva2 = AnimeNueva2.translate({ord("'"): None})
                AnimeNueva2 = AnimeNueva2.translate({ord(')'): None})
                AnimeNueva2 = AnimeNueva2.translate({ord('('): None})
            else:
                AnimeNueva2 = ""
            if Anime2:
                AnimeNueva1 = str(Anime2)
                AnimeNueva1 = AnimeNueva1.translate({ord(','): None})
                AnimeNueva1 = AnimeNueva1.translate({ord("'"): None})
                AnimeNueva1 = AnimeNueva1.translate({ord(')'): None})
                AnimeNueva1 = AnimeNueva1.translate({ord('('): None})
                Nombre4 = AnimeNueva1
            else:
                nuevo = ""
                Anime2 = ""
                pixmapImagen = QPixmap(
                    "Imagenes/{}.png".format(AnimeNueva2)).scaled(166, 178,
                                                                  Qt.KeepAspectRatio,
                                                                  Qt.SmoothTransformation)
                self.labelImagen_2.clear()
                self.LabelNombre_2.setText(Anime2)
                self.label_Explicacion2.setText(Anime2)
                self.Expl.setVisible(False)
                if not pixmapImagen.isNull():
                    # El pixmap no es nulo, mostrar la imagen correspondiente
                    self.labelImagen.setPixmap(pixmapImagen)
                    self.LabelNombre.setText(AnimeNueva2)
                else:
                    # El pixmap es nulo, generar una imagen aleatoria entre 1 y 100
                    num_aleatorio = random.randint(1, 100)
                    pixmapImagenAleatoria = QPixmap("Imagenes/{}.png".format(num_aleatorio)).scaled(166, 178,
                                                                                                    Qt.KeepAspectRatio,
                                                                                                    Qt.SmoothTransformation)
                    self.labelImagen.setPixmap(pixmapImagenAleatoria)
                    self.LabelNombre.setText(AnimeNueva2)

                if (Anime2 != ""):
                    self.boton2.setVisible(True)
            if AnimeNueva2:
                # Adaptar imagen
                pixmapImagen = QPixmap("Imagenes/{}.png".format(AnimeNueva2)).scaled(166, 178,
                                                                                     Qt.KeepAspectRatio,
                                                                                     Qt.SmoothTransformation)
                if not pixmapImagen.isNull():
                    # El pixmap no es nulo, mostrar la imagen correspondiente
                    self.labelImagen.setPixmap(pixmapImagen)
                    self.LabelNombre.setText(AnimeNueva2)
                else:
                    # El pixmap es nulo, generar una imagen aleatoria entre 1 y 100
                    num_aleatorio = random.randint(1, 100)
                    pixmapImagenAleatoria = QPixmap("Imagenes/{}.png".format(num_aleatorio)).scaled(166, 178,
                                                                                                    Qt.KeepAspectRatio,
                                                                                                    Qt.SmoothTransformation)
                    self.labelImagen.setPixmap(pixmapImagenAleatoria)
                    self.LabelNombre.setText(AnimeNueva2)
                    print(AnimeNueva2)
                    # print(AnimeNueva2) FUNCA
                    
                
                AnimeNueva22 = str(Anime12)

                if AnimeNueva22:
                    AnimeNueva22 = AnimeNueva22.translate({ord(','): None})
                    AnimeNueva22 = AnimeNueva22.translate({ord("'"): None})
                    AnimeNueva22 = AnimeNueva22.translate({ord(')'): None})
                    AnimeNueva22 = AnimeNueva22.translate({ord('('): None})
                else:
                    AnimeNueva22 = ""

                self.Label_Explicacion.setText(AnimeNueva22)
                self.Expl.setVisible(False)
                self.boton1.setVisible(True)
                i == 10
                bd.commit()
            else:
                messagebox.showwarning(message="La busqueda no se ha encontrado, el botón de modo experto ha sido habilitado.", title="No se encontro la Rama")
                self.Expl.setVisible(True)
                self.reiniciar()
                
            if len(AnimeNueva1) > 0:
                # Adaptar imagen
                pixmapImagen = QPixmap(
                    "Imagenes/{}.png".format(AnimeNueva1)).scaled(166, 178,
                                                                  Qt.KeepAspectRatio,
                                                                  Qt.SmoothTransformation)

                if not pixmapImagen.isNull():
                    # El pixmap no es nulo, mostrar la imagen correspondiente
                    self.labelImagen_2.setPixmap(pixmapImagen)
                    self.LabelNombre_2.setText(AnimeNueva1)
                else:
                    # El pixmap es nulo, generar una imagen aleatoria entre 1 y 100
                    num_aleatorio2 = random.randint(1, 100)
                    pixmapImagenAleatoria2 = QPixmap("Imagenes/{}.png".format(num_aleatorio2)).scaled(166, 178,
                                                                                                      Qt.KeepAspectRatio,
                                                                                                      Qt.SmoothTransformation)
                    self.labelImagen_2.setPixmap(pixmapImagenAleatoria2)
                    self.LabelNombre_2.setText(AnimeNueva1)

                self.fn_Desc

                sql2 = "SELECT Explicacion FROM anime WHERE nombre='{0}'".format(
                    AnimeNueva1)
                mcursor2 = bd.cursor()
                mcursor2.execute(sql2)
                Describir = mcursor2.fetchone()
                Describiro = str(Describir)

                if Describiro:
                    Describiro = Describiro.translate({ord(','): None})
                    Describiro = Describiro.translate({ord("'"): None})
                    Describiro = Describiro.translate({ord(')'): None})
                    Describiro = Describiro.translate({ord('('): None})
                else:
                    Describiro = ""

                self.label_Explicacion2.setText(Describiro)

                if (Describiro != ""):
                    self.boton2.setVisible(True)
                    self.Expl.setVisible(False)

                bd.commit()

            else:
                bd.rollback()

        except:
            bd.rollback()

        bd.close()

    def fn_capturar_Ingreso(self):
        # captura de los datos pasado a variables adentro del def
        Edad = self.Edad.currentText()
        Genero = self.GeneroP.currentText()
        Motivo = self.Motivo.currentText()
        Clasificacion = self.Clasificacion.currentText()
        Exp = self.Explicacion.text()
        Nombre = self.Nombre.text()
        foto = self.labelImagen.pixmap()

        Res = "0"
        if foto and Nombre and Exp and (len(Edad) != 0) and (len(Genero) != 0) and (len(Motivo) != 0) and (len(Clasificacion) != 0):

            bd = pymysql.connect(
                host="127.0.0.1",
                user="root",
                passwd="",
                db="animes"
            )

            mXcursor = bd.cursor()

            sqlX = "SELECT Nombre FROM anime WHERE Edad='{0}' AND Genero='{1}' AND Motivo='{2}' AND Clasificacion='{3}'".format(
                Edad, Genero, Motivo, Clasificacion)

            try:

                mXcursor.execute(sqlX)
                NombreX = str(mXcursor.fetchall())
                NombreX2 = NombreX.translate({ord(','): None})
                NombreX2 = NombreX2.translate({ord(')'): None})
                NombreX2 = NombreX2.translate({ord("'"): None})
                NombreX2 = NombreX2.translate({ord("("): None})
                Res = "1"

                Digitos = NombreX
                Copia = 0
                for c in Digitos:
                    if c == ",":
                        Copia += 1

                if Copia == 2 or Copia == 0:
                    Res = "1"
                else:
                    Res = "0"

            except:
                bd.rollback()
                messagebox.showinfo(
                    message="No se pudo registrar", title="Error")

            if Res == "1":
                bd = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    db="animes"
                )

                mcursor = bd.cursor()

                sql = "INSERT INTO anime (Edad,Genero,Motivo,Clasificacion,Explicacion,Nombre) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(
                    Edad, Genero, Motivo, Clasificacion, Exp, Nombre)

                try:
                    mcursor.execute(sql)
                    bd.commit()
                    messagebox.showinfo(
                        message="Se ha registrado la rama correctamente", title="Registro Completado")
                except:
                    bd.rollback()
                    messagebox.showinfo(
                        message="Existe un error en el registro", title="Error en el registro")
                bd.close()

                if not QFile.exists("Imagenes"):
                    makedirs("Imagenes")
                foto.save("Imagenes/{}.png".format(Nombre), quality=100)

            else:
                messagebox.showinfo(
                    message="Ya se excedio un limite de resultados", title="Error en el registro")
        else:
            messagebox.showinfo(
                message="Acompleta todos los parametros solicitados", title="Error en el registro")

    def fn_Expl(self):
        Nombre = self.LabelNombre.text()
        Nombre2 = self.LabelNombre_2.text()
        Edad = self.Edad.itemText(self.Edad.currentIndex())
        Genero = self.GeneroP.itemText(self.GeneroP.currentIndex())
        Motivo = self.Motivo.itemText(self.Motivo.currentIndex())
        Clasificacion = self.Clasificacion.itemText(
            self.Clasificacion.currentIndex())
        Anime1 = ""
        Anime2 = ""
        Anime3 = ""
        i = 0

        bd = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="animes"
        )
        sql2 = "SELECT Nombre FROM anime WHERE Edad='{0}' AND Genero='{1}' AND Motivo='{2}' AND Clasificacion='{3}'".format(
            Edad, Genero, Motivo, Clasificacion)
        mscursor = bd.cursor()
        mscursor.execute(sql2)

        try:
            self.fn_Ingresar()

        except:
            bd.rollback()
            messagebox.showinfo(message="Ha ocurrido un error", title="Error")

        bd.close()

    def seleccionar(self):
        imagen, extension = QFileDialog.getOpenFileName(self, "Seleccionar imagen", getcwd(),
                                                        "Archivos de imagen (*.png *.jpg)",
                                                        options=QFileDialog.Options())
        if imagen:
            # Adaptar imagen
            pixmapImagen = QPixmap(imagen).scaled(166, 178, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)

            # Mostrar imagen
            self.labelImagen.setPixmap(pixmapImagen)


if __name__ == '__main__':
    app = QApplication(sys.argv[:1])
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())
