from imageview import *
from stringview import *
import papyon

class ProfileView:
    def __init__(self):
        self.email = StringView()
        self.nick = StringView()
        self.status = papyon.Presence.ONLINE
        self.dp = ImageView()
        self.music = StringView()
        #TODO