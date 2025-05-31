from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.toast.kivytoast.kivytoast import toast
import requests
import webbrowser
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image,AsyncImage
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton, MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDRoundFlatIconButton, MDRoundFlatButton, MDFloatingActionButton, MDIconButton
import requests
import time
import mimetypes
import random
from android.permissions import request_permissions, Permission
from kivy.animation import Animation
from kivy.uix.modalview import ModalView
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.list import MDList,OneLineListItem,OneLineIconListItem,IconLeftWidget




kv='''
Manager:
    Fir:
    Sec:     
<Fir>:
    id:s1
    name:'home'
    MDBottomNavigation:
        id:bon1
        pos_hint:{'bottom':1}
        panel_color:0,0.5,0.5,1
        text_color_active:1,0,0,1
        text_color_normal:0.7,0.7,0.7,1
        MDBottomNavigationItem:
            name:'home'
            text:'home'
            icon:'home'
            MDLabel:
                id:l1
                text:'ENTER CITY:-'
                font_style:'H6'
                pos_hint:{'center_x':0.55,'center_y':0.8}
              
            MDTextField:
                id:tf1
                font_style:'H6'
                hint_text:'Bhiwani'
                pos_hint:{'center_x':0.7,'center_y':0.8}
                size_hint_x:0.5
                
            MDIconButton:
                id:b1
                icon:'magnify'                    
                pos_hint:{'center_x':0.5,'center_y':0.7}
                size_hint_x:0.5
                on_press:app.s()
                                            
                
                
              
                
                
                
        MDBottomNavigationItem:
            name:'setting'
            text:'setting'
            icon:'cog'
            MDScrollView:
                pos_hint:{'center_x':0.5,'center_y':0.5}
                size_hint:1,0.8
                MDList:
                    id:ml1
                    OneLineListItem:
                        id:ol1
                        text:'Light Mode'   
                        bold:True
                        Switch:
                            id:s1
                            pos_hint:{'center_x':0.8,'center_y':0.5}
                            on_active:app.swi(self.active)
                            
                    OneLineIconListItem:
                        id:ol2
                        text:'About'   
                        bold:True
                        on_press:app.info()
                        IconLeftWidget:
                            icon:'information-outline' 
                                                                                                 
                                          
                



    MDTopAppBar:
        id:ta1
        pos_hint:{'top':1}
        title:'WEATHER'
        
        left_action_items:[['menu',lambda x:nd1.set_state('open')]]

    MDNavigationDrawer:
        id: nd1

        ScrollView:

            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: "8dp"
                padding: "8dp"
                pos_hint: {'top': 1}
    
                Image:
                    source: "assets/a1.png"
                    size_hint: (1, None)
                    height: "120dp"
                    allow_stretch: True
                    keep_ratio: False
    
                MDLabel:
                    text: "Hello User"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
    
                MDLabel:
                    text: "Contact mail:- bhavishyarajput75@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
    
                MDLabel:
                    text: "Developer Name:- Bhavishya"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
      
       


            
        
            
    






'''














class Manager(ScreenManager):
    pass

class Fir(Screen):
    pass

class Sec(Screen):
    pass






