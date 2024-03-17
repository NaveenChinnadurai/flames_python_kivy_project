from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup

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
        # Create a BoxLayout as the main layout, centered both vertically and horizontally
        main_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(400, 400), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Create a GridLayout to hold the elements
        layout = GridLayout(cols=1, spacing=10, size_hint=(None, None), size=(400, 200))

        self.label = Label(text="Find relation between two people (Flames)", font_size=20, size_hint_y=None, height=40)
        self.name1 = TextInput(size_hint=(None, None), size=(300, 30))
        self.name2 = TextInput(size_hint=(None, None), size=(300, 30))

        submit_button = Button(text='Submit', on_press=self.submit_inputs, size_hint=(None, None), size=(150, 30))
        
        layout.add_widget(self.label)
        layout.add_widget(self.name1)
        layout.add_widget(self.name2)
        layout.add_widget(submit_button)

        # Set GridLayout height to match its content

        # Add GridLayout to the BoxLayout
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
    Window.size = (600, 300)
    Flames().run()
