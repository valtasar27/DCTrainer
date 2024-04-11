import pyMeow as pm
from misc import OffSets
from time import sleep

class Cheats:
    
    def write_health(self,game,module):
        try:
            pm.w_int(game,pm.pointer_chain_32(game,module + 0x00048184, OffSets.offsets_health),999999)
        except Exception:
            pass
            
    def write_cells(self,game,module):
        try:
            pm.w_int(game, pm.pointer_chain_32(game, module + 0x00048184, OffSets.offsets_cells),999999)
        except Exception:
            pass
            
    def write_coins(self,game,module):
        try:
            pm.w_int(game, pm.pointer_chain_32(game, module + 0x00048184, OffSets.offsets_money),999999)
        except Exception:
            pass