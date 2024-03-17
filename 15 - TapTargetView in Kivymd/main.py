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
from kivymd.uix.taptargetview import MDTapTargetView

KV= '''
Screen:
    
    MDFloatingActionButton:
        id: button
        icon: "language-python"
        pos: 10, 10
        on_release: app.tap_target_start()
'''

class TapTargetView(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
            widget=screen.ids.button,
            title_text = "This is an python button",
            description_text = "Your Description Here",
            widget_position= "left_bottom",
        )
        return screen

    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()
TapTargetView().run()
