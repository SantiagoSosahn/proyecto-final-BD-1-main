from guizero import App, Text, PushButton, Slider, ButtonGroup, PushButton, Box, TextBox


class Welcome_screen_Game:
    def __init__(self):
        self.app = App(title="proyecto1", width=700, height=500,
        layout='auto', bg="black")
        self.Box_inicio = Box(self.app, width="fill", height="fill", align="top")
        self.Box_inicio.bg = "#03101C" 
        self.text_1 = Text(self.Box_inicio, text="Bienvenidos", size = 50)
        self.text_2 = Text(self.Box_inicio, text="Oprima Iniciar para continuar", size = 15)
        self.text_1.text_color = "yellow"
        self.text_2.text_color = "yellow"
        #Boton para ir al login

        self.inicio = PushButton(self.Box_inicio,command=self.regitroLogin ,text="Iniciar")
        self.inicio.text_color = "black"
        self.inicio.text_size = 30
        self.inicio.padding(100, 50)
        self.inicio.bg="#FDB716"
        
        
         #Funcion para id del inicio al ligin

    def regitroLogin(self):
    
        if(self.Box_inicio.visible == True):
        
            self.Box_inicio.hide()
            login_screen = Login(self.app)
            
    def ShowGame(self):
        self.app.display()
                
                

                

        
        








#Menu Principal Box










#Definiciones de funciones y botones



        

