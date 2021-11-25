from guizero import App, Text, PushButton, Slider, ButtonGroup, PushButton, Box

#Se crea la aplicacion
app = App(title="proyecto1", width=700, height=500,
          layout='auto', bg="black")

#Menu Principal Box
Menu_Box = Box(app, width="fill", height="fill", align="top")
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
    
Accept = PushButton(Menu_Box, command=Button_main_menu, text="Aceptar", width=20)
Accept.bg="#FDB716"

boton_volver = PushButton(Menu_juegos, command=Button_back, text="Volver")
boton_volver.bg="#FDB716"

btn_iniciar_juego = PushButton(Menu_juegos, command=Button_start_app, text="Iniciar")
btn_iniciar_juego.bg="#FDB716"



app.display()
