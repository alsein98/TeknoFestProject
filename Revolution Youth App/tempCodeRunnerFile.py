import kivy
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
kivy.require('1.9.0')

class giris(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1
        #--------------top grid--
        self.top_grid=GridLayout()
        self.top_grid.cols=2
        
        #-----------------main rows - creat/add widg.  ----------
        self.l1=Label(text=  "Bluetooth Connection")
        # self.l1=Label(text=  "Bluetooth Connection",halign='right', valign='middle', text_size=(390, 100))
        self.b1=Button(text=  "Bluetooth switch Button ")
        #self.l1.pos = (Window.width / 4, Window.height / 4)
        self.top_grid.add_widget(self.l1)
        self.top_grid.add_widget(self.b1)
        #----------------------------------------------
        self.l4=Label(text="Upload file icon")
        self.b2=Button(text=  "Upload File Button")
        self.top_grid.add_widget(self.l4)
        self.top_grid.add_widget(self.b2)
        #----------------------------------------------
        self.l5=Label(text="Library icon")
        self.b3=Button(text=  "Library Button")
        self.top_grid.add_widget(self.l5)
        self.top_grid.add_widget(self.b3)
        #----------------------------------------------
        self.l6=Label(text="Upload Audio icon")
        self.b4=Button(text=  "Upload Audio Button")
        self.top_grid.add_widget(self.l6)
        self.top_grid.add_widget(self.b4)
        #----------------------------------------------
        self.ti1=TextInput(multiline=False)
        self.b5=Button(text="Enter Text")
        self.b5.bind(on_press=self.ret)
        self.top_grid.add_widget(self.b5)
        self.top_grid.add_widget(self.ti1)
        
        #----------------------------------------------
        self.l7=Label(text="Push To Talk icon")
        self.b6=Button(text=  "Real-Time Recognition")
        self.top_grid.add_widget(self.l7)
        self.top_grid.add_widget(self.b6)
        #----------------------------------------------
        self.add_widget(self.top_grid)
        self.l9=Label(text="Text-Output",size_hint_y=None, size_hint=(0.5, 0.5), size=(200, 100))
        #self.l10=Label()
        self.add_widget(self.l9)
        #self.add_widget(self.l10)
        #-----------------------------------------------
        #self.add_widget(Button(text=  "Test", size_hint=(0.5, 0.#5), size=(200, 100)))
        
        self.l2=Button(text=  " TEKNOFEST-2023\n  Revolution Youth", size_hint=(0, 0.15), size=(200, 100))
        #self.l3=Label()
        self.add_widget(self.l2)
        #self.add_widget(self.l3)
        #-----------------Functions----------
    # convert to binary - send via bluetooth
    def print(self,instance): 
        self.l9.text=self.ti1.text
        print((self.ti1.text))
    def ret(self,instance):
        dic={" ":"00000","a":"00001","e":"00010","i":"00100","n":"01000","r":"10000","l":"00011",
         "k":"00101","m":"01001","d":"10001","t":"00110","o":"01010","u":"10010","y":"01100",
         "b":"10100","s":"11000","g":"00111","z":"01011","c":"10011","ş":"01101","ö":"10011",
         "v":"10101", "w":"10101","j":"11001","h":"01110","ı":"10110","p":"11010","f":"11100","ç":"11100","ğ":"01111"   
        }
        try :
            l=[dic[s.lower()] for s in self.ti1.text]
            print(l)
        except Exception as e:
            print(e)
        l.append("00000")
        self.l9.text=" ".join(l)
        print(" ".join(l))
        return str(l)


class RyApp(App):
    def build(self):
        return giris()
    
if __name__ == "__main__":
    RyApp().run()