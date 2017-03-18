from Algoritmos.Congruenciales import congruencial_lineal,congruencial_mixto,congruencial_multiplicativo
from ScreenObjects.CongruenciaLinealMock import CongruenciaLinealMock
from ScreenObjects.CongruenciaLinealData import CongruenciaLinealData
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
Builder.load_file('Kivy_Files/CongruencialLinealMixtoScreen.kv')
Builder.load_file('Kivy_Files/GeneradorMultiplicativoScreen.kv')


class ErrorPopup(Popup):
    errores = []
    def on_open(self):
        for e in self.errores:
            self.ids['errord'].add_widget(Label(text=e))


class GeneradorMultiplicativoScreen(Screen):

    semilla = ObjectProperty()
    a_value = ObjectProperty()
    modulo = ObjectProperty()
    iteraciones = ObjectProperty()

    def on_pre_enter(self, *args):
        self.semilla.text = ''
        self.a_value.text = ''
        self.modulo.text = ''
        self.iteraciones.text = ''
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(CongruenciaLinealMock())

    def return_to_menu(self):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "right"
        screen_manager.current = 'initial_screen'

    def generador(self):
        x = int(self.semilla.text)
        a = int(self.a_value.text)
        m = int(self.modulo.text)
        xn = []
        xni = []
        random =[]
        l = len(self.semilla.text)
        if self.iteraciones.text == "":
            xn, operador, random = congruencial_multiplicativo(x,a,m)
        else:
            xn, operador, random = congruencial_multiplicativo(x,a,m,int(self.iteraciones.text))
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(CongruenciaLinealData(xn,operador,random))

    def validate_data(self):
        errores = []

        if self.semilla.text == "":
            errores.append("Xo no puede estar vacio")
        else:
            val = int(self.semilla.text)
            if val == 0:
                errores.append("Xo debe ser mayor a 0")

        if self.a_value.text == "":
            errores.append("A no puede estar vacio")
        else:
            val = int(self.a_value.text)
            if val == 0:
                errores.append("A debe ser mayor a 0")

        if self.modulo.text == "":
            errores.append("El módulo no puede estar vacio")
        else:
            val = int(self.modulo.text)
            if val == 0:
                errores.append("El módulo ser mayor a 0")
            else:
                if val<int(self.a_value.text) or val<int(self.semilla.text):
                    errores.append("El módulo debe ser mayor que Xo y A")


        if self.iteraciones.text != "" and int(self.iteraciones.text)==0:
            errores.append("El número de iteraciones debe ser mayor a cero")

        if len(errores) == 0:
            self.generador()
        else:
            the_popup = ErrorPopup()
            the_popup.errores = errores
            the_popup.open()

class CongruencialMixtoScreen(Screen):

    semilla = ObjectProperty()
    a_value = ObjectProperty()
    c_value = ObjectProperty()
    modulo = ObjectProperty()
    iteraciones = ObjectProperty()

    def on_pre_enter(self, *args):
        self.semilla.text = ''
        self.a_value.text = ''
        self.c_value.text = ''
        self.modulo.text = ''
        self.iteraciones.text = ''
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(CongruenciaLinealMock())

    def return_to_menu(self):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "right"
        screen_manager.current = 'initial_screen'

    def generador(self):
        x = int(self.semilla.text)
        a = int(self.a_value.text)
        c = int(self.c_value.text)
        m = int(self.modulo.text)
        xn = []
        xni = []
        random =[]
        l = len(self.semilla.text)
        if self.iteraciones.text == "":
            xn, operador, random = congruencial_mixto(x,a,c,m)
        else:
            xn, operador, random = congruencial_mixto(x,a,c,m,int(self.iteraciones.text))
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(CongruenciaLinealData(xn,operador,random))

    def validate_data(self):
        errores = []

        if self.semilla.text == "":
            errores.append("Xo no puede estar vacio")
        else:
            val = int(self.semilla.text)
            if val == 0:
                errores.append("Xo debe ser mayor a 0")

        if self.a_value.text == "":
            errores.append("A no puede estar vacio")
        else:
            val = int(self.a_value.text)
            if val == 0:
                errores.append("A debe ser mayor a 0")

        if self.c_value.text == "":
            errores.append("C no puede estar vacio")
        else:
            val = int(self.c_value.text)
            if val == 0:
                errores.append("C debe ser mayor a 0")

        if self.modulo.text == "":
            errores.append("El módulo no puede estar vacio")
        else:
            val = int(self.modulo.text)
            if val == 0:
                errores.append("El módulo ser mayor a 0")
            else:
                if val<int(self.c_value.text) or val<int(self.a_value.text) or val<int(self.semilla.text):
                    errores.append("El módulo debe ser mayor que Xo,A y C")


        if self.iteraciones.text != "" and int(self.iteraciones.text)==0:
            errores.append("El número de iteraciones debe ser mayor a cero")

        if len(errores) == 0:
            self.generador()
        else:
            the_popup = ErrorPopup()
            the_popup.errores = errores
            the_popup.open()

