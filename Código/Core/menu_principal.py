from guizero import App, Text, PushButton, Slider, ButtonGroup, PushButton, Box, TextBox



#Se crea la aplicacion

app = App(title="proyecto1", width=700, height=500,

          layout='auto', bg="black")





#Pantalal de inicio de bienvenida.

Box_inicio = Box(app, width="fill", height="fill", align="top")

Box_inicio.bg = "#03101C" 

text_1 = Text(Box_inicio, text="Bienvenidos", size = 50)

text_2 = Text(Box_inicio, text="Oprima Iniciar para continuar", size = 15)

text_1.text_color = "yellow"

text_2.text_color = "yellow"



#Pantalla de login

Box_login = Box(app, width="fill", height="fill", align="top", visible=False)

Box_login.bg = "#03101C"

text_1 = Text(Box_login, text="Introdusca sus datos", size = 40)

text_1.text_color = "yellow"

text_1.height = 2



usuario = Text(Box_login, text="Usuario")

usuario.text_color = "yellow"

usuario.text_size = 20

#Entrada de texto para el nombre de usuario

input_usuario = TextBox(Box_login)

input_usuario.width = 35

input_usuario.bg = "white"



contracenia = Text(Box_login, text="Contraceña")

contracenia.text_color = "yellow"

contracenia.text_size = 20

#Entrada de texto para la contraceña

input_contracenia = TextBox(Box_login)

input_contracenia.width = 35

input_contracenia.bg = "white"





#Menu Principal Box

Menu_Box = Box(app, width="fill", height="fill", align="top",visible = False)

Menu_Box.bg = "#03101C"

welcome_message = Text(Menu_Box, text="Menu", size=20, color="white")

choose = ButtonGroup(Menu_Box, options=["1.Partida Nueva", "2.Reanudar Partida",

                                        "3.Opciones", "4.Salir"])

choose.text_size = 12

choose.text_color = "#FFFFFF"

choose.font="Poppins"





#Menu Juegos

Menu_juegos = Box(app, visible=False, width="fill", height="fill")

Menu_juegos.bg="#03101C"

txt_menu_juegos = Text(Menu_juegos, text="Seleccione una opcion")

choose_game = ButtonGroup(Menu_juegos, options=["1.Tic Tac Toe", "2.Paint"])

choose_game.text_color="white"

txt_menu_juegos.text_color="white";

choose_game.text_size = 12



#Definiciones de funciones y botones

def Button_main_menu():

    if(Menu_Box.visible == True):

        Menu_Box.hide()

        Menu_juegos.show();

        

def Button_back():

    Menu_juegos.hide()

    Menu_Box.show()

    

def Button_start_app():

    pass



 #Funcion para id del inicio al ligin

def regitroLogin():

    if(Box_inicio.visible == True):

        Box_inicio.hide()

        Box_login.show()

   

def menuJuego():

    Box_login.hide()

    Menu_juegos.show()

    

Accept = PushButton(Menu_Box, command=Button_main_menu, text="Aceptar", width=20)

Accept.bg="#FDB716"



boton_volver = PushButton(Menu_juegos, command=Button_back, text="Volver")

boton_volver.bg="#FDB716"



btn_iniciar_juego = PushButton(Menu_juegos, command=Button_start_app, text="Iniciar")

btn_iniciar_juego.bg="#FDB716"



#Boton para ir al login

inicio = PushButton(Box_inicio,command=regitroLogin ,text="Iniciar")

inicio.text_color = "black"

inicio.text_size = 30

inicio.padding(100, 50)

inicio.bg="#FDB716"



#Boton para ir al menu del juego y programa

regitrarse = PushButton(Box_login, text="Registrarse",command=menuJuego)

regitrarse.text_color = "black"

regitrarse.text_size = 20

regitrarse.width = 16

regitrarse.bg="#FDB716"







app.display()

