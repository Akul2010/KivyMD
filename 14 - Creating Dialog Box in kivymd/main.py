*********************************************************************
#You can use source codes as you want
#But You have to give our profile link in your code as comment
#Copy Below Codes and Paste in your codes Comment Section
*********************************************************************
#Github: https://github.com/vipinjangra
#Youtube: https://www.youtube.com/c/vipincoding/
#Website: http://vipincoding.graphy.com
#Facebook: https://www.facebook.com/vstutorialsss
#Instagram: https://www.instagram.com/vstutorials_
*********************************************************************

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

KV = '''
MDFloatLayout:

    MDFlatButton:
        text: "Click Here"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()       
'''
class Dialog(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Oops Connection Lost Please Reconnect!!!",
                radius=[20, 7, 20, 7],
            )
        self.dialog.open()
Dialog().run()
