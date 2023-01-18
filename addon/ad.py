from aqt.utils import showInfo
from aqt.gui_hooks import browser_menus_did_init
from aqt.qt import *
from .toolbar import getMenu
from .config import gc


def setup_browser_menu(self):
    view = getMenu(self, gc("Browser menu used", "UWorld"))
    action = QAction(self)
    action.setText('UWorld')
    action.triggered.connect(lambda b=self: showInfo(text="""The UWorld QID to Anki add-on you downloaded from 
    Ankiweb is just a placeholder as explained on the <a href="https://ankiweb.net/shared/info/607963104">AnkiWeb 
    post</a>. To download the official beta add-on, sign up for an <a href="https://www.ankipalace.com/memberships">
    AnKing membership</a>. The membership includes this and <a href="https://www.ankipalace.com/membership-addons">
    many other add-ons</a>! """, textFormat="rich"))
    view.addAction(action)


browser_menus_did_init.append(setup_browser_menu)
