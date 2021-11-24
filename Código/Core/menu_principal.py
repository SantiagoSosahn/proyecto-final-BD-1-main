from guizero import App, Text, PushButton, Slider, ButtonGroup, PushButton

app = App(title="proyecto1", width=700, height=500,
          layout='auto', bg="#2675D1")

welcome_message = Text(app, text="Menu", size=40, color="white")
choose = ButtonGroup(app, options=["1.X-O", "2.Paint", "3.Administrar Usuarios", "4.Bitacora"])
choose.text_size = 12
Accept = PushButton(app, command=None, text="Aceptar", width=20)
Accept.bg="#FDB716"

app.display()