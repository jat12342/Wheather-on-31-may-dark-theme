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
from kivy.utils import platform
from android.storage import primary_external_storage_path
import os
kv='''
Manager:
    Fir:
    Sec:        
<Fir>:
    id:s1
    name:'home'
    
    MDCarousel:
        id:mc1
        direction:'bottom'
        pos_hint:{'center_x':0.5,'center_y':0.6} 
        size_hint:1,0.5
      
            
   
    MDIconButton:
        icon:'refresh'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        size_hint:1,0.1
        md_bg_color:0,0,1,1
        on_press:app.cl()    
        




    





    MDTopAppBar:
        id:tb1
        pos_hint:{'top':1}
        title:'IMAGE DOWNLOADER'
        left_action_items:[['menu',lambda x:nd1.set_state('open')]]
        md_bg_color:0,0,1,1

    MDNavigationDrawer:
        id:nd1     
        
        ScrollView:
            
            MDBoxLayout:
                id:mdb1
                pos_hint:{'center_y':0.4}
                orientation:'vertical'
                spacing:30
                padding:10
                adaptive_height:True
                Image:
                    source:'assets/a1.png'
                    size_hint_y:None         
                    allow_stretch:True
                    keep_ratio:False                
                    height:'250dp'   
                
                
                MDLabel:
                    text:'Hello Users'   
                    font_name:'RobotoThin'
                    adaptive_height:True                                                                                                                                                                                                                      
                MDLabel:
                    text:'contact mail:- bhavishyarajput75@gmail.com'   
                    font_name:'RobotoThin'
                    adaptive_height:True   
                    font_size:24      
                                                                                                                                                                                                                                                                                                        
                MDLabel:
                    text:'developed by @ Bhavishya Rajput'   
                    font_name:'RobotoThin'
                    adaptive_height:True         
                                                                    
                                                                                                                          
                OneLineIconListItem:
                    text:'click to see'        
                    size_hint_y:None     
                   
                    on_press:app.youtube()
                   
                                                                                                                                                                                                            
                MDLabel:
                    text:'Thanks For @ Download'   
                    font_name:'RobotoThin'
                    adaptive_height:True   
                    font_size:50                                                               
                                                                                                        
                MDRectangleFlatButton:
                    text:'Download build.yml'
                    adaptive_height:True   
                    on_press:app.buy() 
        
     




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
        return self.b
        
    def on_start(self):
        if platform == 'android':
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
                        
      
        try:               
            self.urls ='https://api.unsplash.com/photos/random?query=mountain&client_id=TRIHpYC1opzKSS-FVooWkd55u6iExKUinZlIDmwwlnQ'  
            for i in range(0,5):                
                r1 = requests.get(self.urls).json()
                r2 = r1['urls']['regular']
                
                
                u=self.b.get_screen('home').ids.mc1 
                u2 =MDCard(on_press=lambda x,imgu=r2:self.dow(imgu))    
                
                as1=AsyncImage(source=r2,size_hint=(1,1),allow_stretch=True,keep_ratio=False)
               
                
                u.add_widget(u2)   
                u2.add_widget(as1)     
                                                                                         
                    
        except requests.exceptions.ConnectionError:
            self.b.get_screen('home').ids.mc1.add_widget(MDCard(MDLabel(text='NO INTERNET CONNECTION',font_style='H6')))            
            toast("No internet connection")
            
        except requests.exceptions.Timeout:
            toast("Request timed out")
        except requests.exceptions.HTTPError as e:
            toast(f"HTTP error: {e}")
        except FileNotFoundError:
            toast("Save location not found")
        except PermissionError:
            toast("Permission denied while saving")                            
                                          
                                        
        except Exception as e:
            toast(f'{e}')  
            
            for i in range(0,51):
                rr1=random.randint(1,10000)
                rr2 = f"https://picsum.photos/seed/{rr1}/600/400"
                rr=self.b.get_screen('home').ids.mc1
                rr3 =MDCard(on_press=lambda x,imgu=rr2:self.dow(imgu))
                rr4 =AsyncImage(source=rr2,size_hint=(1,1),allow_stretch=True,keep_ratio=False)
                
                rr.add_widget(rr3)
                rr3.add_widget(rr4)
                
                    
            
        
    def dow(self,link):
        try:
            r1 = requests.get(link)   
            folder = os.path.join(primary_external_storage_path(),'Download','MImag')
            ext = mimetypes.guess_extension(r1.headers.get('content-type', 'image/png'))
            lk=f'dow_{int(time.time())}{ext or ".png"}'
            if not os.path.exists(folder):
                os.makedirs(folder)        
                    
            filepath=os.path.join(folder,lk)                        
            if r1.status_code == 200:
                with open(filepath,'wb') as f:
                    f.write(r1.content)
                toast(f'Downloaded:-{filepath}')           
                         
            else:
                print('Error')                           
                                              
                
        except Exception as e:
            toast(f'{e}')               
        
    def thank(self):
        toast('RADHE-RADHE')    
        
            
    def cl(self):
        c1=self.b.get_screen('home').ids.mc1
        c1.clear_widgets() 
        try:          
            self.urls ='https://api.unsplash.com/photos/random?query=mountain&client_id=XQN5NtHS9OFD2Kv_AVM583EtWrS1UKdf4wns5PekfJg'
            for i in range(0,5):                
                r1 = requests.get(self.urls).json()
                r2 = r1['urls']['regular']
                
                
                u=self.b.get_screen('home').ids.mc1 
                u2 =MDCard(on_press=lambda x,imgu=r2:self.dow(imgu))    
                as1=AsyncImage(source=r2,size_hint=(1,1),allow_stretch=True,keep_ratio=False)
               
                
                u.add_widget(u2)   
                u2.add_widget(as1)
            toast('REFRESHED')   

        except requests.exceptions.ConnectionError:
            self.b.get_screen('home').ids.mc1.add_widget(MDCard(MDLabel(text='NO INTERNET CONNECTION',font_style='H6',text_color=(1,0,0,1))))
            
            toast("No internet connection")
            
        except requests.exceptions.Timeout:
            toast("Request timed out")
        except requests.exceptions.HTTPError as e:
            toast(f"HTTP error: {e}")
        except FileNotFoundError:
            toast("Save location not found")
        except PermissionError:
            toast("Permission denied while saving")           
                
                        
                                
                                                
                  
        except Exception as e:                    
            for i in range(0,51):
                rr1=random.randint(1,100000000000)
                rr2 = f"https://picsum.photos/seed/{rr1}/600/400"
                rr=self.b.get_screen('home').ids.mc1
                rr3 =MDCard(on_press=lambda x,imgu=rr2:self.dow(imgu))
                rr4 =AsyncImage(source=rr2,size_hint=(1,1),allow_stretch=True,keep_ratio=False)
                
                rr.add_widget(rr3)
                rr3.add_widget(rr4)      
            toast('REFRESH 2')                           


                                        
    def youtube(self):
        try:
            webbrowser.open('https://youtube.com/shorts/Mgx8ChaMluU?si=lwfb7gplyFhCOokR') 
                             

        except requests.exceptions.ConnectionError:
            toast('NO INTERNET CONNECTION')                                                                  
        except Exception as e:
            toast(str(e))                                                                              


    def buy(self):
        build1="""name: Build Kivy APK

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Build APK with Buildozer
        uses: digreatbrian/buildozer-action@v2
        with:
          buildozer-cmd: buildozer -v android debug
          work-dir: .  # Directory containing main.py and buildozer.spec

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: kivy-apk
          path: ./bin/*.apk
"""                                   
        try:
            folder = os.path.join(primary_external_storage_path(),'Download','build_yml')   
            f='build.txt' 
            if not os.path.exists(folder):
                os.makedirs(folder)
            fi=os.path.join(folder,f)
            with open(fi,'w') as f:
                f.write(build1)       
            toast('DOWNLOADED')                                                                                     
                                                            
        except Exception as e:
            toast(str(e))            










                
Demo().run()      
    
