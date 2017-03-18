from Algoritmos.CentrosCuadrados import centros_cuadrados
from kivy.uix.screenmanager import ScreenManager,Screen
from ScreenObjects.CentrosMock import CentrosMock
from ScreenObjects.CentrosData import CentrosData
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.app import App



Builder.load_file('Kivy_Files/InitialScreen.kv')
Builder.load_file('Kivy_Files/CentrosCuadradosScreen.kv')
Builder.load_file('Kivy_Files/ErrorPopup.kv')

class ErrorPopup(Popup):

    errores = []

    def on_open(self):
        for e in self.errores:
            self.ids['errord'].add_widget(Label(text=e))



class CentrosCuadradosScreen(Screen):

    semilla = ObjectProperty()
    iteraciones = ObjectProperty()

    def on_pre_enter(self, *args):
        self.semilla.text = ''
        self.iteraciones.text = ''
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(CentrosMock())

    def validate_data(self):
        errores = []

        if self.semilla.text == "":
            errores.append("La semilla no puede estar vacia")
        else:
            s = int(self.semilla.text)
            l = len(str(s))
            if int(self.semilla.text) <= 0:
                errores.append("La semilla debe ser mayor a cero")
            if l % 2 != 0:
                errores.append("La semilla debe tener un número par de digitos")

        if self.iteraciones.text != "" and int(self.iteraciones.text)==0:
            errores.append("El número de iteraciones debe ser mayor a cero")

        if len(errores) == 0:
            self.generador()
        else:
            the_popup = ErrorPopup()
            the_popup.errores = errores
            the_popup.open()


    def generador(self):
        xn = []
        operador = []
        aleatorio = []
        random =[]
        l = len(self.semilla.text)
        if self.iteraciones.text == "":
            xn, operador, aleatorio, random = centros_cuadrados(int(self.semilla.text))
        else:
            xn, operador, aleatorio, random = centros_cuadrados(int(self.semilla.text),int(self.iteraciones.text))
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(CentrosData(xn,operador,aleatorio,random))


    def return_to_menu(self):
        screen_manager.transition.duration = 2
        screen_manager.transition.direction = "right"
        screen_manager.current = 'initial_screen'



class InitialScreen(Screen):
    def centros(self):
        screen_manager.transition.duration = 2
        screen_manager.transition.direction = "left"
        screen_manager.current = 'centros_screen'
    def close_app(self):
        App.get_running_app().stop()

screen_manager = ScreenManager()
screen_manager.add_widget(InitialScreen(name="initial_screen"))
screen_manager.add_widget(CentrosCuadradosScreen(name="centros_screen"))


class App(App):
    def build(self):
        return screen_manager

sample = App()

sample.run()