class CongruencialLinealScreen(Screen):

    semilla = ObjectProperty()
    a_value = ObjectProperty()
    c_value = ObjectProperty()
    modulo = ObjectProperty()
    iteraciones = ObjectProperty()

    def on_pre_enter(self, *args):
        self.semilla.text = ''
        self.a_value.text = ''
        self.c_value.text = ''
        self.modulo.text = ''
        self.iteraciones.text = ''
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(CongruenciaLinealMock())

    def return_to_menu(self):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "right"
        screen_manager.current = 'initial_screen'

    def generador(self):
        x = int(self.semilla.text)
        a = int(self.a_value.text)
        c = int(self.c_value.text)
        m = int(self.modulo.text)
        xn = []
        xni = []
        random =[]
        l = len(self.semilla.text)
        if self.iteraciones.text == "":
            xn, operador, random = congruencial_lineal(x,a,c,m)
        else:
            xn, operador, random = congruencial_lineal(x,a,c,m,int(self.iteraciones.text))
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(CongruenciaLinealData(xn,operador,random))

    def validate_data(self):
        errores = []

        if self.semilla.text == "":
            errores.append("Xo no puede estar vacio")
        else:
            val = int(self.semilla.text)
            if val == 0:
                errores.append("Xo debe ser mayor a 0")

        if self.a_value.text == "":
            errores.append("A no puede estar vacio")
        else:
            val = int(self.a_value.text)
            if val == 0:
                errores.append("A debe ser mayor a 0")

        if self.c_value.text == "":
            errores.append("C no puede estar vacio")
        else:
            val = int(self.c_value.text)
            if val == 0:
                errores.append("C debe ser mayor a 0")

        if self.modulo.text == "":
            errores.append("El módulo no puede estar vacio")
        else:
            val = int(self.modulo.text)
            if val == 0:
                errores.append("El módulo ser mayor a 0")
            else:
                if val<int(self.c_value.text) or val<int(self.a_value.text) or val<int(self.semilla.text):
                    errores.append("El módulo debe ser mayor que Xo,A y C")


        if self.iteraciones.text != "" and int(self.iteraciones.text)==0:
            errores.append("El número de iteraciones debe ser mayor a cero")

        if len(errores) == 0:
            self.generador()
        else:
            the_popup = ErrorPopup()
            the_popup.errores = errores
            the_popup.open()




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
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "right"
        screen_manager.current = 'initial_screen'



class InitialScreen(Screen):

    def centros(self):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "left"
        screen_manager.current = 'centros_screen'

    def congruencial_lineal(self):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "left"
        screen_manager.current = 'congruencial_lineal'

    def congruencial_mixto(self):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "left"
        screen_manager.current = 'congruencial_mixto'

    def congruencial_multiplicativo(self):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "left"
        screen_manager.current = 'congruencial_multiplicativo'

    def close_app(self):
        App.get_running_app().stop()

screen_manager = ScreenManager()
screen_manager.add_widget(InitialScreen(name="initial_screen"))
screen_manager.add_widget(CentrosCuadradosScreen(name="centros_screen"))
screen_manager.add_widget(CongruencialLinealScreen(name="congruencial_lineal"))
screen_manager.add_widget(CongruencialMixtoScreen(name="congruencial_mixto"))
screen_manager.add_widget(GeneradorMultiplicativoScreen(name="congruencial_multiplicativo"))



class App(App):
    def build(self):
        return screen_manager

sample = App()

sample.run()