class Demo(MDApp):
    def build(self):
        self.b=Builder.load_string(kv)   
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
       
        return self.b
        
    def s(self):
        city=self.b.get_screen('home').ids.tf1.text  
        try:                                  
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3c4d50ab986a076d3460c760366e6eee'            
            r1=requests.get(url).json()
            if r1['cod'] == 200:             
                tem=int(float(r1['main']['temp']-273.15))
                temp=f'{tem}°C'
                main1=r1['weather'][0]['main']
                main=f"       {r1['weather'][0]['main']}"
                humi=f"HUMIDITY {r1['main']['humidity']}%"
                pre=f"PRESSURE {r1['main']['pressure']} hpa"
                ws=f"WIND_SPEED { int(r1['wind']['speed']*3.6)} kmp/h" 
                
                popup = ModalView(size_hint=(None, None), size=("300dp", "500dp"), auto_dismiss=True)
                
                s1=ScrollView()
                m =MDCard(md_bg_color=(0.1,0.2,0.3,1))
    
                b1=BoxLayout(orientation='vertical',size_hint_y=None,spacing='10dp',padding='20dp')                    

                b1.bind(minimum_height=b1.setter('height')) 
                so1='assets/tl.png'
                so2='assets/th.png'
        
                i1 = Image(size_hint_y=None, height='150dp', allow_stretch=True, keep_ratio=True, pos_hint={'center_x':0.5})
                if int(tem) <= 15:
                    i1.source=so1
                else:
                    i1.source=so2                    
                    
        
                l1=MDLabel(text='WEATHER',pos_hint={'center_x':0.77},font_style='H4')
                l2=MDLabel(text=str(temp),pos_hint={'center_x':0.8},font_style='H4')
                o1=OneLineIconListItem(MDLabel(text=main,pos_hint={'center_x':0.9,'center_y':0.5},font_style='Caption'))
                ic=IconLeftWidget()
                
                if main1 == 'Clear':
                    ic.icon='weather-sunny'     
                elif main1== 'Clouds':
                    ic.icon='weather-cloudy'                                 
                elif main1== 'Rain':
                    ic.icon='gauge'  
                    
                o2=OneLineIconListItem(MDLabel(text=humi,pos_hint={'center_x':0.9,'center_y':0.5},font_style='Caption'),IconLeftWidget(icon='water-percent'))
                o3=OneLineIconListItem(MDLabel(text=pre,pos_hint={'center_x':0.9,'center_y':0.5},font_style='Caption'),IconLeftWidget(icon='water-pump'))                
                o4=OneLineIconListItem(MDLabel(text=ws,pos_hint={'center_x':0.9,'center_y':0.5},font_style='Caption'),IconLeftWidget(icon='weather-windy'))                          
                        
                                         
                                                                           
                          
                o1.add_widget(ic)                      
                b1.add_widget(i1)
                b1.add_widget(l2)
                              
                b1.add_widget(o1)    
                b1.add_widget(o2)
                b1.add_widget(o3)
                b1.add_widget(o4)
                s1.add_widget(b1)
                m.add_widget(s1)
                popup.add_widget(m)   
                popup.open() 
                
            else:
                toast('City Not Found')           
                
                     
                               
        except requests.exceptions.HTTPError as e:
            toast(f" HTTP Error: {e}")
        except requests.exceptions.ConnectionError:
            toast("NO INTERNET")
        except requests.exceptions.Timeout:
            toast("REQUESTS TIMEOUT")
        except requests.exceptions.TooManyRedirects:
            toast("TOO Many REQUESTS")
        except requests.exceptions.URLRequired:
            toast("URL NOT FOUND")
        except requests.exceptions.RequestException as e:
            toast(f" {e}")
        except Exception as e:
            toast(f"{e}")
            
        
    
        
        
        
    def theme(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"              
        
                   
    def swi(self,value):
        if value:
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Cyan"
            self.b.get_screen('home').ids.bon1.panel_color=(0,1,1,1)
            
            toast('Light Mode')
            
        else:
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Teal"
            self.b.get_screen('home').ids.bon1.panel_color=(0,0.5,0.5,1)
            
            toast('Dark Mode') 
            
    def info(self):
        pop=ModalView(size_hint=(None,None),size=('250dp','400dp'),auto_dismiss=True)      
        m1=MDCard()
        b1=BoxLayout(size_hint_y=None,orientation='vertical',height='400dp',pos_hint={'top':1},spacing='1dp',padding='5dp')
        l1=MDLabel(text='Developed by Bhavishya Rajput')
        l2=MDLabel(text='launch_first_version @ may 31 2025')
        l3=OneLineIconListItem(text='@youtube')
        ic1=IconLeftWidget(icon='youtube')
        ic1.theme_text_color='Custom'
        ic1.text_color=(1,0,0,1)
        l3.bind(on_press=self.y)
        l3.add_widget(ic1)                                     
        l4=MDLabel(text='This @pp help to find Weather',font_style='Caption')
        l5=MDLabel(text='Users_########################________ An work of Calculator Screen Under Construction when the the calc screen added you notify',font_style='Caption')
        

        b1.add_widget(l1)     
        b1.add_widget(l2)
        b1.add_widget(l3)
        b1.add_widget(l4)
        b1.add_widget(l5)
        m1.add_widget(b1)             
        pop.add_widget(m1)
        pop.open()                                                                                                                                                 
    def y(self,*args):
      webbrowser.open('https://youtube.com/shorts/Mgx8ChaMluU?si=aW263HsrojPAGaHP')                                                                                                                              
                                                
                                                        
Demo().run()                                                                        
