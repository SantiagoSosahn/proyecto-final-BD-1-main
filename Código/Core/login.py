from guizero import TextBox, Text, PushButton, App, Box, MenuBar



class Login:
    def __init__(self, app):
        #Pantalla de login

        self.Box_login = Box(app, width="fill", height="fill", align="top", visible=False)
        self.Box_login.bg = "#03101C"
        text_1 = Text(self.Box_login, text="Introduzca sus datos", size = 40)
        text_1.text_color = "yellow"
        text_1.height = 2
        usuario = Text(self.Box_login, text="Usuario")
        usuario.text_color = "yellow"
        usuario.text_size = 20

        #Entrada de texto para el nombre de usuario

        input_usuario = TextBox(self.Box_login)
        input_usuario.width = 35
        input_usuario.bg = "white"
        contraseña = Text(self.Box_login, text="Contraceña")
        contraseña.text_color = "yellow"
        contraseña.text_size = 20

        #Entrada de texto para la contraceña

        input_contracenia = TextBox(self.Box_login, hide_text=True)
        input_contracenia.width = 35
        input_contracenia.bg = "white"

        
    def show_login(self):
        self.Box_login.show()
     
     #Se debe crear la validacion del input con    
    def validate_input(self):
       pass
       # self.Login_Box.hide()
        #menu_principalBox = Core.menu_principal.Menu_principal(self.app)
        
        
        




