from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests


Builder.load_file('frontend.kv')

class FirstScreen(Screen):

    def get_image_link(self):
        print('Working...')
        # Get user input
        user_query = self.manager.current_screen.ids.user_query.text
        print(user_query)

        # Get wikipedia page
        page = wikipedia.WikipediaPage(user_query)
        link = page.images[0]
        return user_query, link

    def download_image(self):
        req = requests.get(self.get_image_link()[1], headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        req.status_code

        # Save photo
        path = "files/"+self.get_image_link()[0]+".jpg"
        with open(path, "wb") as file:
            file.write(req.content)
        return path

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()