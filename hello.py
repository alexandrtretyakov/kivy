from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MainWidget(BoxLayout):
    hello_label = ObjectProperty()
    name_input = ObjectProperty()

    def say_hello(self):
        self.hello_label.text = 'Привет ' + self.name_input.text


class MainApp(App):

    def build(self):
        return MainWidget()


if __name__ == '__main__':
    app = MainApp()
    app.run()