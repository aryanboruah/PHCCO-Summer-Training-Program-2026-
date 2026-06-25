from cc3d.core.PySteppables import *
import numpy as np
import math
import random
import os

class InitialArrangementSteppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)
        
 

    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        
        #Epithelial layout
        
        # center_x, center_y = 200, 200
        
        # params = {
        
        # 'cell_count_ctrl' : [75,100,150,200,225] 
        
        # }
        
        # self.epi_count = params["cell_count_ctrl"]
        # self.hyb_count = params["cell_count_ctrl"]
        # self.mesen_count = params["cell_count_ctrl"]
        tot_cells = 500
        epi_count = 0
                
        # if epi_count >= int(0.45*tot_cells):
            # break      #stop placing 
                
                # dx = x - center_x
                # dy = y - center_y
                # dist = math.sqrt(dx**2 + dy**2)
                
                # MESEN cells = inner core
                
        for x in range(300, 395, 5):
            for y in range(2, 96, 5):
                cell = self.newCell(self.EPI)
                self.cellField[x:x+5, y:y+5, 0] = cell
    
    # ── Region 2: HYB cells (225-250, 0-100) ──
        for x in range(280, 300, 8):
            for y in range(2, 96, 8):
                cell = self.newCell(self.HYB)
                self.cellField[x:x+5, y:y+5, 0] = cell
    
    # ── Region 3: MESEN cells (200-225, 0-100) ──
        for x in range(240, 280, 7):
            for y in range(2, 96, 7):
                cell = self.newCell(self.MESEN)
                self.cellField[x:x+5, y:y+5, 0] = cell
                
                
         
        
        # for x in range(98,102,4):
            # for y in range(50,54,4):
                # cell = self.newCell(self.TCELL)  
                # self.cellField[x:x+4,y:y+4,0] = cell   

        used_positions = set()

        while len(used_positions) < 4:

            x = random.randint(160, 180)
            y = random.randint(0, 96)

            pos = (x, y)

            if pos not in used_positions:

                used_positions.add(pos)

                cell = self.newCell(self.TCELL)

                self.cellField[x:x+4, y:y+4, 0] = cell       
                
                
            
        # if epi_count >= int(0.45*tot_cells):
            # break                   #come out of ol  
  
    
      

    def step(self, mcs):
    
        
    
        # counts = {
            # self.EPI:   0,
            # self.HYB:   0,
            # self.MESEN: 0,
            # self.TCELL: 0
        # }
        
        # for cell in self.cell_list:
            # if cell.type in counts:
                # counts[cell.type] += 1
        
        
        # print(f"MCS={mcs} | EPI={counts[self.EPI]} | HYB={counts[self.HYB]} | MESEN={counts[self.MESEN]}")
        return 0
        
        
        
        
        
    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS


  """








# IFNG_THRESHOLD = 1000   `
# CHEMO_SECRETION = 300  # how much Chemokine MESEN releases


        
# class mesen_uptake_Steppable(SteppableBasePy):
    # def __init__(self, frequency=1):
        # '''
        # constructor
        # '''
        # SteppableBasePy.__init__(self, frequency)
        # # PLACE YOUR CODE BELOW THIS LINE
        

    # def start(self):
        # '''
        # called once before first MCS
        # '''
        # # PLACE YOUR CODE BELOW THIS LINE
        
        # # print("mesen_uptake_Steppable: This function is called once before simulation")
        # for cell in self.cell_list:
            # cell.dict['ifng_accumulated'] = 0.0
            # cell.dict['secreting_chemo']  = False
        
        # # for cell in self.cell_list:
            # # if cell.type == self.MESEN:
          
                # # cd = self.chemotaxisPlugin.addChemotaxisData(cell, "Chemokine")
                # # cd.setLambda(20.0)
                # # cd.assignChemotactTowardsVectorTypes([self.MESEN])
                
        # self.ifng_chemo_log = open("D:/compucell/CompuCell3D-py3-64bit/Output_logs/IFNg_uptake_mesen_release_chemo_log.csv", "w")
        # self.ifng_chemo_log.write("MCS,CellID,Cell_Type,Accumulated_IFNg,Threshold,Status\n")
    
    # def update_ifng_uptake(self,mcs):

        # secretor_ifng = self.get_field_secretor("IFNg")

        # for cell in self.cell_list_by_type(self.MESEN):

            # tot_ifng = abs(
                # secretor_ifng.uptakeInsideCellTotalCount(
                    # cell, 20.0, 0.2
                # ).tot_amount
            # )

            # secretor_ifng.uptakeInsideCell(
                # cell, 20.0, 0.2
            # )

            # cell.dict['ifng_accumulated'] += tot_ifng
            # status = "not yet secreting chemokine"
            
            # if cell.dict['ifng_accumulated'] >= IFNG_THRESHOLD:
                
                
                # cell.dict['secreting_chemo'] = True
                
                # status = "secreting chemokine"

                # line = (
                # f"MCS={mcs} | MESEN {cell.id} | "
                # f"accumulated={cell.dict['ifng_accumulated']:.2f} | "
                # f"secreting Chemokine"
            # )
                # print(line)
              
                    
                # self.ifng_chemo_log.write(
                    # f"{mcs},{cell.id},{cell.dict['ifng_accumulated']:.2f},"
                    # f"{IFNG_THRESHOLD} | {status} \n"
                # )
            # else:

                # line = (
                    # f"MCS={mcs} | MESEN {cell.id} | "
                    # f"accumulated={cell.dict['ifng_accumulated']:.2f} / "
                    # f"{IFNG_THRESHOLD} | {status}"
                # )
                
                # print(line)
              
                    
                # self.ifng_chemo_log.write(
                    # f"{mcs},{cell.id},{cell.dict['ifng_accumulated']:.2f},"
                    # f"{IFNG_THRESHOLD} | {status} \n"
                # )
    
    # def secrete_chemokine(self):

        # secretor_chemo = self.get_field_secretor("Chemokine")

        # for cell in self.cell_list_by_type(self.MESEN):

            # if cell.dict['secreting_chemo']:

                # secretor_chemo.secreteInsideCell(cell,CHEMO_SECRETION)

    # def step(self, mcs):    # all the fucntion pre defined are called in the step fucntion
        
        # if mcs % 50 == 0:
            # self.update_ifng_uptake(mcs)

        # self.secrete_chemokine()
            
                


    # def finish(self):
        # '''
        # this function may be called at the end of simulation - used very infrequently though
        # '''        
        # # PLACE YOUR CODE BELOW THIS LINE
        
        # return

    # def on_stop(self):
        # '''
        # this gets called each time user stops simulation
        # '''        
        # # PLACE YOUR CODE BELOW THIS LINE
        
        # return



















TGF_SECRETION = 100  #how much tgfb MESEN releases
TGF_THRESHOLD_EPI = 5
TGF_THRESHOLD_HYB = 9
        
class TGFb_secretion_Steppable(SteppableBasePy): #the secretion is induced by IFNg
    def __init__(self, frequency=1):  # starting this steppable again would make every time the cell.dict['tgfb_accumulated'] = 0.0 which is not true. 
        '''
        constructor
        '''
        SteppableBasePy.__init__(self, frequency)
        # PLACE YOUR CODE BELOW THIS LINE
        

    def start(self):
        '''
        called once before first MCS
        '''
        # PLACE YOUR CODE BELOW THIS LINE
        for cell in self.cell_list_by_type(self.EPI, self.HYB):
            cell.dict['tgfb_accumulated'] = 0.0
            cell.dict['secreting_tgfb']  = False
            
        # self.ifng_rel_tgf_log = open("D:/compucell/CompuCell3D-py3-64bit/Output_logs/IFNg_uptake_mesen_release_tgfb_log.csv", "w")
        self.tgfb_switch_log = open("D:/compucell/CompuCell3D-py3-64bit/Output_logs/TGFb_uptake_EPI_HYB_switching_log.csv", "w")
        
        # self.ifng_rel_tgf_log.write("MCS,CellID,Cell_Type,Accumulated_IFNg,Threshold,Status\n")    
        self.tgfb_switch_log.write("MCS,CellID,Cell_Type,Accumulated_TGFb,Threshold,Status\n")    
        
        # print("TGFb_secretion_Steppable: This function is called once before simulation")
    
    
    
    
    # def tgfb_secretion(self,mcs):
        
        # secretor_ifng  = self.get_field_secretor("IFNg")        
        # secretor_tgfb = self.get_field_secretor("TGFb")

        # for cell in self.cell_list_by_type(self.MESEN):
                        
            # # accumulated = cell.dict['ifng_accumulated']  # inherited via cell.dict, no class inheritance needed
            # tot_ifng = abs(secretor_ifng.uptakeInsideCellTotalCount(cell, 20.0, 0.2).tot_amount)

            # secretor_ifng.uptakeInsideCell(
                # cell, 20.0, 0.2)
            
            # status = "not yet secreting TGF"
            
            # # Step 3 — check threshold
            # cell.dict['ifng_accumulated'] += tot_ifng
        
            
            # if cell.dict['ifng_accumulated'] >= IFNG_THRESHOLD:
           
                
                # # mark as secreting
                # cell.dict['secreting_tgfb'] = True
                
                # # secrete Chemokine
                # secretor_tgfb.secreteInsideCell(cell, TGF_SECRETION)
                # status = "secreting TGFb"
    
                # if mcs % 100 == 0:
                    
                    
                    
                    # line = (f"MCS={mcs} | MESEN {cell.id} | "
                          # f"accumulated={cell.dict['ifng_accumulated']:.2f}, /"
                          # f"{IFNG_THRESHOLD} | {status}")
                          
                    # print(line)
              
                    
                    # self.ifng_rel_tgf_log.write(
                        # f"{mcs},{cell.id},{cell.type}{cell.dict['ifng_accumulated']:.2f},"
                        # f"{IFNG_THRESHOLD}, {status} \n"
                    # )
                          
                    
            # else:
                # if mcs % 100 == 0:
                    # line = (f"MCS={mcs} | MESEN {cell.id} |"
                          # f"accumulated={cell.dict['ifng_accumulated']:.2f} / "
                          # f"{IFNG_THRESHOLD} | {status}")
                          
                    # print(line)
                    # self.ifng_rel_tgf_log.write(
                        # f"{mcs},{cell.id},{cell.type},{cell.dict['ifng_accumulated']:.2f},"
                        # f"{IFNG_THRESHOLD}, {status}\n"
                    # )      
                          
                          
        # if mcs % 100 == 0:
            # self.ifng_rel_tgf_log.flush()
    
        return 0
    
    
    
    def switching_ETH_HTM(self,mcs):
        
        #Uptake by hybrid and epithelial and switching  
       
        secretor_tgfb = self.get_field_secretor("TGFb")
        
        for cell in self.cell_list_by_type(self.EPI):
            
            # Step 1 — measure IFNg uptake this MCS
            tot_tgfb = abs(secretor_tgfb.uptakeInsideCellTotalCount(
                cell, 20.0, 0.2).tot_amount)
            secretor_tgfb.uptakeInsideCell(cell, 20.0, 0.2)
            
            # Step 2 — ADD to cumulative total
            cell.dict['tgfb_accumulated'] += round(tot_tgfb)
            
            status = "not switching"
            
            # Step 3 — check threshold
            if cell.dict['tgfb_accumulated'] >= TGF_THRESHOLD_EPI:
                
                # mark as secreting
                cell.dict['secreting_tgfb'] = True  
                status = "switching happening from EPI to HYB!"
                
                cell.type = self.HYB
            if mcs % 100 == 0:
                line = (f"MCS={mcs} | EPI {cell.id} | "
                      f"accumulated={cell.dict['tgfb_accumulated']:.2f} | "
                      f" {status}")
                print(line)
                
                self.tgfb_switch_log.write(
                    f"{mcs},{cell.id},{cell.type},{cell.dict['tgfb_accumulated']:.2f},"
                    f"{TGF_THRESHOLD_EPI}, {status}\n"
                )
                    
                
        for cell in self.cell_list_by_type(self.HYB):
            
            tot_tgfb = abs(secretor_tgfb.uptakeInsideCellTotalCount(
                cell, 20.0, 0.2).tot_amount)
            secretor_tgfb.uptakeInsideCell(cell, 10.0, 0.2)
            
            # Step 2 — ADD to cumulative total
            cell.dict['tgfb_accumulated'] += round(tot_tgfb)
            status = "not switching"
            
            # Step 3 — check threshold
            if cell.dict['tgfb_accumulated'] > TGF_THRESHOLD_HYB:
                
                # mark as secreting
                cell.dict['secreting_tgfb'] = True
                status = "switching happening from HYB to MESEN! "
                
                cell.type = self.MESEN
            if mcs % 100 == 0:
                line = (f"MCS={mcs} | HYB {cell.id} " 
                      f"accumulated={cell.dict['tgfb_accumulated']:.2f}, "
                      f"{status}")
                      
                      
                self.tgfb_switch_log.write(
                    f"{mcs},{cell.id},{cell.type},{cell.dict['tgfb_accumulated']:.2f},"
                    f"{TGF_THRESHOLD_HYB}, {status}\n"
                )      
        
        if mcs % 100 == 0:
            self.tgfb_switch_log.flush()
    
    def step(self, mcs):
        '''
        called every MCS or every "frequency" MCS (depending how it was instantiated in the main Python file)
        '''
        # PLACE YOUR CODE BELOW THIS LINE
                
        # self.tgfb_secretion(mcs)
            
        if mcs % 50 == 0:
            
            self.switching_ETH_HTM(mcs)
                          
                          
        #Uptake by hybrid and epithelial and switching              
                          
       
            
                
                          
                          

    def finish(self):
        '''
        this function may be called at the end of simulation - used very infrequently though
        '''        
        # PLACE YOUR CODE BELOW THIS LINE
        
        return

    def on_stop(self):
        '''
        this gets called each time user stops simulation
        '''        
        # PLACE YOUR CODE BELOW THIS LINE
        
        return



PDL1_MIN_IFNG_TO_RESPOND_MESEN = 40.0     # minimal cumulative IFNg before PD-L1 starts changing
PDL1_MIN_IFNG_TO_RESPOND_HYB = 100.0     # minimal cumulative IFNg before PD-L1 starts changing
PDL1_MIN_IFNG_TO_RESPOND_EPI = 100.0     # minimal cumulative IFNg before PD-L1 starts changing

# PDL1_RATE = {1: 0.1, 2: 0.1, 3: 0.1}   EPI=1, HYB=2, MESEN=3 → adjust to match your XML TypeIds
PDL1_RATE_MESEN = 0.1
PDL1_RATE_HYB = 0.1
PDL1_RATE_EPI = 0.1

PDL1_MAX_MESEN  = 60.0                   # cap on expression
PDL1_MAX_HYB = 100.0
PDL1_MAX_EPI = 100.0 


        
class BASELINE_PDL1_EXP_Steppable(SteppableBasePy):
    def __init__(self, frequency=1):
        '''
        constructor
        '''
        SteppableBasePy.__init__(self, frequency)
        # PLACE YOUR CODE BELOW THIS LINE
        

    def start(self):
        
        for cell in self.cell_list:
            if cell.type == self.EPI:
                cell.dict['PDL1_level'] = 10.0   # receptor expression level
            if cell.type == self.HYB:
                cell.dict["PDL1_level"] = 20.0
            if cell.type == self.MESEN:
                cell.dict["PDL1_level"] = 30.0
        
            cell.dict["ifng_cumulative"] = 0.0   # for each cell in the simulation 
            
        self.PDL1_expression_log = open("D:/compucell/CompuCell3D-py3-64bit/Output_logs/PDL1_expression_log.csv", "w")     
        
        self.PDL1_expression_log.write("MCS,CellID,Cell_Type,PDL1_level\n")    
                # cap at max expression
                # cell.dict['PDL1_level'] = min(cell.dict['PDL1_level'], 100.0)
    
    
    def mesen_pdl1(self,mcs):
        
        
        secretor_ifng = self.get_field_secretor("IFNg")
    
        for cell in self.cell_list:
            if cell.type == self.MESEN:  # checks for cells except t-cells 
            
                field = self.field.IFNg
                
                tot_ifng = abs(secretor_ifng.uptakeInsideCellTotalCount(
                    cell, 10.0, 0.02).tot_amount)
                     
                secretor_ifng.uptakeInsideCell(cell, 20.0, 0.02)
                
                
                
                # PD-L1 upregulated by IFNg exposure (biologically accurate!)
                cell.dict['ifng_cumulative'] += tot_ifng   # for each cell
            
            # ── only respond once minimal exposure threshold crossed ──
                if cell.dict['ifng_cumulative'] >= PDL1_MIN_IFNG_TO_RESPOND_MESEN:
                    
                    rate = PDL1_RATE_MESEN
                    cell.dict['PDL1_level'] += round(tot_ifng * rate)
                    
                    # cap at max expression
                    cell.dict['PDL1_level'] = min(cell.dict['PDL1_level'], PDL1_MAX_MESEN)
                    
                    
                if mcs % 100 == 0:
                    print(f"MCS={mcs} | {cell.type} {cell.id} | "
                          f"ifng_cumulative={cell.dict['ifng_cumulative']:.2f} | "
                          f"PDL1={cell.dict['PDL1_level']:.2f}")
                      
                    self.PDL1_expression_log.write(
                        f"{mcs},{cell.id},{cell.type},{cell.dict['PDL1_level']:.2f}\n"
                    )            
    
        
    def hyb_pdl1(self,mcs):
        
        secretor_ifng = self.get_field_secretor("IFNg")
    
        for cell in self.cell_list:
            if cell.type == self.HYB:  # cheks for cells except t-cells 
            
                field = self.field.IFNg
                
                tot_ifng = abs(secretor_ifng.uptakeInsideCellTotalCount(
                    cell, 20.0, 0.02).tot_amount)
                     
                secretor_ifng.uptakeInsideCell(cell, 20.0, 0.02)
                
                
                
                # PD-L1 upregulated by IFNg exposure (biologically accurate!)
                cell.dict['ifng_cumulative'] += tot_ifng   # for each cell
            
            # ── only respond once minimal exposure threshold crossed ──
                if cell.dict['ifng_cumulative'] >= PDL1_MIN_IFNG_TO_RESPOND_HYB:
                    
                    rate = PDL1_RATE_HYB
                    cell.dict['PDL1_level'] += round(tot_ifng * rate)
                    
                    # cap at max expression
                    cell.dict['PDL1_level'] = min(cell.dict['PDL1_level'], PDL1_MAX_HYB)
                    
                if mcs % 100 == 0:
                    print(f"MCS={mcs} | {cell.type} {cell.id} | "
                          f"ifng_cumulative={cell.dict['ifng_cumulative']:.2f} | "
                          f"PDL1={cell.dict['PDL1_level']:.2f}")
                          
                    self.PDL1_expression_log.write(
                        f"{mcs},{cell.id},{cell.type},{cell.dict['PDL1_level']:.2f}\n"
                    )            
                        
                    
                    
    def epi_pdl1(self,mcs):
        
        secretor_ifng = self.get_field_secretor("IFNg")
    
        for cell in self.cell_list:
            if cell.type == self.EPI:  # cheks for cells except t-cells 
            
                field = self.field.IFNg
                
                tot_ifng = abs(secretor_ifng.uptakeInsideCellTotalCount(
                    cell, 20.0, 0.02).tot_amount)
                     
                secretor_ifng.uptakeInsideCell(cell, 20.0, 0.02)
                
                
                
                # PD-L1 upregulated by IFNg exposure (biologically accurate!)
                cell.dict['ifng_cumulative'] += tot_ifng   # for each cell
            
            # ── only respond once minimal exposure threshold crossed ──
                if cell.dict['ifng_cumulative'] >= PDL1_MIN_IFNG_TO_RESPOND_EPI:
                    
                    rate = PDL1_RATE_EPI
                    cell.dict['PDL1_level'] += round(tot_ifng * rate)
                    
                    # cap at max expression
                    cell.dict['PDL1_level'] = min(cell.dict['PDL1_level'], PDL1_MAX_EPI)
                    
                if mcs % 100 == 0:
                    print(f"MCS={mcs} | {cell.type} {cell.id} | "
                          f"ifng_cumulative={cell.dict['ifng_cumulative']:.2f} | "
                          f"PDL1={cell.dict['PDL1_level']:.2f}")
                          
                    self.PDL1_expression_log.write(
                        f"{mcs},{cell.id},{cell.type},{cell.dict['PDL1_level']:.2f}\n"
                    )            
        
    def step(self, mcs):
        '''
        called every MCS or every "frequency" MCS (depending how it was instantiated in the main Python file)
        '''
        # PLACE YOUR CODE BELOW THIS LINE
        
                
        # for cell in self.cell_list:
            # print("CELL ID=",cell.id, " CELL TYPE=",cell.type," volume=",cell.volume)
            
            
        self.mesen_pdl1(mcs)
        
        self.hyb_pdl1(mcs)
        
        self.epi_pdl1(mcs)
        
        counts = {
            self.EPI:   0,
            self.HYB:   0,
            self.MESEN: 0,
            self.TCELL: 0
        }
        
        for cell in self.cell_list:
            if cell.type in counts:
                counts[cell.type] += 1
            
            
            
          

    def finish(self):
        '''
        this function may be called at the end of simulation - used very infrequently though
        '''        
        # PLACE YOUR CODE BELOW THIS LINE
        self.PDL1_expression_log.close()
        
        return

    def on_stop(self):
        '''
        this gets called each time user stops simulation
        '''        
        # PLACE YOUR CODE BELOW THIS LINE
        
        return
  

PDL1_SUPPRESSION_THRESHOLD_MESEN = 50.0
PDL1_SUPPRESSION_THRESHOLD_HYB = 40.0
PDL1_SUPPRESSION_THRESHOLD_EPI = 30.0


  
        
class TCELL_KILLINGSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        '''
        constructor
        '''
        SteppableBasePy.__init__(self, frequency)
        # PLACE YOUR CODE BELOW THIS LINE
        

    def start(self):
        '''
        called once before first MCS
        '''
        # PLACE YOUR CODE BELOW THIS LINE
        
        print("TCELL_KILLINGSteppable: This function is called once before simulation")
        for cell in self.cell_list_by_type(self.TCELL):
            
            cell.dict['touching_mesen'] = False
            cell.dict['touching_hyb'] = False
            cell.dict['touching_epi'] = False
            
        for cell in self.cell_list:
         
            cell.dict['marked_for_death'] = False    
            
            
            
            
        self.plot_win = self.add_new_plot_window(title='EMT Switching',
                                                 x_axis_title='MCS',
                                                 y_axis_title='Cell number', x_scale_type='linear', y_scale_type='linear',
                                                 grid=True,
                                                 config_options={'legend': True}
                                                  )
        
        self.plot_win.add_plot("MESENCHYME", style='Lines', color='yellow', size=2)
        self.plot_win.add_plot("HYBRID", style='Lines', color='green', size=2)
        self.plot_win.add_plot("EPITHELIAL", style='Lines', color='blue', size=2)
            # self.plot_win.add_plot("MSur", style='Dots', color='green', size=1)
            
            
            
        
    def touchMesenCell(self, mcs):
        
        
        for cell in self.cell_list:
            cell.dict['marked_for_death'] = False
        # cells_to_delete = []  collect first, delete after loop
        cells_to_delete = set()
        
        
        
        for cell in self.cell_list_by_type(self.TCELL):
            for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                if neighbor: #Ensure we are not looking at the Medium
                    if neighbor.type == self.MESEN:
                        
                        pdl1_level   = neighbor.dict.get('PDL1_level', 0.0)
                        
                        if cell.dict['touching_mesen'] == False:
                            cell.dict['touching_mesen'] = True
                            
                        if pdl1_level >= PDL1_SUPPRESSION_THRESHOLD_MESEN:
                            pass
                            # print(f"MCS={mcs} , TCell {cell.id} SUPPRESSED by PD-L1={pdl1_level:.2f}")
                        
                    
                        else:
                        # TCell kills MESEN — shrink it
                                # neighbor.targetVolume = 0
                                # neighbur.lambdaVolume = 50.0 
                                if neighbor.dict['marked_for_death']:
                                    continue

                                neighbor.dict['marked_for_death'] = True
                                cells_to_delete.add(neighbor)
                                # cells_to_delete.append(neighbor)
                             
                                if mcs % 50 == 0:
                                    print(f"MCS={mcs} | TCell {cell.id} KILLING MESEN {neighbor.id}")
                                    # print(f"MCS={mcs} , TCell {cell.id} KILLING MESEN {neighbor.id} , "
                                              # f"targetVolume={neighbor.targetVolume}")
                            
                    if neighbor.type == self.HYB:
                        
                        pdl1_level   = neighbor.dict.get('PDL1_level', 0.0)
                        
                        if cell.dict['touching_hyb'] == False:
                            cell.dict['touching_hyb'] = True
                            
                            
                        if pdl1_level >= PDL1_SUPPRESSION_THRESHOLD_HYB:
                            pass
                        
                    
                        else:
                        # TCell kills MESEN — shrink it
               
                            # neighbor.targetVolume = 0
                            # neighbur.lambdaVolume = 50.0 
                            # cells_to_delete.append(neighbor)
                            if neighbor.dict['marked_for_death']:
                                    continue

                            neighbor.dict['marked_for_death'] = True
                            cells_to_delete.add(neighbor)
                                
                                    
                                      
        # delete AFTER loop to avoid modifying list while iterating
        # for cell in cells_to_delete:
            # self.delete_cell(cell)                              
        for dead_cell in cells_to_delete:
            self.delete_cell(dead_cell)                                  
                       

                                      
                                      
                                      
                                      
                                      
                            

    def step(self, mcs):        
        '''
        called every MCS or every "frequency" MCS (depending how it was instantiated in the main Python file)
        '''
        # PLACE YOUR CODE BELOW THIS LINE
        
        self.touchMesenCell(mcs)
        
        counts = {
            self.EPI:   0,
            self.HYB:   0,
            self.MESEN: 0,
            self.TCELL: 0
        }
        
        
        
        for cell in self.cell_list:
            if cell.type in counts:
                counts[cell.type] += 1
                
                
                
        # arguments are (name of the data series, x, y)
        self.plot_win.add_data_point("MESENCHYME", mcs, counts[self.MESEN])
        self.plot_win.add_data_point("HYBRID", mcs, counts[self.HYB])
        self.plot_win.add_data_point("EPITHELIAL", mcs, counts[self.EPI])
        
        if mcs % 50 == 0:
            self.plot_win.save_plot_as_png(
                f"D:/compucell/CompuCell3D-py3-64bit/Output_logs/plots/PDL1_{mcs}.png"
            )
        # self.plot_win.add_data_point("MSur", mcs, cell.surface)        
        
                    
        # for cell in self.cell_list:
            # print("CELL ID=",cell.id, " CELL TYPE=",cell.type," volume=",cell.volume)

    def finish(self):
        '''
        this function may be called at the end of simulation - used very infrequently though
        '''        
        # PLACE YOUR CODE BELOW THIS LINE
        
        return

    def on_stop(self):
        '''
        this gets called each time user stops simulation
        '''        
        # PLACE YOUR CODE BELOW THIS LINE
        
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# ANTI_PDL1_DRUG_DOSAGE = 50   

        
# class therapy_Steppable(SteppableBasePy):
    # def __init__(self, frequency=1):
        # '''
        # constructor
        # '''
        # SteppableBasePy.__init__(self, frequency)
        # # PLACE YOUR CODE BELOW THIS LINE
        

    # def start(self):
        # '''
        # called once before first MCS
        # '''
        # # PLACE YOUR CODE BELOW THIS LINE
        # for cell in self.cell_list:
            
            # cell.dict['anti_pdl1_bound'] = False
            # cell.dict['marked_for_death'] = False
            
        # self.PDL1_expression_therapy_log = open("D:/compucell/CompuCell3D-py3-64bit/Output_logs/PDL1_expression_therapy_log.csv", "w")     
        
        # self.PDL1_expression_therapy_log.write("MCS,CellID,Cell_Type,PDL1_level_after_therapy\n")    
        
        
        
   
        
        # anti_pdl1 = self.field.AntiPDL1
        
        # for x in range(self.dim.x):
            # for y in range(self.dim.y):
                
                # anti_pdl1[x,y,0] = ANTI_PDL1_DRUG_DOSAGE
                
                
    # def anti_pdl1_therapy(self, mcs):

        # anti_pdl1_on = self.shared_steppable_vars.get("ANTI_PDL1_ON", False)
        # for cell in self.cell_list:
            # cell.dict['marked_for_death'] = False
        
        # print(
        # f"MCS={mcs} | anti_pdl1_on={anti_pdl1_on}"
        # )

        # # cells_to_delete = []
        # cells_to_delete = set()

        # for cell in self.cell_list_by_type(self.TCELL):

            # for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):

                # if not neighbor:
                    # continue

                # # Mesen

                # if neighbor.type == self.MESEN:

                    # pdl1_level = neighbor.dict.get('PDL1_level', 0.0)

                    # effective_pdl1 = pdl1_level

                    # if anti_pdl1_on:
                        # effective_pdl1 *= 0.2
                        
                        # print("effectivepdl1 :", effective_pdl1)

                    # if effective_pdl1 >= PDL1_SUPPRESSION_THRESHOLD_MESEN:
                        
                        # pass

                    # else:

                        # # cells_to_delete.append(neighbor)
                        # # cells_to_delete.add(neighbor)
                        # if neighbor.dict['marked_for_death']:
                            # continue

                        # neighbor.dict['marked_for_death'] = True
                        # cells_to_delete.add(neighbor)
                    
                        # self.PDL1_expression_therapy_log.write(
                        # f"{mcs},{neighbor.id},MESEN,{effective_pdl1:.2f}\n"
                    # )

                        # if mcs % 50 == 0:
                            # print(f"MCS={mcs} , " f"TCell {cell.id} ", f"KILLING MESEN {neighbor.id}")
                            
                        
                # #Hybrid

                # elif neighbor.type == self.HYB:

                    # pdl1_level = neighbor.dict.get('PDL1_level',0.0)

                    # effective_pdl1 = pdl1_level

                    # if anti_pdl1_on:
                        # effective_pdl1 *= 0.2
                        
                        # print("effectivepdl1 :", effective_pdl1)

                    # if effective_pdl1 >= PDL1_SUPPRESSION_THRESHOLD_HYB:

                        # pass

                    # else:

                        # # cells_to_delete.append(neighbor)
                        # if neighbor.dict['marked_for_death']:
                            # continue

                        # neighbor.dict['marked_for_death'] = True

                        # cells_to_delete.add(neighbor)
                        
                        # self.PDL1_expression_therapy_log.write(
                        # f"{mcs},{neighbor.id},HYB,{effective_pdl1:.2f}\n"
                    # )

                        # if mcs % 50 == 0:
                            # print(f"MCS={mcs} , " f"TCell {cell.id} " f"KILLING HYB {neighbor.id}")
                            
                            
                # # Epi

                # elif neighbor.type == self.EPI:

                    # pdl1_level = neighbor.dict.get(
                        # 'PDL1_level',
                        # 0.0
                    # )

                    # effective_pdl1 = pdl1_level

                    # if anti_pdl1_on:
                        # effective_pdl1 *= 0.2

                    # if effective_pdl1 >= PDL1_SUPPRESSION_THRESHOLD_EPI:

                        # pass

                    # else:

                        # # cells_to_delete.append(neighbor)
                        # if neighbor.dict['marked_for_death']:
                            # continue

                        # neighbor.dict['marked_for_death'] = True

                        # cells_to_delete.add(neighbor)
                        
                        # self.PDL1_expression_therapy_log.write(
                        # f"{mcs},{neighbor.id},HYB,{effective_pdl1:.2f}\n"
                    # )

                        # if mcs % 50 == 0:
                            # print(f"MCS={mcs} , " f"TCell {cell.id} " f"KILLING EPI {neighbor.id}")
                            
                            
                        
                        
                        
        # # for cell in cells_to_delete:
            # # self.delete_cell(cell)
                   
                   
        # for dead_cell in cells_to_delete:
            # self.delete_cell(dead_cell)
            
        # if mcs % 50 == 0:
            # self.PDL1_expression_therapy_log.flush()        
                        
                
                

    # def step(self, mcs):
        
        # if mcs >= 450:
            
            # self.shared_steppable_vars["ANTI_PDL1_ON"] = True
            # self.anti_pdl1_therapy(mcs)
        
        
                
                
        
        # '''
        # called every MCS or every "frequency" MCS (depending how it was instantiated in the main Python file)
        # '''
        # # PLACE YOUR CODE BELOW THIS LINE
                
        # # for cell in self.cell_list:
            # # print("CELL ID=",cell.id, " CELL TYPE=",cell.type," volume=",cell.volume)

    # def finish(self):
        # '''
        # this function may be called at the end of simulation - used very infrequently though
        # '''        
        # # PLACE YOUR CODE BELOW THIS LINE
        
        # return

    # def on_stop(self):
        # '''
        # this gets called each time user stops simulation
        # '''        
        # # PLACE YOUR CODE BELOW THIS LINE
        
        # return
