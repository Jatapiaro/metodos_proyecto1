from kivy.uix.screenmanager import ScreenManager,Screen
from Table.Table import Table
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.app import App
from ScreenObjects.CentrosMock import CentrosMock

Builder.load_file('Kivy_Files/InitialScreen.kv')
Builder.load_file('Kivy_Files/CentrosCuadradosScreen.kv')


class CentrosCuadradosScreen(Screen):
    def on_pre_enter(self, *args):
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(CentrosMock(80))



class InitialScreen(Screen):
    def centros(self):
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
