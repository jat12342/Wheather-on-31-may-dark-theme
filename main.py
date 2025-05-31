from kivy.config import Config
Config.set('kivy', 'video', 'ffpyplayer')  # Important to set BEFORE importing other Kivy parts

from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: "vertical"

    MDLabel:
        text: "Video Player Example"
        halign: "center"
        size_hint_y: None
        height: dp(50)

    Video:
        source: "assets/v1.mp4"
        state: "play"
        options: {"eos": "loop"}
        allow_stretch: True
        keep_ratio: True
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
