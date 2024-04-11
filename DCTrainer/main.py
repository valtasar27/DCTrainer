import pyMeow as pm
import sys
from time import sleep
from gui import Menu
from values import Cheats
from configparser import ConfigParser

            
class Main:
    def __init__(self):
        
        self.menu = Menu()
        self.config = ConfigParser()
        
        try:
            with open("config.ini") as f:
                self.config.read_file(f)
            self.game = pm.open_process("deadcells.exe") #32 bits
            self.module = pm.get_module(self.game, "libhl.dll")['base']
            pm.overlay_init(
                exitKey=0x24,
                target="Dead Cells",
                title="test"
            )
        except Exception as e:
            sys.exit(e)
            
    def main_loop(self):
        while pm.overlay_loop():
            
            w_i = pm.get_window_info("Dead Cells")
            
            pm.begin_drawing()
            
            # FPS
            if self.config.getboolean('Main','Drawfps'):
                pm.draw_fps(posX=w_i[2] -w_i[2],
                            posY=w_i[3] -w_i[3] 
                            )
                
            if self.config.getboolean("Main","infhealth"):
                Cheats.write_health(self,self.game,self.module)
                
            if self.config.getboolean("Main","infcells"):
                Cheats.write_cells(self,self.game,self.module)
            
            if self.config.getboolean("Main","infcoins"):
                Cheats.write_coins(self,self.game,self.module)
            
            # the menu
            self.menu.check_draw()
            if self.menu.draw:   
                self.menu.draw_menu(self.config,w_i)
                
            pm.end_drawing()
    

    
triner = Main()
triner.main_loop()