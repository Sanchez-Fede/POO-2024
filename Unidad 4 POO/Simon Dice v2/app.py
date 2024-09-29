
from tkinter import *
from tkinter import ttk, font, messagebox, simpledialog
from claseJugador import Jugador
from claseGestorJugadores import GestorJugadores
import tkinter as tk
import time, random 
import datetime

class appSimonDice():

    __ventana : None
    __listaColor : list
    __botonApp : list
    __secuencia : list
    __NombreJugador : str
    __fecha : None
    __hora : None
    __puntaje : None
    __gestor : GestorJugadores

    def __init__(self):
        #   Configuraciones de la ventana
        self.__ventana =tk.Tk()
        self.__ventana.title('Simon dice by JugateYa')
        self.__ventana.geometry('250x450')
        self.__ventana.configure(bg='beige')
        self.__ventana.resizable(0,0)
        self.__listaColor = ["#006400", "#8B0000", "#CCCC00", "#00008B"]
        #   Datos jugador
        self.__NombreJugador = None
        self.__fecha = None
        self.__hora = None
        self.__puntaje = 0
        self.__gestor = GestorJugadores()
        self.__gestor.cargarJugadores()
        self.crearMenu()
        self.crearBotones()
        self.__ventana.protocol("WM_DELETE_WINDOW", self.salir_aplicacion)
        self.__ventana.mainloop()

    def crearMenu(self):
        # Barra menu
        barraMenu = Menu(self.__ventana)
        self.__ventana.config(menu = barraMenu)
        
        menuPuntaje = Menu(barraMenu, tearoff=0)
        barraMenu.add_cascade(label='Puntajes', menu = menuPuntaje)
        menuPuntaje.add_command(label='Listado de Puntajes', command=self.galeria_puntaje)
        menuPuntaje.add_command(label='Salir', command=self.salir_aplicacion)

    def crearBotones(self):
        self.__botonApp = []
        for i, color in enumerate(self.__listaColor):
            #   Creo el canvas
            unBoton = tk.Canvas(self.__ventana, width=100, height=150, background=color, relief="raised")
            unBoton.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            self.__botonApp.append(unBoton)
        # Creo los botones de comenzar y salir
        self.botonComenzar = tk.Button(self.__ventana, text="Comenzar", command=self.ventana_jugador, bg='beige', font='weight')
        self.botonComenzar.grid(row=4, column=1, ipady=10, ipadx=25)
        #  Etiquetas de Texto:
        fuente = font.Font(weight='bold')
        self.labelJugador = tk.Label(self.__ventana, text='', font=fuente, padx=5, pady=5, bg='beige' )
        self.labelJugador.grid(column=0, row=3)
        self.puntaje = tk.Label(self.__ventana, text='0', font=fuente, padx=5, pady=5, bg='beige')
        self.puntaje.grid(column=1, row=3)

