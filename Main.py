from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.lang import Builder
import matplotlib.pyplot as plt
from kivy.app import App

Builder.load_file('Kivy_Files/InitialScreen.kv')

class InitialScreen(Screen):
   def close_app(self):
       App.get_running_app().stop()

screen_manager = ScreenManager()
screen_manager.add_widget(InitialScreen(name="initial_screen"))


class App(App):

    def build(self):
        return screen_manager

sample = App()

sample.run()
