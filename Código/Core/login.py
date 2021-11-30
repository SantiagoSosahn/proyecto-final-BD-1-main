from guizero import TextBox, Text, PushButton, App, Box, MenuBar
import Core.menu_principal


class Login:
    def __init__(self):
        self.app = App(title="proyecto1", width=700, height=500,
        layout='auto', bg="black")
        
        
        #Login Box
        self.Login_Box = Box(self.app,  width="fill", height="fill", align="center")
        self.Login_Box.bg = "#03101C"
        self.Login_Title = Text(self.Login_Box, text="Login",color="white")
        self.Login_Title.size=32
        self.Login_Title.font="Poppins"
        self.txtb_name = TextBox(self.Login_Box,  width=25, height=5)
        self.txtb_password = TextBox(self.Login_Box,  width=25, height=5,hide_text=True)
        self.txtb_name.bg="white"
        self.txtb_password.bg = "white"
        self.iniciar_sesion = PushButton(self.Login_Box, text="Iniciar sesion", command=self.validate_input)
        self.iniciar_sesion.bg="#FDB716"
        
    def show_login(self):
        self.app.display()
     
     #Se debe crear la validacion del input con    
    def validate_input(self):
        self.Login_Box.hide()
        menu_principalBox = Core.menu_principal.Menu_principal(self.app)
        
        
        




