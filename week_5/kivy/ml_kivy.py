from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import pickle

class WeightPredict(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        file_name = "finalized_model.sav"
        self.ml_service = pickle.load(open(file_name,'rb'))

        # label widget
        self.heading = Label(
                        text= "Weight Prediction in Lb",
                        font_size= 26,
                        bold= True,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.heading)

        # label widget
        self.greeting = Label(
                        text= "Enter Height in inches",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "PREDICT",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        try:
            height = int(self.user.text)
            self.greeting.text = "Predicted Weight(lb) =  "+str(self.ml_service.predict([[height]])[0])
        except:
            self.greeting.text = "Please type integer only values"
        

# run Say Hello App Calss
if __name__ == "__main__":
    WeightPredict().run()