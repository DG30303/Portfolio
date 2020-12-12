'''Missionaries3_VIS_FOR_TK3.py
Version of Sept. 17, 2019.
This visualization file works with Missionaries3.py and
Tk_SOLUZION_Client3.py.
It uses three jpg images for showing missionaries, cannibals, and the boat.

'''
from tkinter import font
import threading
import time

myFont=None

WIDTH = 500
HEIGHT = 600

TITLE = 'Chronic Disease Crisis'

STATE_WINDOW = None
STATE_ARRAY = None

def initialize_vis(st_win, state_arr, initial_state):
  global STATE_WINDOW, STATE_ARRAY
  STATE_WINDOW = st_win
  STATE_ARRAY = state_arr
  STATE_WINDOW.winfo_toplevel().title(TITLE)
  render_state(initial_state)
  
def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
    #print("In render_state, state is "+str(s))
    # Create the default array of colors
    lightRed = (255, 204, 203)
    lightGreen = (144, 238, 144)
    tan = (243,243,243)
    white = (255, 255, 255)
    gray = (128, 128, 128)
    blue = (15, 121, 242)
    green = (0, 204, 0)
    black = (0, 0, 0)
    red = (255,0,0)
    yellow = (255,255,0)
    orange = (255,165,0)
    blue2 = (0,0,255)
    green2 = (0,255,0)
    red2 = (255, 65, 65)
    yellow2 = (247, 227, 38)
    pink = (221, 160, 221)

    if(s.inARoom == False and s.reportScreen == False and s.startGame == True and s.finalScreen == False):
        row = [white]*1
        the_color_array = [row, row[:], row[:], row[:]]
        the_color_array[0][0]="lab.jpg"
        the_color_array[1][0]="waiting.jpg"
        the_color_array[2][0]="emergency.jpg"
        the_color_array[3][0]="center.jpg"
        # Now create the default array of string labels.
        row = ['' for i in range(1)]
        the_string_array = [row, row[:], row[:], row[:]]
    elif(s.startGame == False and s.tutorial == False):
        row = [white]*1
        the_color_array = [row[:]]
        the_color_array[0][0]= "hospital.jpg"
        row = ['' for i in range(1)]
        the_string_array = [row[:]]
    elif(s.startGame == False and s.tutorial == True):
        row = [white]*1
        the_color_array = [row[:]]
        the_color_array[0][0]= "tutorial.jpg"
        row = ['' for i in range(1)]
        the_string_array = [row[:]]
    elif(s.inWaitingRoom == True and s.inMiniGame == False and s.startGame == True and s.finalScreen == False):
        row = [tan]*3
        the_color_array = [row, row[:]]
        row1 = ['' for i in range(3)]
        the_string_array = [row1, row1[:]]
        for i in range(len(s.waitingRoom)):
            imageName = s.waitingRoom[i].image
            the_color_array[0][i]= imageName
            the_color_array[1][i] = "bkg.jpg"
        for i in range(len(s.waitingRoom)):
            the_string_array[0][i] = ""
            the_string_array[1][i] = "Patient " + str(i + 1) + "\n\n" + s.waitingRoom[i].__str__()
            if s.medicine[s.waitingRoom[i].disease] < s.waitingRoom[i].resources[0] or s.staff < s.waitingRoom[i].resources[1]:
                the_string_array[1][i] += "\nYou do not\nhave the proper\nresources to treat\nthis patient."
            else:
                the_string_array[1][i] += "\nYou can treat\nthis patient."
        myFont = font.Font(family="Helvetica", size=9, weight="bold")
        # Now create the default array of string labels.'''
    elif(s.inEmergencyRoom == True and s.inMiniGame == False and s.startGame == True and s.finalScreen == False):
        row = [tan]*3
        the_color_array = [row, row[:]]
        row1 = ['' for i in range(3)]
        the_string_array = [row1, row1[:]]
        for i in range(len(s.emergencyRoom)):
            imageName = s.emergencyRoom[i].image
            the_color_array[0][i]= imageName
            the_color_array[1][i] = "bkg.jpg"
        for i in range(len(s.emergencyRoom)):
            the_string_array[0][i] = ""
            the_string_array[1][i] = "Patient " + str(i + 1) + "\n\n" + s.emergencyRoom[i].__str__()
            if s.medicine[s.emergencyRoom[i].disease] < s.emergencyRoom[i].resources[0] or s.staff < s.emergencyRoom[i].resources[1]:
                the_string_array[1][i] += "\nYou do not\nhave the proper\nresources to treat\nthis patient."
            else:
                the_string_array[1][i] += "\nYou can treat\nthis patient."
        myFont = font.Font(family="Helvetica", size=9, weight="bold")
    elif(s.displayHeartDiseaseInfo == True and s.inVisitorCenter == True and s.startGame == True and s.finalScreen == False):
        row = [white]
        the_color_array = [row]
        the_color_array[0][0] = "heartInfo.jpg"
        row1 = [""]
        the_string_array = [row1]
    elif(s.displayAlzheimersInfo == True and s.inVisitorCenter == True and s.startGame == True and s.finalScreen == False):
        row = [white]
        the_color_array = [row]
        the_color_array[0][0] = "alzheimersInfo.jpg"
        row1 = [""]
        the_string_array = [row1]
    elif(s.displayLungDiseaseInfo == True and s.inVisitorCenter == True and s.startGame == True and s.finalScreen == False):
        row = [white]
        the_color_array = [row]
        the_color_array[0][0] = "lungInfo.jpg"
        row1 = [""]
        the_string_array = [row1]
    elif(s.displayCancerInfo == True and s.inVisitorCenter == True and s.startGame == True and s.finalScreen == False):
        row = [white]
        the_color_array = [row]
        the_color_array[0][0] = "cancerInfo.jpg"
        row1 = [""]
        the_string_array = [row1]
    elif(s.displayStrokeInfo == True and s.inVisitorCenter == True and s.startGame == True and s.finalScreen == False):
        row = [white]
        the_color_array = [row]
        the_color_array[0][0] = "strokeInfo.jpg"
        row1 = [""]
        the_string_array = [row1]
    elif(s.inVisitorCenter == True and s.displayHeartDiseaseInfo == False and s.displayAlzheimersInfo == False and s.displayLungDiseaseInfo == False and s.displayCancerInfo == False and s.displayStrokeInfo == False):
        row = [white]
        the_color_array = [row]
        the_color_array[0][0] = "tutorial.jpg"
        row1 = [""]
        the_string_array = [row1]
    elif(s.inMiniGame == True and s.inCatchMiniGame == True and s.startGame == True and s.finalScreen == False):
        row = [white]*len(s.catch.board)
        the_color_array = []
        for i in range(len(s.catch.board)):
            the_color_array += [row[:]]
        # Now create the default array of string labels.
        row = ['' for i in range(len(s.catch.board))]
        the_string_array = []
        for i in range(len(s.catch.board)):
            the_string_array += [row[:]]
        myFont = font.Font(family="Helvetica", size=26, weight="bold")
        # Adjust colors and strings to match the state.
        for row in range(len(s.catch.board)):
            for col in range(len(s.catch.board)):
                if s.catch.board[row][col] == " ":
                    the_color_array[row][col] = white
                    the_string_array[row][col] = s.catch.board[row][col]
                elif s.catch.board[row][col] == "X":
                    the_color_array[row][col] = "redblood.png"
                    the_string_array[row][col] = ""
                elif s.catch.board[row][col] == "O":
                    the_color_array[row][col] = "whiteblood.jpg"
                    the_string_array[row][col] = ""
    elif(s.inMiniGame == True and s.inMazeMiniGame == True and s.startGame == True and s.finalScreen == False):
        print("In render_state, state is "+str(s))
        the_string_array = []
        if s.maze.condition == "Critical":
            the_color_array = flashlight_mode(s, red, gray, blue, green, black)
        else:
            the_color_array = regular_mode(s, red, gray, blue, green, black)
        the_color_array[9][9] = green #Change this to lung.jpg
        caption="Current state of the puzzle. Textual version: "+str(s)
    elif(s.inMiniGame == True and s.inMemoryMiniGame == True and s.startGame == True and s.finalScreen == False):
        default = ".jpg"
        if not myFont:
            myFont = font.Font(family="Helvetica", size=26, weight="bold")
        print("In render_state, state is "+str(s))
    
        caption="Welcome to the memory game! Remember each image and press next to progress. Then pick the right order!"
        row = [white]*1
        the_color_array = [row[:]]
        image = s.memory.list_of_orders[s.memory.current_order][s.memory.current_image]
        the_color_array[0][0] = image
        row = ['' for i in range(1)]
        the_string_array = [row[:]]
        if s.memory.win == True:
            the_string_array[0][0] = "You got it right!"
        if s.memory.attempts == 1 and s.memory.win == False:
            the_string_array[0][0] = "You got it wrong!"
    elif(s.inMiniGame == True and s.inBattleMiniGame == True and s.startGame == True and s.finalScreen == False):
        the_color_array = [[green],[white],[white],[white],[green2],[blue2]]
        the_string_array = [["Health: "],[""],[""],[""],["Health: "],[""]]
        the_string_array[0][0] += str(s.battle.badCellHealth)
        the_string_array[4][0] += str(s.battle.goodCellHealth)
        r1 = 0
        g1 = 255
        if s.battle.badCellHealth < 50:
            r1 = 255
            for i in range(50 - s.battle.badCellHealth):
                g1 -= 5.1
        else:
            for i in range(100 - s.battle.badCellHealth):
                r1 += 5.1
        healthBarColor1 = (int(r1),int(g1),0)
        the_color_array[0] = [healthBarColor1]
        r2 = 0
        g2 = 255
        if s.battle.goodCellHealth < 50:
            r2 = 255
            for i in range(50 - s.battle.goodCellHealth):
                g2 -= 5.1
        else:
            for i in range(100 - s.battle.goodCellHealth):
                r2 += 5.1
        healthBarColor2 = (int(r2),int(g2),0)
        the_color_array[4] = [healthBarColor2]
        the_color_array[1][0] = "cancerousCell.jpg"
        the_color_array[2][0] = "actionLines.jpg"
        the_color_array[3][0] = "whiteBloodCellBattle.jpg"
        the_color_array[5][0] = "moves.jpg"
    elif(s.inMiniGame == True and s.inLuckMiniGame == True and s.startGame == True and s.finalScreen == False):
        row = [white] + [white] + [white]
        the_color_array = [row]
        row1 = ["","",""]
        the_string_array = [row1]
        the_color_array[0][0] = "heart1.jpg"
        the_color_array[0][1] = "heart2.jpg"
        the_color_array[0][2] = "heart3.jpg"
        if s.luck.player_guess == True:
            the_string_array[0][s.luck.correctCup] = "You got it!"
        if s.luck.player_guess == False and s.luck.turn_counter > 0:
            the_string_array[0][s.luck.previousGuess] = "This is not it!"
    elif(s.inLabResources == True and s.inMiniGame == False and s.reportScreen == False and s.startGame == True and s.finalScreen == False):
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
        addOn = 2
        row = [white]*2
        the_color_array = [row[:]]
        row = ['' for i in range(2)]
        the_string_array = [row[:]]
        
        the_string_array[0][0] = "Disease"
        the_string_array[0][1] = "Medicine Amount"
        
        row = [white]*2
        the_color_array += [row[:], row[:]]
        row = ['' for i in range(2)]
        the_string_array += [row[:], row[:]]
        
        the_string_array[1][0] = "Heart Disease"
        the_string_array[1][1] = str(s.medicine["Heart Disease"])
        
        the_string_array[2][0] = "Alzheimer's"
        the_string_array[2][1] = str(s.medicine["Alzheimer's"])
        
        if s.cancer == True:
            addOn += 1
            row = [white]*2
            the_color_array += [row[:]]
            row = ['' for i in range(2)]
            the_string_array += [row[:]]
            the_string_array[addOn][0] = "Cancer"
            the_string_array[addOn][1] = str(s.medicine["Cancer"])
            
        if s.stroke == True:
            addOn += 1
            row = [white]*2
            the_color_array += [row[:]]
            row = ['' for i in range(2)]
            the_string_array += [row[:]]
            the_string_array[addOn][0] = "Stroke"
            the_string_array[addOn][1] = str(s.medicine["Stroke"])
            
        if s.lungDisease == True:
            addOn += 1
            row = [white]*2
            the_color_array += [row[:]]
            row = ['' for i in range(2)]
            the_string_array += [row[:]]
            the_string_array[addOn][0] = "Lung Disease"
            the_string_array[addOn][1] = str(s.medicine["Lung Disease"])
        
        row = [white]*2
        the_color_array += [row[:], row[:], row[:], row[:], row[:], row[:]]
        row = ['' for i in range(2)]
        the_string_array += [row[:], row[:], row[:], row[:], row[:], row[:]]
        
        space = [tan]*2
        the_color_array[addOn + 1] = space[:]
        space = [""]*2
        the_string_array[addOn + 1] = space[:]
        the_string_array[addOn + 2][0] = "Total Staff: " + str(s.staff)
        the_string_array[addOn + 3][0] = "Total Net Profit: $" + str(s.profit)
        
        if s.cancer == True:
            the_string_array[addOn + 4][0] = "Invested in Cancer"
            the_string_array[addOn + 4][1] = "True"
            bkg = [lightGreen]*2
            the_color_array[addOn + 4] = bkg[:]
        else:
            the_string_array[addOn + 4][0] = "Invested in Cancer"
            the_string_array[addOn + 4][1] = "False"
            bkg = [lightRed]*2
            the_color_array[addOn + 4] = bkg[:]
        
        if s.stroke == True:
            the_string_array[addOn + 5][0] = "Invested in Stroke"
            the_string_array[addOn + 5][1] = "True"
            bkg = [lightGreen]*2
            the_color_array[addOn + 5] = bkg[:]
        else:
            the_string_array[addOn + 5][0] = "Invested in Stroke"
            the_string_array[addOn + 5][1] = "False"
            bkg = [lightRed]*2
            the_color_array[addOn + 5] = bkg[:]
            
        if s.lungDisease == True:
            the_string_array[addOn + 6][0] = "Invested in\nLung Disease"
            the_string_array[addOn + 6][1] = "True"
            bkg = [lightGreen]*2
            the_color_array[addOn + 6] = bkg[:]
        else:
            the_string_array[addOn + 6][0] = "Invested in\nLung Disease"
            the_string_array[addOn + 6][1] = "False"
            bkg = [lightRed]*2
            the_color_array[addOn + 6] = bkg[:]
    elif(s.reportScreen == True and s.startGame == True and s.finalScreen == False):
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
        row = [tan]*3
        the_color_array = [row[:], row[:], row[:], row[:], row[:], row[:], row[:]]
        row = ['' for i in range(3)]
        the_string_array = [row[:], row[:], row[:], row[:], row[:], row[:], row[:]]
        the_string_array[0][0] = "Disease"
        the_string_array[0][1] = "Patients\nTreated"
        the_string_array[0][2] = "Patients\nKilled"
        the_string_array[1][0] = "Heart Disease"
        the_string_array[2][0] = "Lung Disease"
        the_string_array[3][0] = "Alzheimer's"
        the_string_array[4][0] = "Stroke"
        the_string_array[5][0] = "Cancer"
        the_string_array[1][1] = s.heartDiseasePatientsTreated
        the_string_array[2][1] = s.lungDiseasePatientsTreated
        the_string_array[3][1] = s.alzheimersPatientsTreated
        the_string_array[4][1] = s.strokePatientsTreated
        the_string_array[5][1] = s.cancerPatientsTreated
        the_string_array[1][2] = s.heartDiseasePatientsKilled
        the_string_array[2][2] = s.lungDiseasePatientsKilled
        the_string_array[3][2] = s.alzheimersPatientsKilled
        the_string_array[4][2] = s.strokePatientsKilled
        the_string_array[5][2] = s.cancerPatientsKilled
        the_string_array[6][0] = "Profit Earned\nin Round " + str(s.turn - 1)
        the_string_array[6][1] = "$" + str(s.turnProfit)
    elif(s.finalScreen == True):
        myFont = font.Font(family="Helvetica", size=10, weight="bold")
        row = [white] + [white]
        the_color_array = [row[:], row[:] , row[:], row[:], row[:], row[:], row[:], row[:], row[:]]
        row1 = [""] + [""]
        the_string_array = [row1[:], row1[:], row1[:], row1[:], row1[:], row1[:], row1[:], row1[:], row1[:]]
        r1 = 255
        g1 = 0
        if s.alzheimersPercent < 50:
            g1 = 255
            for i in range(50 - s.alzheimersPercent):
                r1 -= 5.1
        else:
            for i in range(100 - s.alzheimersPercent):
                g1 += 5.1
        statBarColor1 = (int(r1),int(g1),0)
        bkg = [statBarColor1]*2
        the_color_array[4] = bkg[:]
        g2 = 0
        r2 = 255
        if s.heartDiseasePercent < 50:
            g2 = 255
            for i in range(50 - s.heartDiseasePercent):
                r2 -= 5.1
        else:
            for i in range(100 - s.heartDiseasePercent):
                g2 += 5.1
        statBarColor2 = (int(r2),int(g2),0)
        bkg = [statBarColor2]*2
        the_color_array[5] = bkg[:]
        g3 = 0
        r3 = 255
        if s.lungDiseasePercent < 50:
            g3 = 255
            for i in range(50 - s.lungDiseasePercent):
                r3 -= 5.1
        else:
            for i in range(100 - s.lungDiseasePercent):
                g3 += 5.1
        statBarColor3 = (int(r3),int(g3),0)
        bkg = [statBarColor3]*2
        the_color_array[6] = bkg[:]
        g4 = 0
        r4 = 255
        if s.cancerPercent < 50:
            g4 = 255
            for i in range(50 - s.cancerPercent):
                r4 -= 5.1
        else:
            for i in range(100 - s.cancerPercent):
                g4 += 5.1
        statBarColor4 = (int(r4),int(g4),0)
        bkg = [statBarColor4]*2
        the_color_array[7] = bkg[:]
        g5 = 0
        r5 = 255
        if s.strokePercent < 50:
            g5 = 255
            for i in range(50 - s.strokePercent):
                r5 -= 5.1
        else:
            for i in range(100 - s.strokePercent):
                g5 += 5.1
        statBarColor5 = (int(r5),int(g5),0)
        bkg = [statBarColor5]*2
        the_color_array[8] = bkg[:]
        the_string_array[1][0] = "Patients Treated"
        the_string_array[1][1] = str(s.patientsTreated)
        the_string_array[2][0] = "Patients Killed"
        the_string_array[2][1] = str(s.totalPatients - s.patientsTreated)
        the_string_array[3][0] = "Patients Not Seen"
        the_string_array[3][1] = str(22 - s.totalPatients)
        the_string_array[4][0] = "World Alzheimer's Prevalence"
        the_string_array[4][1] = str(s.alzheimersPercent) + "%"
        the_string_array[5][0] = "World Heart Disease Prevalence"
        the_string_array[5][1] = str(s.heartDiseasePercent) + "%"
        the_string_array[6][0] = "World Lung Disease Prevalence"
        the_string_array[6][1] = str(s.lungDiseasePercent) + "%"
        the_string_array[7][0] = "World Cancer Prevalence"
        the_string_array[7][1] = str(s.cancerPercent) + "%"
        the_string_array[8][0] = "World Stroke Prevalence"
        the_string_array[8][1] = str(s.strokePercent) + "%"
        the_color_array[0][0] = "game.jpg"
        the_color_array[0][1] = "results.jpg"
        
    caption="-INSTRUCTIONS-"+str(s)
    print(caption)
    the_state_array = STATE_ARRAY(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  text_color = "black",
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
    
def flashlight_mode(s, red, gray, blue, green, black):
    white = (255, 255, 255)
    the_color_array = [[black for i in range(10)] for j in range(10)]
    for r in range(len(s.maze.current_maze)):
      for c in range(len(s.maze.current_maze)):
        try:
          if r <= (s.maze.cr + 2) and r >= (s.maze.cr - 2) and c <= (s.maze.cl + 2) and c >= (s.maze.cl - 2):
            if s.maze.current_maze[r][c] == 0:
              the_color_array[r][c] = white
            elif s.maze.current_maze[r][c] == 1:  
              the_color_array[r][c] = gray
            elif s.maze.current_maze[r][c] == "X":
              the_color_array[r][c] = blue #Change this to circle.jpg
        except:
          pass
    return the_color_array

def regular_mode(s, red, gray, blue, green, black):
    white = (255, 255, 255)
    the_color_array = [[white for i in range(10)] for j in range(10)] 
    for r in range(len(s.maze.current_maze)):
      for c in range(len(s.maze.current_maze)):
        if s.maze.current_maze[r][c] == 1:
          the_color_array[r][c] = gray
        elif s.maze.current_maze[r][c] == "X":
          the_color_array[r][c] = blue #Change this to circle.jpg
    return the_color_array



print("The Health VIS file has been imported.")
    

    
