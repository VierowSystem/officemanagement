from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest
import json

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.status_label = Label(text='')
        login_button = Button(text='Login', size_hint=(None, None), size=(100, 40))
        login_button.bind(on_press=self.login)
        layout.add_widget(Label(text='Login Form'))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        layout.add_widget(self.status_label)
        self.add_widget(layout)

    def login(self, instance):
        # Perform login request and validation logic here
        # On successful login, switch to the home screen
        self.manager.current = 'home'
        self.manager.transition.direction = 'left'


class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.email_input = TextInput(hint_text='Email', multiline=False)
        self.status_label = Label(text='')
        register_button = Button(text='Register', size_hint=(None, None), size=(100, 40))
        register_button.bind(on_press=self.register)
        layout.add_widget(Label(text='Registration Form'))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.email_input)
        layout.add_widget(register_button)
        layout.add_widget(self.status_label)
        self.add_widget(layout)

    def register(self, instance):
        # Perform registration request and validation logic here
        # On successful registration, switch to the login screen
        self.manager.current = 'login'
        self.manager.transition.direction = 'right'


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        layout.add_widget(Label(text='Welcome to the Home Page'))
        self.add_widget(layout)


class MyApp(App):
    def build(self):
        # Create the screen manager and add screens to it
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(HomeScreen(name='home'))
        return sm


if __name__ == '__main__':
    MyApp().run()