#  Funciones del Juego:  =========================================================================== #
    #   Inicio el juego reseteando secuencia y respuesta del juegador
    def iniciarJuego(self):
        self.botonComenzar.config(state=tk.DISABLED) # luego de apretar el boton comenzar se inhabilita
        self.__secuencia = []
        self.respuesta_jugador = []
        self.generar_color()

    def generar_color(self):  
        if self.__secuencia == []:  #primer secuencia inicia con verde como pide la app
            color_nuevo = self.__listaColor[0]
            self.__secuencia.append(color_nuevo)
            self.mostrar_secuencia()
        else:
            color_nuevo = random.choice(self.__listaColor)
            self.__secuencia.append(color_nuevo)
            self.mostrar_secuencia()

    def mostrar_secuencia(self):
        time.sleep(1) #1 segundo
        for color in self.__secuencia:
            index_color = self.__listaColor.index(color)
            self.__botonApp[index_color].config(bg="gray")
            self.__ventana.update()
            time.sleep(1)
            self.__botonApp[index_color].config(bg=color)
            self.__ventana.update()
            time.sleep(0.5)
        self.jugar()

    def jugar(self):
        self.respuesta_jugador = []
        self.__ventana.bind("<Button-1>", self.procesar_clic) #Asociar el boton click izquierdo (mouse) para capturarlo 

    def procesar_clic(self, event):
        colores = ["#006400", "#8B0000", "#CCCC00", "#00008B"]
        colores_click = ['#7fbf80','#df5f5f','#ffff80','#7f7fbf'] # mismo colores con diferentes tonos
        boton_presionado = event.widget
        color_presionado = boton_presionado.cget("background")
        self.respuesta_jugador.append(color_presionado)
        
        for i in range(len(colores)):
            if colores[i] == color_presionado:
                boton_presionado.config(bg=colores_click[i])
        self.__ventana.update()
        time.sleep(0.2)
        boton_presionado.config(bg=color_presionado)
        self.__ventana.update()

        if len(self.respuesta_jugador) == len(self.__secuencia):
            self.verificar_respuesta()

    def verificar_respuesta(self):
        if self.respuesta_jugador == self.__secuencia:
            self.actualizar_puntaje(len(self.__secuencia))
            self.generar_color()
        else:
            messagebox.showinfo("¡Perdiste!", "Respuesta incorrecta. ¡Inténtalo de nuevo!")
            self.botonComenzar.config(state=tk.NORMAL)
            self.guardar_record()
            self.resetPuntaje()
            
    def resetPuntaje(self):
        self.puntaje.config(text='0')
        self.__puntaje = 0    
    def actualizar_puntaje(self, puntos):
        puntaje_actual = int(self.puntaje.cget("text"))
        self.__puntaje = puntaje_actual + puntos
        self.puntaje.config(text=str(self.__puntaje)) 

    def guardar_record(self):
        fecha_hora = datetime.datetime.now()
        self.__fecha = fecha_hora.date()
        self.__hora = fecha_hora.strftime('%H:%M:%S')
        self.__gestor.agregarJugador(Jugador(self.__NombreJugador,self.__fecha,self.__hora,self.__puntaje))
        self.resetPuntaje()

    #  Ventana donde ingresa el nombre el jugador
    def ventana_jugador(self):
        self.__ventanaJug = Toplevel()
        fuente = font.Font(weight='bold')
        self.__ventanaJug.resizable(0,0)
        self.__ventanaJug.title('Simon dice')
        
        #   Labels e inputs
        self.labelDatosJug = tk.Label(self.__ventanaJug, text='Datos del jugador')
        self.labelDatosJug.grid(row=0, column=0)
        
        self.nombre_jugador = tk.Label(self.__ventanaJug, text='Jugador', font=fuente, padx=5, pady=5)
        self.nombre_jugador.grid(row=1, column=0)
        self.__NombreJugador = StringVar()
        self.__NombreJugador.set('')
    
        self.ctext1 = tk.Entry(self.__ventanaJug, textvariable=self.__NombreJugador, width=30 )
        self.ctext1.grid(column=1, row=1, columnspan=2)
        
        #   Botones
        self.botonIniciar = tk.Button(self.__ventanaJug, text="Iniciar Juego",padx=5, pady=5, command=self.actualizarNombre)
        self.botonIniciar.grid(row=2, column=1)
        self.__ventanaJug.mainloop()
        
    def actualizarNombre(self):
        self.__NombreJugador = self.ctext1.get()
        self.labelJugador.configure(text=self.__NombreJugador)
        self.__ventanaJug.destroy()
        self.iniciarJuego()
    
    def salir_aplicacion(self):
        print('Saliendo de la app...\nGuardando records...')
        datos = self.__gestor.toJson()
        self.__gestor.guardarJSONArchivo(datos)
        self.__ventana.destroy()

    def galeria_puntaje(self):
        galeria = Toplevel() #ventana secundaria
        galeria.resizable(0,0)
        galeria.title('Galeria de Puntajes')
        frame = ttk.Frame(galeria)
        frame.pack(padx=10, pady=10)
        tree = ttk.Treeview(frame, columns=('Jugador', 'Fecha', 'Hora', 'Puntaje'), show='headings', height=5) #mostrar lista de contenido
        
        tree.heading("Jugador", text="Jugador")
        tree.heading("Fecha", text="Fecha")
        tree.heading("Hora", text="Hora")
        tree.heading("Puntaje", text="Puntaje")        
        
        tree.column("Jugador", width=100)
        tree.column("Fecha", width=100)
        tree.column("Hora", width=100)
        tree.column("Puntaje", width=100)
        
        jugadores = self.__gestor.get_jugadores()
        jugadores.sort()
        for jugador in jugadores:
            tree.insert("", tk.END, values=(jugador.getJugador(), jugador.getFecha(), jugador.getHora(), jugador.getPuntaje()))
            
        tree.pack()
        boton_salir = ttk.Button(galeria, text="Cerrar", command=galeria.destroy)
        boton_salir.pack(pady=10)
        
        galeria.mainloop()
        
if __name__ == '__main__':
    app = appSimonDice()
