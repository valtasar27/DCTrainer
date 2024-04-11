import pyMeow as pm
from time import sleep


class Menu:
    
    def __init__(self):
        
        self.draw = False
        self.menu_key = 0x2D
        
    def draw_menu(self,config,w_i):
        
        window = pm.gui_window_box(
            posX=w_i[2] - 200,
            posY=w_i[3] - w_i[3],
            width=200,
            height=200,
            title="DC Trainer"
        )
        
        if window:
            self.draw = False
            pm.toggle_mouse()
            
        config["Main"]["drawFPS"] = str(pm.gui_check_box(
            posX=w_i[2]-180,
            posY=w_i[3]-w_i[3]+43,
            width=18,
            height=18,
            text="Show fps",
            checked=config.getboolean("Main", "drawFPS")
        ))
        
        config["Main"]["infhealth"] = str(pm.gui_check_box(
            posX=w_i[2]-180,
            posY=w_i[3]-w_i[3]+73,
            width=18,
            height=18,
            text="Infinite Health",
            checked=config.getboolean("Main","infhealth")
        ))
        
        config["Main"]["infcells"] = str(pm.gui_check_box(
            posX=w_i[2]-180,
            posY=w_i[3]-w_i[3]+103,
            width=18,
            height=18,
            text="Infinite Cells",
            checked=config.getboolean("Main","infcells")
        ))
        
        config["Main"]["infcoins"] = str(pm.gui_check_box(
            posX=w_i[2]-180,
            posY=w_i[3]-w_i[3]+133,
            width=18,
            height=18,
            text="Infinite Coins",
            checked=config.getboolean("Main","infcoins")
        ))
        
            
        
    def check_draw(self):
        if pm.key_pressed(self.menu_key):
            self.draw = not self.draw
            pm.toggle_mouse()
            sleep(0.15)