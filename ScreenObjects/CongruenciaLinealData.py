from Table.Table import Table
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

class CongruenciaLinealData(BoxLayout):
    """docstring for MainScreen"""
    def __init__(self,xn,xni,random):
        super(CongruenciaLinealData, self).__init__()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.my_table = Table()
        self.my_table.cols = 4
        self.my_table.add_button_row("n",'Xn', 'Xn+1', "Random")
        l = len(xn)
        for i in range(l):
            self.my_table.add_row(
                [Button,{'text': str(i), 'color_widget': [0, 0, 0.5, 1], 'color_click': [0, 1, 0, 1], 'size_hint_x': 1}],
                [TextInput, {'text': str(xn[i]),'color_click': [1, 0, .5, 1], 'readonly':True, 'size_hint_x': 1}],
                [TextInput, {'text': str(xni[i]),'color_click': [1, 0, .5, 1], 'readonly':True, 'size_hint_x': 1}],
                [TextInput, {'text': str(random[i]), 'color_click': [1, 0, .5, 1], 'readonly': True, 'size_hint_x': 1}]
            )
        self.my_table.label_panel.visible = False
        self.my_table.label_panel.height_widget = 0
        self.my_table.label_panel.color = [1, 1, 1, 1]
        self.my_table.number_panel.auto_width = False
        self.my_table.number_panel.width_widget = 100
        self.my_table.number_panel.visible = False
        self.my_table.grid.color = [0, 0.4, 0, 1]
        self.my_table.label_panel.color = [0, 1, 0, 1]
        self.my_table.number_panel.color = [0, 0, 1, 1]
        self.my_table.scroll_view.bar_width = 10
        self.my_table.scroll_view.scroll_type = ['bars']
        self.add_widget(self.my_table)

    def _keyboard_closed(self):
        pass

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        pass