from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
import wikipedia,requests

Builder.load_file('frontend.kv')
class FirstScreen(Screen):
    def search_image(self):
        #get user query
        query=self.manager.current_screen.ids.user_query.text

        #fetching details
        page = wikipedia.page(query, auto_suggest=False, redirect=True, preload=False)

        image_links=page.images[0]

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        #downloading the image


        req= requests.get(image_links,headers=headers)
        with open('files/image.jpg','wb') as file:
            file.write(req.content)

        self.manager.current_screen.ids.img.source = 'files/image.jpg'
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()