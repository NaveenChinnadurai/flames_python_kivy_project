from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle

from flames_modules.utils import remainingLetter
from flames_modules.utils import findRelationLetter
from flames_modules.utils import finalRelation

def checkString(string):
    result=False
    for i in string:
        if (i>='a' and i<='z') or (i>='A' and i <='Z'):
            result=True
        else:
            result=False
            break
    return result

class Flames(App):
    def on_start(self):
        self.title = 'Flames'
    def build(self):
        
        main_layout = BoxLayout(orientation='horizontal',spacing=10)
        
        layout = BoxLayout(orientation='vertical',spacing=10,pos_hint={'center_y': 1})

        self.label = Label(text="Find relation between two people (Flames)", font_size=20, height=40,size_hint=(None, None), size=(300, 30),pos_hint={'center_x': 0.5,'center_y': 0.5})
        self.name1 = TextInput(size_hint=(None, None), size=(300, 30),pos_hint={'center_x': 0.5})
        self.name2 = TextInput(size_hint=(None, None), size=(300, 30),pos_hint={'center_x': 0.5})

        submit_button = Button(text='Submit', on_press=self.submit_inputs, size_hint=(None, None), size=(150, 30),background_color=(0.2, 0.3, 0.4, 1),pos_hint={'center_x': 0.5,'center_y': 0.5}, padding=(0, 30))
        
        layout.add_widget(self.label)
        layout.add_widget(self.name1)
        layout.add_widget(self.name2)
        layout.add_widget(submit_button)


        main_layout.add_widget(layout)
        return main_layout

    def submit_inputs(self, instance):
        input1_text = self.name1.text
        input2_text = self.name2.text

        if checkString(input1_text) and checkString(input2_text):
            letterRemaining = remainingLetter(input1_text, input2_text)
            relation = findRelationLetter(letterRemaining)
            
            label = Label(text=finalRelation(relation))
            popup_layout = BoxLayout(orientation='vertical', padding=20)
            popup_layout.add_widget(label)

            popup = Popup(title='Flames Popup', content=popup_layout, size_hint=(None, None), size=(300, 200))
            label.bind(on_press=popup.dismiss)
            popup.open()
        else:
            if len(input1_text) == 0 and len(input2_text) == 0:
                content = "Enter Valid Names (Empty Strings Obtained)!!"
            else:
                content = "Names can consist of only alphabets, no numeric or special characters allowed"
            error_label = Label(text=content)
            error_popup = Popup(title='Error', content=error_label, size_hint=(None, None), size=(350, 200))
            error_label.bind(on_press=error_popup.dismiss)
            error_popup.open()

if __name__ == '__main__':
    Flames().run()
