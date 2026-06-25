
from cc3d import CompuCellSetup
        

from EMTphcco_1Steppables import InitialArrangementSteppable

CompuCellSetup.register_steppable(steppable=InitialArrangementSteppable(frequency=1))


        
# from EMTphcco_1Steppables import mesen_uptake_Steppable
# CompuCellSetup.register_steppable(steppable=mesen_uptake_Steppable(frequency=1))


        
from EMTphcco_1Steppables import TGFb_secretion_Steppable
CompuCellSetup.register_steppable(steppable=TGFb_secretion_Steppable(frequency=1))


        
from EMTphcco_1Steppables import BASELINE_PDL1_EXP_Steppable
CompuCellSetup.register_steppable(steppable=BASELINE_PDL1_EXP_Steppable(frequency=1))



        
from EMTphcco_1Steppables import TCELL_KILLINGSteppable
CompuCellSetup.register_steppable(steppable=TCELL_KILLINGSteppable(frequency=1))


        
# from EMTphcco_1Steppables import therapy_Steppable
# CompuCellSetup.register_steppable(steppable=therapy_Steppable(frequency=1))

CompuCellSetup.run()
