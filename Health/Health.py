'''Health.py
("Chronic Diseases" problem)
'''
#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "Chronic Disease Crisis"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['D. Garzon', 'E. Martin','A. Nag', 'S. Mehrvarzan']
PROBLEM_CREATION_DATE = "18-SEP-2020"
PROBLEM_DESC=\
'''
Welcome to the Global Hospital! 
The purpose is to treat and research chronics diseases that are facing our world today. 
By tackling different minigames and seeing how diseases affect our world today the user will go through 
different tasks to treat patients at a global hospital. 
Each turn the user will receive a new round of patients 
and will try their best to treat them all with the resources that they havea avaiable.
'''

#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
#User has 3 options:
#Waiting Room
#Emergency Room
#Lab

class State:
  def __init__(self, old=None, battle = None, catch = None, maze = None, luck = None, memory = None):
    # Default new state is a state objects initialized as the
    # initial state.
    # If called with old equal to a non-empty state, then
    # the new instance is made to be a copy of that state.
    self.displayHeartDiseaseInfo = False
    self.displayAlzheimersInfo = False
    self.displayLungDiseaseInfo = False
    self.displayCancerInfo = False
    self.displayStrokeInfo = False
    self.inVisitorCenter = False
    self.tutorial = False
    self.cancer = False
    self.stroke = False
    self.totalPatients = 0
    self.startGame = False
    self.battle = None
    self.catch = None
    self.maze = None
    self.luck = None
    self.memory = None
    self.inWaitingRoom = False
    self.inEmergencyRoom = False
    self.inLabResources = False
    self.inLabPurchases = False
    self.reportScreen = False
    self.endTurn = False
    self.nextScreen = False
    self.turn = 1
    self.waitingRoom = []
    self.emergencyRoom = []
    self.getPatients(self.turn)
    self.medicineCost = {"Heart Disease" : 300, "Alzheimer's" : 400, "Lung Disease" : 200, "Stroke" : 200, "Cancer" : 400}
    self.lungDisease = False
    self.inMiniGame = False
    self.inCatchMiniGame = False
    self.inMazeMiniGame = False
    self.inMemoryMiniGame = False
    self.inLuckMiniGame = False
    self.inBattleMiniGame = False
    self.inARoom = False
    self.catch = None
    self.finalScreen = False
    self.patientsTreated = 0
    self.cancerPercent = 100
    self.heartDiseasePercent = 100
    self.lungDiseasePercent = 100
    self.alzheimersPercent = 100
    self.strokePercent = 100
    self.staff = 5
    self.medicine = {"Heart Disease" : 2, "Alzheimer's" : 1, "Lung Disease" : 0, "Stroke" : 0, "Cancer" : 0}
    self.profit = 100
    self.turnProfit = 0
    self.heartDiseasePatientsTreated = 0
    self.lungDiseasePatientsTreated = 0
    self.alzheimersPatientsTreated = 0
    self.strokePatientsTreated = 0
    self.cancerPatientsTreated = 0
    self.heartDiseasePatientsKilled = 0
    self.lungDiseasePatientsKilled = 0
    self.alzheimersPatientsKilled = 0
    self.strokePatientsKilled = 0
    self.cancerPatientsKilled = 0
    if not memory is None:
      self.memory = memory
    if not battle is None:
      self.battle = battle
    if not catch is None:
      self.catch = catch
    if not maze is None:
      self.maze = maze
    if not luck is None:
      self.luck = luck
    if not old is None:
      self.displayHeartDiseaseInfo = old.displayHeartDiseaseInfo
      self.displayAlzheimersInfo = old.displayAlzheimersInfo
      self.displayLungDiseaseInfo = old.displayLungDiseaseInfo
      self.displayCancerInfo = old.displayCancerInfo
      self.displayStrokeInfo = old.displayStrokeInfo
      self.inVisitorCenter = old.inVisitorCenter
      self.tutorial = old.tutorial
      self.medicineCost = old.medicineCost
      self.turnProfit = old.turnProfit
      self.heartDiseasePatientsTreated = old.heartDiseasePatientsTreated
      self.lungDiseasePatientsTreated = old.lungDiseasePatientsTreated
      self.alzheimersPatientsTreated = old.alzheimersPatientsTreated
      self.strokePatientsTreated = old.strokePatientsTreated 
      self.cancerPatientsTreated = old.cancerPatientsTreated 
      self.heartDiseasePatientsKilled = old.heartDiseasePatientsKilled
      self.lungDiseasePatientsKilled = old.lungDiseasePatientsKilled
      self.alzheimersPatientsKilled = old.alzheimersPatientsKilled
      self.strokePatientsKilled = old.strokePatientsKilled
      self.cancerPatientsKilled = old.cancerPatientsKilled
      self.finalScreen = old.finalScreen
      self.patientsTreated = old.patientsTreated
      self.totalPatients = old.totalPatients
      self.cancerPercent = old.cancerPercent
      self.heartDiseasePercent = old.heartDiseasePercent
      self.lungDiseasePercent = old.lungDiseasePercent
      self.alzheimersPercent = old.alzheimersPercent
      self.strokePercent = old.strokePercent
      self.startGame = old.startGame
      self.nextScreen = old.nextScreen
      self.endTurn = old.endTurn
      self.reportScreen = old.reportScreen
      self.turn = old.turn
      self.inWaitingRoom = old.inWaitingRoom
      self.inEmergencyRoom = old.inEmergencyRoom
      self.inLabResources = old.inLabResources
      self.inLabPurchases = old.inLabPurchases
      self.waitingRoom = old.waitingRoom[:]
      self.emergencyRoom = old.emergencyRoom[:]
      self.inMiniGame = old.inMiniGame
      self.inCatchMiniGame = old.inCatchMiniGame
      self.inMazeMiniGame = old.inMazeMiniGame
      self.inMemoryMiniGame = old.inMemoryMiniGame
      self.inLuckMiniGame = old.inLuckMiniGame
      self.inBattleMiniGame = old.inBattleMiniGame
      self.inARoom = old.inARoom
      self.staff = old.staff
      self.medicine = old.medicine
      self.profit = old.profit
      self.cancer = old.cancer
      self.lungDisease = old.lungDisease
      self.stroke = old.stroke
      
      description = self.describe_state()
      print(description)

  def can_move(self,action, act = None, num = None):
    if self.inMiniGame == False:
      if action == "startGame" and self.startGame == False and self.tutorial == False:
        return True
      elif action == "generalTutorial" and self.startGame == False and self.tutorial == False:
        return True
      elif action == "exitGeneralTutorial" and self.tutorial == True and self.startGame == False:
        return True
      elif action == "goIntoLabResources" and self.inARoom == False and self.startGame == True and self.reportScreen == False and self.finalScreen == False:
        return True
      elif action == "goIntoWaitingRoom" and self.inARoom == False and self.startGame == True and self.reportScreen == False and self.finalScreen == False:
        return True
      elif action == "goIntoEmergencyRoom" and self.inARoom == False and self.startGame == True and self.reportScreen == False and self.finalScreen == False:
        return True
      elif action == "nextTurn" and self.reportScreen == True:
          return True
      elif action == "reportScreen" and self.endTurn == True and self.reportScreen == False:
          return True
      elif action == "buyStaff" and self.inLabResources == True and self.profit > 10 and self.reportScreen == False:
          return True
      elif action == "strokeMedicine" and self.inLabResources == True and self.profit > 200 and self.reportScreen == False and self.stroke == True:
          return True
      elif action == "cancerMedicine" and self.inLabResources == True and self.profit > 400 and self.reportScreen == False and self.cancer == True:
          return True
      elif action == "alzhimerMedicine" and self.inLabResources == True and self.profit > 400 and self.reportScreen == False:
          return True
      elif action == "heartMedicine" and self.inLabResources == True and self.profit > 300 and self.reportScreen == False:
          return True
      elif action == "lungMedicine" and self.inLabResources == True and self.profit > 200 and self.reportScreen == False and self.lungDisease == True:
          return True
      elif action == "investStroke" and self.inLabResources == True and self.profit > 600 and self.reportScreen == False and self.turn >= 4 and self.stroke == False:
          return True
      elif action == "investLung" and self.inLabResources == True and self.profit > 600 and self.reportScreen == False and self.turn >= 2 and self.lungDisease == False:
          return True
      elif action == "investCancer" and self.inLabResources == True and self.profit > 600 and self.reportScreen == False and self.turn >= 3 and self.cancer == False:
          return True
      elif action == "exitLab" and self.inLabResources == True and self.endTurn == False and self.finalScreen == False:
          return True
      elif action == "exitWait" and self.inWaitingRoom == True:
          return True
      elif action == "exitEmergency" and self.inEmergencyRoom == True:
          return True
      elif action == "selectPatient1WaitingRoom":
        if self.inWaitingRoom == True:
            try:
              if not self.waitingRoom[0] is None and self.waitingRoom[0].resources[0] <= self.medicine[self.waitingRoom[0].disease] and self.waitingRoom[0].resources[1] <= self.staff:
                return True
              else:
                return False
            except:
                return False
        else:
          return False
      elif action == "selectPatient2WaitingRoom":
        if self.inWaitingRoom == True:
            try:
              if not self.waitingRoom[1] is None and self.waitingRoom[1].resources[0] <= self.medicine[self.waitingRoom[1].disease] and self.waitingRoom[1].resources[1] <= self.staff:
                return True
              else:
                return False
            except:
                return False
        else:
          return False
      elif action == "selectPatient3WaitingRoom":
        if self.inWaitingRoom == True:
            try:
              if not self.waitingRoom[2] is None and self.waitingRoom[2].resources[0] <= self.medicine[self.waitingRoom[2].disease] and self.waitingRoom[2].resources[1] <= self.staff:
                return True
              else:
                return False
            except:
                return False
        else:
          return False
      elif action == "selectPatient1EmergencyRoom":
        if self.inEmergencyRoom == True:
            try:
              if not self.emergencyRoom[0] is None and self.emergencyRoom[0].resources[0] <= self.medicine[self.emergencyRoom[0].disease] and self.emergencyRoom[0].resources[1] <= self.staff:
                return True
              else:
                return False
            except:
                return False
        else:
          return False
      elif action == "selectPatient2EmergencyRoom":
        if self.inEmergencyRoom == True:
            try:
              if not self.emergencyRoom[1] is None and self.emergencyRoom[1].resources[0] <= self.medicine[self.emergencyRoom[1].disease] and self.emergencyRoom[1].resources[1] <= self.staff:
                return True
              else:
                return False
            except:
                return False
        else:
          return False
      elif action == "selectPatient3EmergencyRoom":
        if self.inEmergencyRoom == True:
            try:
              if not self.emergencyRoom[2] is None and self.emergencyRoom[2].resources[0] <= self.medicine[self.emergencyRoom[2].disease] and self.emergencyRoom[2].resources[1] <= self.staff:
                return True
              else:
                return False
            except:
                return False
        else:
          return False
    if action == "catchMiniGame" and self.inMazeMiniGame == False and self.inMemoryMiniGame == False \
       and self.inLuckMiniGame == False and self.inBattleMiniGame == False and self.inCatchMiniGame == False and self.inMiniGame == True:
      return True
    elif action == "mazeMiniGame" and self.inMazeMiniGame == False and self.inMemoryMiniGame == False \
       and self.inLuckMiniGame == False and self.inBattleMiniGame == False and self.inCatchMiniGame == False and self.inMiniGame == True:
      return True
    elif action == "memoryMiniGame" and self.inMazeMiniGame == False and self.inMemoryMiniGame == False \
       and self.inLuckMiniGame == False and self.inBattleMiniGame == False and self.inCatchMiniGame == False and self.inMiniGame == True:
      return True
    elif action == "luckMiniGame" and self.inMazeMiniGame == False and self.inMemoryMiniGame == False \
       and self.inLuckMiniGame == False and self.inBattleMiniGame == False and self.inCatchMiniGame == False and self.inMiniGame == True:
      return True
    elif action == "battleMiniGame" and self.inMazeMiniGame == False and self.inMemoryMiniGame == False \
       and self.inLuckMiniGame == False and self.inBattleMiniGame == False and self.inCatchMiniGame == False and self.inMiniGame == True:
      return True
    elif action == "inBattleMiniGame" and self.inMiniGame == True and self.inBattleMiniGame == True and self.battle.battleOver == False:
      return True
    elif action == "inLuckMiniGame" and self.inMiniGame == True and self.inLuckMiniGame == True and self.luck.player_guess == False and self.luck.gameOver == False:
      return True
    elif action == "inCatchMiniGame" and self.inMiniGame == True and self.inCatchMiniGame == True:
        if self.catch.can_move(act) == True and self.catch.endGame == False:
            return True
    elif action == "inMazeMiniGame" and self.inMiniGame == True and self.inMazeMiniGame == True:
        if self.maze.can_move(act) == True and self.maze.endGame == False:
            return True
    elif action == "inMemoryMiniGame" and self.inMiniGame == True and self.inMemoryMiniGame == True:
        if self.memory.can_move(act, num) == True and self.memory.endGame == False:
            return True
    elif action == "endCatchGame" and self.inMiniGame == True and self.inCatchMiniGame == True and self.catch.endGame == True:
        return True
    elif action == "endMazeGame" and self.inMiniGame == True and self.inMazeMiniGame == True and self.maze.endGame == True:
        return True
    elif action == "endBattleGame" and self.inMiniGame == True and self.inBattleMiniGame == True and self.battle.battleOver == True:
        return True
    elif action == "endLuckGame" and self.inMiniGame == True and self.inLuckMiniGame == True and (self.luck.player_guess == True or self.luck.gameOver == True):
        return True
    elif action == "endMemoryGame" and self.inMiniGame == True and self.inMemoryMiniGame == True and self.memory.endGame == True:
        return True
    elif action == "endTurn" and self.turn < 5 and len(self.emergencyRoom) == 0 and len(self.waitingRoom) == 0 and self.inMiniGame == False and self.nextScreen == False:
        return True
    elif action == "goToEndOfGameScreen" and self.inMiniGame == False and self.turn == 5 and len(self.waitingRoom) == 0 and len(self.emergencyRoom) == 0 and self.nextScreen == False:
        return True
    elif action == "ranOutOfMoney" and self.checkMoney() == True and self.inMiniGame == False and self.finalScreen == False:
        return True
    elif action == "heartDiseaseInfo" and self.inVisitorCenter == True:
        return True
    elif action == "alzheimersInfo" and self.inVisitorCenter == True:
        return True
    elif action == "lungDiseaseInfo" and self.inVisitorCenter == True:
        return True
    elif action == "cancerInfo" and self.inVisitorCenter == True:
        return True
    elif action == "strokeInfo" and self.inVisitorCenter == True:
        return True
    elif action == "enterVisitorCenter" and self.inARoom == False and self.startGame == True and self.reportScreen == False and self.finalScreen == False:
        return True
    elif action == "exitVisitorCenter" and self.inVisitorCenter == True and self.displayHeartDiseaseInfo == False and self.displayAlzheimersInfo == False and self.displayLungDiseaseInfo == False and self.displayCancerInfo == False and self.displayStrokeInfo == False:
        return True
    elif action == "returnToVisitorCenter" and (self.displayHeartDiseaseInfo == True or self.displayAlzheimersInfo == True or self.displayLungDiseaseInfo == True or self.displayCancerInfo == True or self.displayStrokeInfo == True):
        return True
    else:
      return False
      
  def move(self, action, act = None, num = None):
    news = State(old = self, battle = self.battle, catch = self.catch, maze = self.maze, luck = self.luck, memory = self.memory) # Make a copy of the current state.
    if action == "goIntoLabResources":
      news.inLabResources = True
      news.inWaitingRoom = False
      news.inEmergencyRoom = False
      news.inLabPurchase = False
      news.inARoom = True
    elif action == "startGame":
      news.startGame = True
    elif action == "generalTutorial":
      news.tutorial = True
    elif action == "exitGeneralTutorial":
      news.tutorial = False
    elif action == "goIntoWaitingRoom":
      news.inLabResources = False
      news.inWaitingRoom = True
      news.inEmergencyRoom = False
      news.inLabPurchases = False
      news.inARoom = True
    elif action == "goIntoEmergencyRoom":
      news.inLabResources = False
      news.inWaitingRoom = False
      news.inEmergencyRoom = True
      news.inLabPurchases = False
      news.inARoom = True
    elif action == "enterVisitorCenter":
      news.inLabResources = False
      news.inWaitingRoom = False
      news.inEmergencyRoom = False
      news.inVisitorCenter = True
      news.inARoom = True
    elif action == "exitVisitorCenter":
      news.inARoom = False
      news.inVisitorCenter = False
    elif action == "returnToVisitorCenter":
      news.displayHeartDiseaseInfo = False
      news.displayAlzheimersInfo = False
      news.displayLungDiseaseInfo = False
      news.displayCancerInfo = False
      news.displayStrokeInfo = False
    elif action == "heartDiseaseInfo":
      news.displayStrokeInfo = False
      news.displayCancerInfo = False
      news.displayLungDiseaseInfo = False
      news.displayAlzheimersInfo = False
      news.displayHeartDiseaseInfo = True
    elif action == "alzheimersInfo":
      news.displayStrokeInfo = False
      news.displayCancerInfo = False
      news.displayLungDiseaseInfo = False
      news.displayAlzheimersInfo = True
      news.displayHeartDiseaseInfo = False
    elif action == "lungDiseaseInfo":
      news.displayStrokeInfo = False
      news.displayCancerInfo = False
      news.displayLungDiseaseInfo = True
      news.displayAlzheimersInfo = False
      news.displayHeartDiseaseInfo = False
    elif action == "cancerInfo":
      news.displayStrokeInfo = False
      news.displayCancerInfo = True
      news.displayLungDiseaseInfo = False
      news.displayAlzheimersInfo = False
      news.displayHeartDiseaseInfo = False
    elif action == "strokeInfo":
      news.displayStrokeInfo = True
      news.displayCancerInfo = False
      news.displayLungDiseaseInfo = False
      news.displayAlzheimersInfo = False
      news.displayHeartDiseaseInfo = False
    elif action == "buyStaff":
      news.staff = news.staff + 1
      news.profit = news.profit - 10
    elif action == "strokeMedicine":
      news.medicine["Stroke"] = news.medicine["Stroke"] + 1
      news.profit = news.profit - 200
    elif action == "cancerMedicine":
      news.medicine["Cancer"] = news.medicine["Cancer"] + 1
      news.profit = news.profit - 400
    elif action == "alzhimerMedicine":
      news.medicine["Alzheimer's"] = news.medicine["Alzheimer's"] + 1
      news.profit = news.profit - 400
    elif action == "heartMedicine":
      news.medicine["Heart Disease"] = news.medicine["Heart Disease"] + 1
      news.profit = news.profit - 300
    elif action == "lungMedicine":
      news.medicine["Lung Disease"] = news.medicine["Lung Disease"] + 1
      news.profit = news.profit - 200
    elif action == "investCancer":
      news.cancer = True
      news.profit = news.profit - 600
    elif action == "investLung":
      news.lungDisease = True
      news.profit = news.profit - 600
    elif action == "investStroke":
      news.stroke = True
      news.profit = news.profit - 600
    elif action == "exitLab":
      news.inARoom = False
      news.inLabResources = False
    elif action == "exitWait":
      news.inARoom = False
      news.inWaitingRoom = False
    elif action == "exitEmergency":
      news.inARoom = False
      news.inEmergencyRoom = False
    elif action == "selectPatient1EmergencyRoom":
        if news.emergencyRoom[0].disease == "Cancer":
           news.medicine["Cancer"] = news.medicine["Cancer"] - news.emergencyRoom[0].resources[0]
           news.inBattleMiniGame = True
           news.inMiniGame = True
           news.battle = Battle(self.turn , health = news.emergencyRoom[0].health)
           news.emergencyRoom[0].treated = True
        elif news.emergencyRoom[0].disease == "Stroke":
           news.medicine["Stroke"] = news.medicine["Stroke"] - news.emergencyRoom[0].resources[0]
           news.inCatchMiniGame = True
           news.inMiniGame = True
           news.catch = Catch(None, news.emergencyRoom[0].health)
           news.emergencyRoom[0].treated = True
        elif news.emergencyRoom[0].disease == "Lung Disease":
           news.medicine["Lung Disease"] = news.medicine["Lung Disease"] - news.emergencyRoom[0].resources[0]
           news.inMazeMiniGame = True
           news.inMiniGame = True
           news.maze = Maze(None, news.turn, news.emergencyRoom[0].health)
           news.emergencyRoom[0].treated = True
        elif news.emergencyRoom[0].disease == "Heart Disease":
           news.medicine["Heart Disease"] = news.medicine["Heart Disease"] - news.emergencyRoom[0].resources[0]
           news.inLuckMiniGame = True
           news.inMiniGame = True
           news.luck = Luck(self.turn , health = news.emergencyRoom[0].health)
           news.emergencyRoom[0].treated = True
        elif news.emergencyRoom[0].disease == "Alzheimer's":
           news.medicine["Alzheimer's"] = news.medicine["Alzheimer's"] - news.emergencyRoom[0].resources[0]
           news.inMemoryMiniGame = True
           news.inMiniGame = True
           news.memory = Memory(None, news.turn, news.emergencyRoom[0].health)
           news.emergencyRoom[0].treated = True 
    elif action == "selectPatient2EmergencyRoom":
        if news.emergencyRoom[1].disease == "Cancer":
           news.medicine["Cancer"] = news.medicine["Cancer"] - news.emergencyRoom[1].resources[0]
           news.inBattleMiniGame = True
           news.inMiniGame = True
           news.battle = Battle(self.turn , health = news.emergencyRoom[1].health)
           news.emergencyRoom[1].treated = True
        elif news.emergencyRoom[1].disease == "Stroke":
           news.medicine["Stroke"] = news.medicine["Stroke"] - news.emergencyRoom[1].resources[0]
           news.inCatchMiniGame = True
           news.inMiniGame = True
           news.catch = Catch(None, news.emergencyRoom[1].health)
           news.emergencyRoom[1].treated = True
        elif news.emergencyRoom[1].disease == "Lung Disease":
           news.medicine["Lung Disease"] = news.medicine["Lung Disease"] - news.emergencyRoom[1].resources[0]
           news.inMazeMiniGame = True
           news.inMiniGame = True
           news.maze = Maze(None, news.turn, news.emergencyRoom[1].health)
           news.emergencyRoom[1].treated = True
        elif news.emergencyRoom[1].disease == "Heart Disease":
           news.medicine["Heart Disease"] = news.medicine["Heart Disease"] - news.emergencyRoom[1].resources[0]
           news.inLuckMiniGame = True
           news.inMiniGame = True
           news.luck = Luck(self.turn , health = news.emergencyRoom[1].health)
           news.emergencyRoom[1].treated = True
        elif news.emergencyRoom[1].disease == "Alzheimer's":
           news.medicine["Alzheimer's"] = news.medicine["Alzheimer's"] - news.emergencyRoom[1].resources[0]
           news.inMemoryMiniGame = True
           news.inMiniGame = True
           news.memory = Memory(None, news.turn, news.emergencyRoom[1].health)
           news.emergencyRoom[1].treated = True
    elif action == "selectPatient3EmergencyRoom":
        if news.emergencyRoom[2].disease == "Cancer":
           news.medicine["Cancer"] = news.medicine["Cancer"] - news.emergencyRoom[2].resources[0]
           news.inBattleMiniGame = True
           news.inMiniGame = True
           news.battle = Battle(self.turn , health = news.emergencyRoom[2].health)
           news.emergencyRoom[2].treated = True
        elif news.emergencyRoom[2].disease == "Stroke":
           news.medicine["Stroke"] = news.medicine["Stroke"] - news.emergencyRoom[2].resources[0]
           news.inCatchMiniGame = True
           news.inMiniGame = True
           news.catch = Catch(None, news.emergencyRoom[2].health)
           news.emergencyRoom[2].treated = True
        elif news.emergencyRoom[2].disease == "Lung Disease":
           news.medicine["Lung Disease"] = news.medicine["Lung Disease"] - news.emergencyRoom[2].resources[0]
           news.inMazeMiniGame = True
           news.inMiniGame = True
           news.maze = Maze(None, news.turn, news.emergencyRoom[2].health)
           news.emergencyRoom[2].treated = True
        elif news.emergencyRoom[2].disease == "Heart Disease":
           news.medicine["Heart Disease"] = news.medicine["Heart Disease"] - news.emergencyRoom[2].resources[0]
           news.inLuckMiniGame = True
           news.inMiniGame = True
           news.luck = Luck(self.turn , health = news.emergencyRoom[2].health)
           news.emergencyRoom[2].treated = True
        elif news.emergencyRoom[2].disease == "Alzheimer's":
           news.medicine["Alzheimer's"] = news.medicine["Alzheimer's"] - news.emergencyRoom[2].resources[0]
           news.inMemoryMiniGame = True
           news.inMiniGame = True
           news.memory = Memory(None, news.turn, news.emergencyRoom[2].health)
           news.emergencyRoom[2].treated = True           
    elif action == "selectPatient1WaitingRoom":
        if news.waitingRoom[0].disease == "Cancer":
           news.medicine["Cancer"] = news.medicine["Cancer"] - news.waitingRoom[0].resources[0]
           news.inBattleMiniGame = True
           news.inMiniGame = True
           news.battle = Battle(self.turn , health = news.waitingRoom[0].health)
           news.waitingRoom[0].treated = True
        elif news.waitingRoom[0].disease == "Stroke":
           news.medicine["Stroke"] = news.medicine["Stroke"] - news.waitingRoom[0].resources[0]
           news.inCatchMiniGame = True
           news.inMiniGame = True
           news.catch = Catch(None, news.waitingRoom[0].health)
           news.waitingRoom[0].treated = True
        elif news.waitingRoom[0].disease == "Lung Disease":
           news.medicine["Lung Disease"] = news.medicine["Lung Disease"] - news.waitingRoom[0].resources[0]
           news.inMazeMiniGame = True
           news.inMiniGame = True
           news.maze = Maze(None, news.turn, news.waitingRoom[0].health)
           news.waitingRoom[0].treated = True
        elif news.waitingRoom[0].disease == "Heart Disease":
           news.medicine["Heart Disease"] = news.medicine["Heart Disease"] - news.waitingRoom[0].resources[0]
           news.inLuckMiniGame = True
           news.inMiniGame = True
           news.luck = Luck(self.turn , health = news.waitingRoom[0].health)
           news.waitingRoom[0].treated = True
        elif news.waitingRoom[0].disease == "Alzheimer's":
           news.medicine["Alzheimer's"] = news.medicine["Alzheimer's"] - news.waitingRoom[0].resources[0]
           news.inMemoryMiniGame = True
           news.inMiniGame = True
           news.memory = Memory(None, news.turn, news.waitingRoom[0].health)
           news.waitingRoom[0].treated = True             
    elif action == "battleGame":
      news.battle = news.battle.turnBattle(act)
    elif action == "endBattleGame":
      if news.battle.win == True:
          news.profit = news.profit + 500
          news.patientsTreated += 1
          news.cancerPercent -= 25
          news.turnProfit += 500
          news.cancerPatientsTreated += 1
      else:
          news.cancerPatientsKilled += 1
      news.battle = None
      news.inLabResources = False
      news.inBattleMiniGame = False
      news.inWaitingRoom = False
      news.inEmergencyRoom = False
      news.inLabPurchase = False
      news.inARoom = False
      news.inMiniGame = False
    elif action == "selectPatient2WaitingRoom":
        if news.waitingRoom[1].disease == "Cancer":
           news.medicine["Cancer"] = news.medicine["Cancer"] - news.waitingRoom[1].resources[0]
           news.inBattleMiniGame = True
           news.inMiniGame = True
           news.battle = Battle(self.turn , health = news.waitingRoom[1].health)
           news.waitingRoom[1].treated = True
        elif news.waitingRoom[1].disease == "Stroke":
           news.medicine["Stroke"] = news.medicine["Stroke"] - news.waitingRoom[1].resources[0]
           news.inCatchMiniGame = True
           news.inMiniGame = True
           news.catch = Catch(None, news.waitingRoom[1].health)
           news.waitingRoom[1].treated = True
        elif news.waitingRoom[1].disease == "Lung Disease":
           news.medicine["Lung Disease"] = news.medicine["Lung Disease"] - news.waitingRoom[1].resources[0]
           news.inMazeMiniGame = True
           news.inMiniGame = True
           news.maze = Maze(None, news.turn, news.waitingRoom[1].health)
           news.waitingRoom[1].treated = True
        elif news.waitingRoom[1].disease == "Heart Disease":
           news.medicine["Heart Disease"] = news.medicine["Heart Disease"] - news.waitingRoom[1].resources[0]
           news.inLuckMiniGame = True
           news.inMiniGame = True
           news.luck = Luck(self.turn , health = news.waitingRoom[1].health)
           news.waitingRoom[1].treated = True
        elif news.waitingRoom[1].disease == "Alzheimer's":
           news.medicine["Alzheimer's"] = news.medicine["Alzheimer's"] - news.waitingRoom[1].resources[0]
           news.inMemoryMiniGame = True
           news.inMiniGame = True
           news.inWaitingRoom = False
           news.memory = Memory(None, news.turn, news.waitingRoom[1].health)
           news.waitingRoom[1].treated = True           
    elif action == "catchGame":
      news.catch = news.catch.turnCatch(act)
    elif action == "endCatchGame":
      if news.catch.win == True:
          news.profit = news.profit + 400
          news.patientsTreated += 1
          news.strokePercent -= 25
          news.turnProfit += 400
          news.strokePatientsTreated += 1
      else:
          news.strokePatientsKilled += 1
      news.catch = None
      news.inCatchMiniGame = False
      news.inLabResources = False
      news.inWaitingRoom = False
      news.inEmergencyRoom = False
      news.inLabPurchase = False
      news.inARoom = False
      news.inMiniGame = False
    elif action == "selectPatient3WaitingRoom":
      if news.waitingRoom[2].disease == "Cancer":
           news.medicine["Cancer"] = news.medicine["Cancer"] - news.waitingRoom[2].resources[0]
           news.inBattleMiniGame = True
           news.inMiniGame = True
           news.battle = Battle(self.turn , health = news.waitingRoom[2].health)
           news.waitingRoom[2].treated = True
      elif news.waitingRoom[2].disease == "Stroke":
           news.medicine["Stroke"] = news.medicine["Stroke"] - news.waitingRoom[2].resources[0]
           news.inCatchMiniGame = True
           news.inMiniGame = True
           news.catch = Catch(None, news.waitingRoom[2].health)
           news.waitingRoom[2].treated = True
      elif news.waitingRoom[2].disease == "Lung Disease":
           news.medicine["Lung Disease"] = news.medicine["Lung Disease"] - news.waitingRoom[2].resources[0]
           news.inMazeMiniGame = True
           news.inMiniGame = True
           news.maze = Maze(None, news.turn, news.waitingRoom[2].health)
           news.waitingRoom[2].treated = True
      elif news.waitingRoom[2].disease == "Heart Disease":
           news.medicine["Heart Disease"] = news.medicine["Heart Disease"] - news.waitingRoom[2].resources[0]
           news.inLuckMiniGame = True
           news.inMiniGame = True
           news.luck = Luck(self.turn , health = news.waitingRoom[2].health)
           news.waitingRoom[2].treated = True
      elif news.waitingRoom[2].disease == "Alzheimer's":
           news.medicine["Alzheimer's"] = news.medicine["Alzheimer's"] - news.waitingRoom[2].resources[0]
           news.inMemoryMiniGame = True
           news.inMiniGame = True
           news.memory = Memory(None, news.turn, news.waitingRoom[2].health)
           news.waitingRoom[2].treated = True            
    elif action == "mazeGame":
      news.maze = news.maze.turnMaze(act)
    elif action == "endMazeGame":
      if news.maze.win == True:
          news.profit = news.profit + 400
          news.patientsTreated += 1
          news.lungDiseasePercent -= 25
          news.turnProfit += 400
          news.lungDiseasePatientsTreated += 1
      else:
          news.lungDiseasePatientsKilled += 1
      news.maze = None
      news.inMazeMiniGame = False
      news.inLabResources = False
      news.inWaitingRoom = False
      news.inEmergencyRoom = False
      news.inLabPurchase = False
      news.inARoom = False
      news.inMiniGame = False
    elif action == "luckGame":
      news.luck = news.luck.turnLuck(act)
    elif action == "endLuckGame":
      if news.luck.player_guess == True:
          news.profit = news.profit + 600
          news.patientsTreated += 1
          news.heartDiseasePercent -= 20
          news.turnProfit += 500
          news.heartDiseasePatientsTreated += 1
      else:
          news.heartDiseasePatientsKilled += 1
      news.luck = None
      news.inLuckMiniGame = False
      news.inLabResources = False
      news.inBattleMiniGame = False
      news.inWaitingRoom = False
      news.inEmergencyRoom = False
      news.inLabPurchase = False
      news.inARoom = False
      news.inMiniGame = False
    elif action == "memoryGame":
      news.memory = news.memory.turnMemory(act, num)
    elif action == "endMemoryGame":
      if news.memory.win == True:
          news.profit = news.profit + 500
          news.patientsTreated += 1
          news.alzheimersPercent -= 20
          news.turnProfit += 500
          news.alzheimersPatientsTreated += 1
      else:
          news.alzheimersPatientsKilled += 1
      news.memory = None
      news.inMemoryMiniGame = False
      news.inLabResources = False
      news.inWaitingRoom = False
      news.inEmergencyRoom = False
      news.inLabPurchase = False
      news.inARoom = False
      news.inMiniGame = False
    elif action == "reportScreen":
      news.inARoom = False
      news.inLabResources = False
      news.reportScreen = True
    elif action == "nextTurn":
      news.getPatients(news.turn)
      news.reportScreen = False
      news.inARoom = False
      news.inLabResources = False
      news.endTurn = False
      news.nextScreen = False
      news.inMiniGame = False
      news.turnProfit = 0
      news.inWaitingRoom = False
      news.inEmergencyRoom = False
      news.inLabPurchase = False
      news.heartDiseasePatientsTreated = 0
      news.lungDiseasePatientsTreated = 0
      news.alzheimersPatientsTreated = 0
      news.strokePatientsTreated = 0
      news.cancerPatientsTreated = 0
      news.heartDiseasePatientsKilled = 0
      news.lungDiseasePatientsKilled = 0
      news.alzheimersPatientsKilled = 0
      news.strokePatientsKilled = 0
      news.cancerPatientsKilled = 0
    elif action == "endTurn":
      news.turn += 1
      news.inLabResources = True
      news.inARoom = True
      news.endTurn = True
      news.nextScreen = True
      news.inWaitingRoom = False
      news.inEmergencyRoom = False
    elif action == "goToEndOfGameScreen":
        news.finalScreen = True
    news.removePatients()
    return news

  def checkMoney(self):
      cost = 0
      for i in range(len(self.waitingRoom)):
          if self.medicine[self.waitingRoom[i].disease] >= self.waitingRoom[i].resources[0] and self.staff >= self.waitingRoom[i].resources[1]:
              return False
          if self.medicine[self.waitingRoom[i].disease] < self.waitingRoom[i].resources[0]:
              cost = self.medicineCost[self.waitingRoom[i].disease]
          if self.staff < self.waitingRoom[i].resources[1]:
              cost += (self.waitingRoom[i].resources[1] - self.staff)*10
          if self.profit >= cost:
              return False
      for i in range(len(self.emergencyRoom)):
          if self.medicine[self.emergencyRoom[i].disease] >= self.emergencyRoom[i].resources[0] and self.staff >= self.emergencyRoom[i].resources[1]:
              return False
          if self.medicine[self.emergencyRoom[i].disease] < self.emergencyRoom[i].resources[0]:
              cost = self.medicineCost[self.emergencyRoom[i].disease]
          if self.staff < self.emergencyRoom[i].resources[1]:
              cost += (self.emergencyRoom[i].resources[1] - self.staff)*10
          if self.profit >= cost:
              return False
      if len(self.waitingRoom) == 0 and len(self.emergencyRoom) == 0:
          return False
      return True 
  
  def removePatients(self):
      for i in range(len(self.waitingRoom)):
          try:
              if self.waitingRoom[i].treated == True:
                  self.waitingRoom.pop(i)
          except:
              pass
      for i in range(len(self.emergencyRoom)):
          try:
              if self.emergencyRoom[i].treated == True:
                  self.emergencyRoom.pop(i)
          except:
              pass

  def getPatients(self, turn):
      self.waitingRoom = []
      self.emergencyRoom = []
      if(turn == 1):
        self.waitingRoom.append(Patient("Heart Disease", "Fair", [1, 5], "Asia", "patient3.jpg"))
        self.totalPatients += 1
        self.waitingRoom.append(Patient("Alzheimer's", "Fair", [1, 5], "Europe", "patient2.jpg"))
        self.totalPatients += 1
        self.waitingRoom.append(Patient("Heart Disease", "Poor", [1, 5], "South America", "patient1.jpg"))
        self.totalPatients += 1
      elif(turn == 2):
        self.waitingRoom.append(Patient("Alzheimer's", "Fair", [1, 5], "Asia", "patient2.jpg"))
        self.totalPatients += 1
        self.emergencyRoom.append(Patient("Heart Disease", "Critical", [1, 5], "Asia", "patient3.jpg"))
        self.totalPatients += 1
        if self.lungDisease == True:
            self.waitingRoom.append(Patient("Lung Disease", "Poor", [1, 10], "South America", "patient1.jpg"))
            self.totalPatients += 1
        self.emergencyRoom.append(Patient("Alzheimer's", "Critical", [1, 5], "North America", "patient2.jpg"))
        self.totalPatients += 1
      elif(turn == 3):
        if self.cancer == True:
            self.waitingRoom.append(Patient("Cancer", "Poor", [1, 15], "Australia", "patient1.jpg"))
            self.totalPatients += 1
        if self.lungDisease == True:
            self.waitingRoom.append(Patient("Lung Disease", "Fair", [1, 10], "Oceania", "patient3.jpg"))
            self.totalPatients += 1
        if self.lungDisease == True:
            self.emergencyRoom.append(Patient("Lung Disease", "Critical", [1, 10], "Africa", "patient2.jpg"))
            self.totalPatients += 1
        self.emergencyRoom.append(Patient("Heart Disease", "Critical", [1, 5], "North America", "patient1.jpg"))
        self.totalPatients += 1
      elif(turn == 4):
        self.waitingRoom.append(Patient("Alzheimer's", "Fair", [1, 5], "Asia", "patient3.jpg"))
        self.totalPatients += 1
        if self.stroke == True:
            self.waitingRoom.append(Patient("Stroke", "Poor", [1, 20], "Europe", "patient1.jpg"))
            self.totalPatients += 1
        if self.stroke == True:
            self.emergencyRoom.append(Patient("Stroke", "Critical", [1, 20], "Africa", "patient2.jpg"))
            self.totalPatients += 1
        if self.lungDisease == True:
            self.emergencyRoom.append(Patient("Lung Disease", "Critical", [1, 10], "Africa", "patient3.jpg"))
            self.totalPatients += 1
        if self.cancer == True:
            self.emergencyRoom.append(Patient("Cancer", "Critical", [1, 15], "North America", "patient1.jpg"))
            self.totalPatients += 1
      elif(turn == 5):
        self.waitingRoom.append(Patient("Heart Disease", "Fair", [1, 5], "Asia", "patient3.jpg"))
        self.totalPatients += 1
        if self.stroke == True:
            self.waitingRoom.append(Patient("Stroke", "Poor", [1, 20], "Europe", "patient1.jpg"))
            self.totalPatients += 1
        if self.cancer == True:
            self.waitingRoom.append(Patient("Cancer", "Fair", [1, 15], "Europe", "patient2.jpg"))
            self.totalPatients += 1
        if self.stroke == True:
            self.emergencyRoom.append(Patient("Stroke", "Critical", [1, 20], "Africa", "patient1.jpg"))
            self.totalPatients += 1
        self.emergencyRoom.append(Patient("Alzheimer's", "Critical", [1, 5], "North America", "patient2.jpg"))
        self.totalPatients += 1
        if self.cancer == True:
            self.emergencyRoom.append(Patient("Cancer", "Critical", [1, 15], "South America", "patient3.jpg"))
            self.totalPatients += 1
        
  def describe_state(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    s = "The state of the game at this point in time is as follows:\n" 
    if not self.battle is None:
        s+= "The player is currently treating a patient with cancer and is playing the battle mini game.\n"
    else:
        s+= "The player is not currently treating a patient with cancer.\n"
    if not self.luck is None:
        s+= "The player is currently treating a patient with heart disease and is playing the luck mini game.\n"
    else:
        s+= "The player is not currently treating a patient with heart disease.\n"
    if not self.maze is None:
        s+= "The player is currently treating a patient with lung disease and is playing the maze mini game.\n"
    else:
        s+= "The player is not currently treating a patient with lung disease.\n"
    if not self.catch is None:
        s+= "The player is currently treating a patient with stroke and is playing the catch mini game.\n"
    else:
        s+= "The player is not currently treating a patient with stroke.\n"
    if self.inWaitingRoom == False:
        s+= "The player is currently not in the waiting room.\n"
    else:
        s+= "The player is currently in the waiting room.\n"
    if self.inEmergencyRoom == False:
        s+= "The player is currently not in the emergency room.\n"
    else:
        s+= "The player is currently in the emergency room.\n"
    if self.inLabResources == False:
        s+= "The player is currently not in the lab resources room.\n"
    else:
        s+= "The player is currently in the lab resources room.\n"
    if self.inLabPurchases == False:
        s+= "The player is currently not in the lab purchases room.\n"
    else:
        s+= "The player is currently in the lab purchases room.\n"
    s+= "It is currently turn number " + str(self.turn) + ".\n"
    s+= "The patients in the waiting room as of now are:\n"
    for p in self.waitingRoom:
        s+= p.__str__() + "\n"
    s+= "The patients in the emergency room as of now are:\n"
    for p in self.emergencyRoom:
        s+= p.__str__() + "\n"
    if self.cancer == True:
        s+= "The player currently has cancer patients treatment unlocked.\n"
    else:
        s+= "The player currently does not have cancer patients treatment unlocked.\n"
    if self.lungDisease == True:
        s+= "The player currently has lung disease patients treatment unlocked.\n"
    else:
        s+= "The player currently does not have lung disease patients treatment unlocked.\n"
    if self.stroke == True:
        s+= "The player currently has stroke patients treatment unlocked.\n"
    else:
        s+= "The player currently does not have alzheimer patients treatment unlocked.\n"
    s+= "The player currently has heart disease patients treatment unlocked.\n"
    s+= "The player currently has stroke patients treatment unlocked.\n"
    s+= "The player currently has " + str(self.staff) + " staff working in the hospital.\n"
    s+= "The player currently has " + str(self.profit) + " dollars.\n"
    s+= "The player currently has the following medicines and quantities:\n"
    for m in self.medicine:
        s+= m + ": " + str(self.medicine[m]) + "\n"
    return s

  def is_goal(self):
    '''If the cube has 6 faces with each face consisting of a single color, then s is a goal state.'''
    return False
  
  def __eq__(self, s2):
    if self.inARoom != s2.inARoom: return False
    if self.medicineCost != s2.medicineCost: return False
    if self.turnProfit != s2.turnProfit: return False
    if self.heartDiseasePatientsTreated != s2.heartDiseasePatientsTreated: return False
    if self.lungDiseasePatientsTreated != s2.lungDiseasePatientsTreated: return False
    if self.alzheimersPatientsTreated != s2.alzheimersPatientsTreated: return False
    if self.strokePatientsTreated != s2.strokePatientsTreated: return False
    if self.cancerPatientsTreated != s2.cancerPatientsTreated: return False 
    if self.heartDiseasePatientsKilled != s2.heartDiseasePatientsKilled: return False
    if self.lungDiseasePatientsKilled != s2.lungDiseasePatientsKilled: return False
    if self.alzheimersPatientsKilled != s2.alzheimersPatientsKilled: return False
    if self.strokePatientsKilled != s2.strokePatientsKilled: return False
    if self.cancerPatientsKilled != s2.cancerPatientsKilled: return False
    if self.finalScreen != s2.finalScreen: return False
    if self.patientsTreated != s2.patientsTreated: return False
    if self.totalPatients != s2.totalPatients: return False
    if self.cancerPercent != s2.cancerPercent: return False
    if self.heartDiseasePercent != s2.heartDiseasePercent: return False
    if self.lungDiseasePercent != s2.lungDiseasePercent: return False
    if self.alzheimersPercent != s2.alzheimersPercent: return False
    if self.strokePercent != s2.strokePercent: return False
    if self.startGame != s2.startGame: return False
    if self.nextScreen != s2.nextScreen: return False
    if self.endTurn != s2.endTurn: return False
    if self.reportScreen != s2.reportScreen: return False
    if self.turn != s2.turn: return False
    if self.inWaitingRoom != s2.inWaitingRoom: return False
    if self.inEmergencyRoom != s2.inEmergencyRoom: return False
    if self.inLabResources != s2.inLabResources: return False
    if self.inLabPurchases != s2.inLabPurchases: return False
    if self.waitingRoom != s2.waitingRoom[:]: return False
    if self.emergencyRoom != s2.emergencyRoom[:]: return False
    if self.inMiniGame != s2.inMiniGame: return False
    if self.inCatchMiniGame != s2.inCatchMiniGame: return False
    if self.inMazeMiniGame != s2.inMazeMiniGame: return False
    if self.inMemoryMiniGame != s2.inMemoryMiniGame: return False
    if self.inLuckMiniGame != s2.inLuckMiniGame: return False
    if self.inBattleMiniGame != s2.inBattleMiniGame: return False
    if self.inARoom != s2.inARoom: return False
    if self.staff != s2.staff: return False
    if self.medicine != s2.medicine: return False
    if self.profit != s2.profit: return False
    if self.cancer != s2.cancer: return False
    if self.lungDisease != s2.lungDisease: return False
    if self.stroke != s2.stroke: return False
    return True

  def __str__(self):
    s = ""
    if self.startGame == False:
        s = "\nWelcome to Chronic Disease Crisis! \n Start the game to enter the hospital.\nView the tutorial to gain a better understanding of the game\n"
    if self.tutorial == True:
        s = "\nThis is the tutorial for the game."
    if self.inARoom == False and self.startGame == True:
        s = "\nWelcome to the Global Hospital! \n The purpose is to treat and research chronics diseases that are facing our world today. \n Please enter one of the rooms and start healing patients!"
    if self.inWaitingRoom == True:
        s = "\nThis is the waiting room. \n Patients in here are at different moderate conditions and need to be treated. \n Some patients require a certain amount of staff and medicine. \n Those utilities can be purchased in the Lab."    
    if self.inLabResources == True and self.endTurn == True:
        s = "\nGo and purchase medicine for the next round of patients!\nDon't forget to invest in new diseases!"   
    if self.reportScreen == True:
        s = "\nHere are the statistics for round " + str(self.turn - 1) + "!" 
    if self.finalScreen == True:
        s = "\nYou complted the game!\nThe table above shows you how well you did!"
    if self.inLabResources == True and self.endTurn == False:
        s = "\nThis is the resource lab. \n Here you can purchase certain disease medications, staff for treatment, or invest in research on a disease. \n All research costs $600. "
    if self.inEmergencyRoom == True:
        s = "\nThis is the emergency room. \n Patients in here are in critical condition and need to be treated. \n Some patients require a certain amount of staff and medicine. \n Those utilities can be purchased in the Lab.\nIt is harder to treat these patients!"     
    if not self.catch is None:
      s = "\nAs the White Blood Cell try to catch the threatening Red Blood Cell to cure the Patient \n"
    if not self.maze is None:
      s = "\nFind your way through the lung to tackle the source of the lung disease. \nYou have " + str(self.maze.maxMoves - self.maze.attempts) + " steps left!"
    if not self.luck is None:
      s = "\nSelect the right part of the heart that is affected by heart disease. \nYou have " + str(self.luck.maxMoves - self.luck.turn_counter) + " guesses left!"
    if not self.battle is None:
      s = "\nFight off the cancer cell in a battle! \nLook at the Shell/Console/Prints \nBattle Healths:\n" 
      s += str(self.battle.goodCellHealth) + " Good | Bad " + str(self.battle.badCellHealth)
    if not self.memory is None:
      s = "\nScroll through the images.\nSelect the correct order of picutres.\n"
    return s

  def __hash__(self):
    return (str(self)).__hash__()

  def goal_message(self):
    return "Congratulations on successfully solving the Game"

def copy_state(s):
  return State(old=s)

class Patient:
  def __init__(self, disease, health, resources, nationality, image):
      self.disease = disease
      self.health = health
      self.resources = resources
      self.nationality = nationality
      self.treated = False
      self.image = image
      
  def __str__(self):
      s = "This patient suffers\nfrom " + self.disease + ".\nTheir health\ncondition is " + str(self.health)
      s+= ".\nIn order to treat\nthis patient\nyou will need:\n" + str(self.resources[0]) + " medicine and " + str(self.resources[1]) + " staff.\n"
      s+= "You will get "
      if self.disease == "Heart Disease":
          s+= "600 "
      elif self.disease == "Alzheimer's":
          s+= "500 "
      elif self.disease == "Lung Disease":
          s+= "400 "
      elif self.disease == "Cancer":
          s+= "500 "
      elif self.disease == "Stroke":
          s+= "400 "
      s+= "\ndollars for curing\nthis patient\nand no money\nif they die.\n"
      return s

class Luck:
    def __init__(self, turn = 1, old=None, health = "Fair"):
        self.gameTurn = turn
        self.cup1 = False
        self.cup2 = False
        self.cup3 = False
        self.correctCup = 0
        if self.gameTurn == 1:
            self.cup1 = True
            self.correctCup = 0
        elif self.gameTurn == 2:
            self.cup3 = True
            self.correctCup = 2
        elif self.gameTurn == 3:
            self.cup2 = True
            self.correctCup = 1
        elif self.gameTurn == 5:
            self.cup3 = True
            self.correctCup = 2
        self.cups = [self.cup1, self.cup2, self.cup3]
        self.player_guess = False
        self.turn_counter = 0
        self.previousGuess = 0
        self.gameOver = False
        self.maxMoves = 2
        if health == "Critical":
            self.maxMoves = 1
        if not old is None:
            self.cup1 = old.cup1
            self.cup2 = old.cup2
            self.cup3 = old.cup3
            self.correctCup = old.correctCup
            self.cups = old.cups
            self.player_guess = old.player_guess
            self.turn_counter = old.turn_counter
            self.previousGuess = old.previousGuess
            self.gameOver = old.gameOver
            self.maxMoves = old.maxMoves
            self.gameTurn = old.gameTurn

    def turnLuck(self, selected):
        '''Assuming it's legal to make the move, this make a new state
        representing the result of moving the boat carrying
        m missionaries and c cannibals.'''
        news = Luck(old=self)  # Make a copy of the current state.
        if news.cups[selected] == True:
            news.player_guess = True
        else:
            news.player_guess = False
        news.turn_counter += 1
        news.previousGuess = selected
        if news.turn_counter == news.maxMoves:
            news.gameOver = True
        return news

class Memory:
    def __init__(self, old=None, turn=1, condition=None):
    # Default new state is a state objects initialized as the
    # initial state.
    # If called with old equal to a non-empty state, then
    # the new instance is made to be a copy of that state.
    #Basketball = Red, Tennis Ball = Green
        self.order1 = ["basketball.jpg", "tennis.jpg", "bowling.jpg", "soccer.jpg", "baseball.jpg"]
        self.order2 = ["grape.jpg", "banana.jpg", "apple.jpg", "pineapple.jpg", "orange.jpg"]
        self.order3 = ["steve3.jpg", "stevecarell.jpg", "stevetanimoto.jpg", "steveharvey.jpg", "stevejobs.jpg", "steveminecraft.jpg", "steve2.jpg"]
        self.order4 = ["colorPens.jpg", "markers.jpg", "pen.jpg", "pencil.jpg", "sharpie.jpg"]
        self.order5 = ["polarbear.jpg", "dolphin.jpg", "deer.jpg", "giraffe.jpg", "rhino.jpg", "snake.jpg", "raven.jpg"]
        self.list_of_orders = [self.order1, self.order2, self.order3, self.order4, self.order5]
        self.user_pick = None
        self.correct_answers = [2, 0, 0, 3, 2]
        self.attempts = 0
        self.turn = turn
        self.condition = condition
        self.current_order = 0
        self.win = False
        self.endGame = False
        if self.turn == 1:
                self.current_order = 0
        elif self.turn == 2 and self.condition == "Critical":
                self.current_order = 2
        elif self.turn == 2:
                self.current_order = 1
        elif self.turn == 4:
                self.current_order = 3
        elif self.turn == 5:
                self.current_order = 4
        self.current_image = 0
        if not old is None:
          self.user_pick = old.user_pick
          self.attempts = old.attempts
          self.turn = old.turn
          self.condition = old.condition
          self.current_order = old.current_order
          self.current_image = old.current_image
          self.win = old.win
          self.endGame = old.endGame
      
      #Rest of the variables don't need to be updated every turn

    def can_move(self, play_type, order):
        '''Tests whether it's legal for the player to pick an option'''
        if play_type == "progress":
            if self.current_image < len(self.list_of_orders[self.current_order]) - 1:
                return True
            else:
                return False
        elif play_type == "answer" and order == self.current_order:
            if self.current_image == len(self.list_of_orders[self.current_order]) - 1:
                return True
        else:
            return False
    
    def turnMemory(self, play_type, pick):
        '''Assuming it's legal to make the move, this make a new state
        representing the choice made by the user'''
        news = Memory(old = self)
        if play_type == "progress":
            news.current_image += 1
        else:
            news.user_pick = pick
            news.attempts += 1
        if news.user_pick == news.correct_answers[news.current_order]:
            news.win = True
            news.endGame = True
        if news.attempts > 0:
            news.endGame = True
        return news

class Maze:
  def __init__(self, old=None, turn=1, condition="fair"):
    # Default new state is a state objects initialized as the
    # initial state.
    # If called with old equal to a non-empty state, then
    # the new instance is made to be a copy of that state.
    self.maze1 = [["X", 1, 1, 0, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
                  [0, 0, 1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 0], \
                  [0, 0, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
                  [0, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], \
                  [1, 0, 0, 1, 1, 0, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1, 0, 0, 1, 0]] 
    
    self.maze2 = [["X", 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 0, 1, 0], \
                  [1, 0, 1, 0, 0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
                  [0, 1, 1, 0, 1, 0, 1, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0, 0, 0], \
                  [0, 0, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0, 1, 0, 0, 0], \
                  [1, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 1, 0, 0]]
    
    self.maze3 = [["X", 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 1, 1, 0, 0], \
                  [0, 1, 1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
                  [0, 1, 1, 0, 1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0], \
                  [0, 1, 1, 0, 1, 0, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0, 1, 1, 0, 0], \
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 0, 0, 1, 0]] 
    self.list_of_mazes = [None, self.maze1, self.maze2, self.maze3] #Matches turns where COPD patients are available
    self.cr = 0
    self.cl = 0
    self.turn = turn
    self.current_maze = self.list_of_mazes[turn - 1]
    self.condition = condition
    self.attempts = 0
    self.maxMoves = 20
    if self.condition == "Critical":
        self.maxMoves = 40
    self.endGame = False
    self.win = False
    if not old is None:
      self.cr = old.cr
      self.cl = old.cl
      self.maze1 = old.maze1
      self.maze2 = old.maze2
      self.maze3 = old.maze3
      self.turn = old.turn
      self.condition = old.condition
      self.current_maze = old.current_maze
      self.attempts = old.attempts
      self.endGame = old.endGame
      self.win = old.win
      self.maxMoves = old.maxMoves

  def can_move(self, direction):
    '''Tests whether it's legal to move the player either up, down,
    left, or right'''
    try:
        new_r, new_c = self.cr, self.cl
        if (direction % 2) == 0:
            new_r += int(direction / 2)
        else:
            new_c += direction
            
        if self.current_maze[new_r][new_c] == 0 and not new_r == -1 and not new_c == -1:
            return True
        else:
            return False
    except:
        return False

  def turnMaze(self, direction):
    '''Assuming it's legal to make the move, this make a new state
    representing the result of moving the player to the next spot
    in the maze'''
    news = Maze(old = self)
    if (direction % 2) == 0:
        news.cr = self.cr + int(direction / 2)
    else:
        news.cl = self.cl + direction
    news.current_maze[news.cr][news.cl] = "X"
    news.current_maze[self.cr][self.cl] = 0
    if news.attempts == 39 and news.condition == "Critical":
        news.endGame = True
    elif news.attempts == 19 and (news.condition == "Fair" or news.condition == "Poor"):
        news.endGame = True
    if news.current_maze[9][9] == "X":
        news.endGame = True
        news.win = True
    news.attempts += 1
    return news

import time
import copy

class Catch:
  def __init__(self, old=None, condition = ""):
    self.condition = condition
    self.board = [[" " for row in range(4)] for column in range(4)]
    self.redLocation = [3, 3]
    self.whiteLocation = [0, 0]
    self.computerMoves = ["Left", "Left", "Right", "Right"]
    self.moves = 20
    
    if self.condition == "Critical":
        self.board = [[" " for row in range(6)] for column in range(6)]
        self.redLocation = [5, 5]
        self.whiteLocation = [0, 0]
        self.computerMoves = ["Up", "Left", "Left", "Up", "Down", "Right", "Right", "Up", "Left", "Right", "Down", "Down"]
        self.moves = 15        
        
    self.board[self.redLocation[0]][self.redLocation[1]] = "X"
    self.board[self.whiteLocation[0]][self.whiteLocation[1]] = "O"
   
    self.computerTurn = 0
    self.turn = 0
    self.endGame = False
    self.win = False
    
    if not old is None:
        self.computerMoves = copy.deepcopy(old.computerMoves)
        self.board = old.board
        self.endGame = old.endGame
        self.computerTurn = old.computerTurn
        self.turn = old.turn
        self.redLocation = copy.deepcopy(old.redLocation)
        self.whiteLocation = copy.deepcopy(old.whiteLocation)
        self.moves = old.moves
        self.condition = old.condition
        self.win = old.win
        
  def can_move(self, action):
      if action == "Up" and self.whiteLocation[0] - 1 == -1:
          return False
      if action == "Down" and self.whiteLocation[0] + 1 == len(self.board):
          return False
      if action == "Left" and self.whiteLocation[1] - 1 == -1:
          return False
      if action == "Right" and self.whiteLocation[1] + 1 == len(self.board):
          return False
      return True
  
  def turnCatch(self, action):
    news = Catch(old = self) # Make a copy of the current state.
    news.board[news.whiteLocation[0]][news.whiteLocation[1]] = " "
    if action == "Up":
          news.moves = news.moves - 1
          news.board[news.whiteLocation[0] - 1][news.whiteLocation[1]] = "O"
          news.whiteLocation = [news.whiteLocation[0] - 1,news.whiteLocation[1]]
    elif action == "Down":
          news.moves = news.moves - 1
          news.board[news.whiteLocation[0] + 1][news.whiteLocation[1]] = "O"
          news.whiteLocation = [news.whiteLocation[0] + 1,news.whiteLocation[1]]
    elif action == "Left":
          news.moves = news.moves - 1
          news.board[news.whiteLocation[0]][news.whiteLocation[1] - 1] = "O"
          news.whiteLocation = [news.whiteLocation[0], news.whiteLocation[1] - 1]
    elif action == "Right":
          news.moves = news.moves - 1
          news.board[news.whiteLocation[0]][news.whiteLocation[1] + 1] = "O"
          news.whiteLocation = [news.whiteLocation[0],news.whiteLocation[1] + 1]
    print("Red's Turn!")
    if news.board[news.redLocation[0]][news.redLocation[1]] == " " or news.board[news.redLocation[0]][news.redLocation[1]] == "X":
        news.board[news.redLocation[0]][news.redLocation[1]] = " "        
    redCellMove = news.computerMoves[news.computerTurn]
    if redCellMove == "Up":
        news.board[news.redLocation[0] - 1][news.redLocation[1]] = "X"
        news.redLocation = copy.deepcopy([news.redLocation[0] - 1,news.redLocation[1]])
        news.computerTurn = news.computerTurn + 1
    elif redCellMove == "Down":
        news.board[news.redLocation[0] + 1][news.redLocation[1]] = "X"
        news.redLocation = copy.deepcopy([news.redLocation[0] + 1,news.redLocation[1]])
        news.computerTurn = news.computerTurn + 1
    elif redCellMove == "Left":
        news.board[news.redLocation[0]][news.redLocation[1] - 1] = "X"
        news.redLocation = copy.deepcopy([news.redLocation[0],news.redLocation[1] - 1])
        news.computerTurn = news.computerTurn + 1
    elif redCellMove == "Right":
        news.board[news.redLocation[0]][news.redLocation[1] + 1] = "X"
        news.redLocation = copy.deepcopy([news.redLocation[0],news.redLocation[1] + 1])
        news.computerTurn = news.computerTurn + 1
    if news.redLocation == news.whiteLocation:
        news.board[news.whiteLocation[0]][news.whiteLocation[1]] = "O"
        news.endGame = True
        news.win = True
        print("Nice Job! You Won!")
    print(news.redLocation)
    if (news.computerTurn) == len(news.computerMoves):
        news.computerTurn = 0
    if news.moves == 0:
        if news.redLocation == news.whiteLocation:
            news.board[news.whiteLocation[0]][news.whiteLocation[1]] = "O"
            news.endGame = True
            news.win = True
            print("Nice Job! You Won!")
        else:
            news.endGame = True
            news.win = False
            print("You Lost!")
    return news

#Battle minigame to be used for patients with cancer
from random import randint
class Battle:
  def __init__(self, turn = 1, health = "Fair",old = None):
    #Sets up attributes for both "fighters" and their moves
    self.gameTurn = turn
    self.badCellHealth = 100
    self.badCellDamage = 33
    self.highPower = 2
    self.lowPower = 1
    self.hinderPower = 0.67
    self.hinderAcc = 75
    self.healPower = 1.4
    goodCellHealth = 100
    if health == "Critical":
        goodCellHealth = 50
    self.goodCellHealth = goodCellHealth
    self.goodCellDamage = 33
    self.computerMoveCount = 0
    moves = []
    if self.gameTurn == 3:
        moves = ["heavy","heal","accurate","hinder"]
    elif self.gameTurn == 4:
        moves = ["hinder","heal","accurate","heavy"]
    elif self.gameTurn == 5:
        moves = ["accurate","heavy","heal","hinder"]
    self.computerMoves = moves
    self.initialHealthGoodCell = goodCellHealth
    self.battleOver = False
    self.win = False
    if not old is None:
        self.gameTurn = old.gameTurn
        self.badCellHealth = old.badCellHealth
        self.badCellDamage = old.badCellDamage
        self.highPower = old.highPower
        self.computerMoveCount = old.computerMoveCount
        self.lowPower = old.lowPower
        self.hinderPower = old.hinderPower
        self.healPower = old.healPower
        self.goodCellHealth = old.goodCellHealth
        self.goodCellDamage = old.goodCellDamage
        self.computerMoves = old.computerMoves
        self.initialHealthGoodCell = old.initialHealthGoodCell
        self.battleOver = old.battleOver
        self.win = old.win

  def turnBattle(self,action):
    newb = Battle(old=self)
    if action == "accurate":
      newb.badCellHealth -= newb.goodCellDamage * newb.lowPower
      print("The white blood cell hit the cancerous cell for " + str(newb.goodCellDamage * newb.lowPower) + " damage.")
    elif action == "heavy":
      newb.badCellHealth -= newb.goodCellDamage * newb.highPower
      newb.goodCellHealth -= newb.goodCellDamage * newb.lowPower
      print("The white blood cell hit the cancerous cell for " + str(newb.goodCellDamage * newb.highPower) + " damage."\
            + " The white blood cell was hurt by recoil.")
    elif action == "heal":
      heal = int(newb.goodCellDamage * newb.healPower)
      if heal + newb.goodCellHealth > newb.initialHealthGoodCell:
        heal = newb.initialHealthGoodCell - newb.goodCellHealth
      newb.goodCellHealth += heal
      print("The white blood cell healed " + str(heal) + " hitpoints.")
    elif action == "hinder":
      newb.badCellDamage = int(newb.badCellDamage * newb.hinderPower)
      if newb.badCellDamage == 0:
        newb.badCellDamage = 1
      print("The cancerous cell's damage was decreased to " + str(newb.badCellDamage) + " power.")
    if newb.badCellHealth > 0:
      action = newb.computerMoves[newb.computerMoveCount]
      newb.computerMoveCount += 1
      if newb.computerMoveCount == len(newb.computerMoves):
        newb.computerMoveCount = 0
      if action == "accurate":
        newb.goodCellHealth -= newb.badCellDamage * newb.lowPower
        print("The cancerous cell hit the whitle blood cell for " + str(newb.badCellDamage * newb.lowPower) + " damage.")
      elif action == "heavy":
        newb.goodCellHealth -= newb.badCellDamage * newb.highPower
        newb.badCellHealth -= newb.badCellDamage * newb.lowPower
        print("The cancerous cell hit the whitle blood cell for " + str(newb.badCellDamage * newb.highPower) + " damage." \
              + " The cancerous cell was hurt by recoil.")
      elif action == "heal":
        heal = int(newb.badCellDamage * newb.healPower)
        if newb.badCellHealth + heal > 100:
          heal = 100 - newb.badCellHealth
        newb.badCellHealth += heal
        print("The cancerous cell healed " + str(heal) + " hitpoints.")
      elif action == "hinder":
        newb.goodCellDamage = int(newb.goodCellDamage * newb.hinderPower)
        if newb.goodCellDamage == 0:
          newb.goodCellDamage = 1
        print("The white blood cell's damage was decreased to " + str(newb.goodCellDamage) + " power.")
      if newb.goodCellHealth <= 0:
        print("The white blood cell lost the fight... the patient died.")
        newb.goodCellHealth = 0
        newb.battleOver = True
      else:
        print("Both cells survived this turn, prepare for the next round!")
    else:
      print("The cancerous cell was defeated! The patient lives to see another day!")
      newb.battleOver = True
      newb.badCellHealth = 0
      newb.win = True
    return newb


class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
INITIAL_STATE = State()
#</INITIAL_STATE>

#<OPERATORS>
phi0 = Operator("Go into Lab",
  lambda s: s.can_move("goIntoLabResources"),
  lambda s: s.move("goIntoLabResources"))

phi1 = Operator("Go into Waiting Room",
  lambda s: s.can_move("goIntoWaitingRoom"),
  lambda s: s.move("goIntoWaitingRoom"))

phi2 = Operator("Go into Emergency Room",
  lambda s: s.can_move("goIntoEmergencyRoom"),
  lambda s: s.move("goIntoEmergencyRoom"))

phi3 = Operator("Start the Game!",
  lambda s: s.can_move("startGame"),
  lambda s: s.move("startGame"))

phi4 = Operator("Select Patient 1",
  lambda s: s.can_move("selectPatient1WaitingRoom"),
  lambda s: s.move("selectPatient1WaitingRoom"))

phi5 = Operator("Select Patient 1",
  lambda s: s.can_move("selectPatient1EmergencyRoom"),
  lambda s: s.move("selectPatient1EmergencyRoom"))

phi6 = Operator("Play Catch Mini Game",
  lambda s: s.can_move("catchMiniGame"),
  lambda s: s.move("catchMiniGame"))

phi7 = Operator("Play Maze Mini Game",
  lambda s: s.can_move("mazeMiniGame"),
  lambda s: s.move("mazeMiniGame"))

phi8 = Operator("Play memory Mini Game",
  lambda s: s.can_move("memoryMiniGame"),
  lambda s: s.move("memoryMiniGame"))

phi9 = Operator("Play luck Mini Game",
  lambda s: s.can_move("luckMiniGame"),
  lambda s: s.move("battleGame", "hinder"))

phi10 = Operator("Play battle Mini Game",
  lambda s: s.can_move("battleMiniGame"),
  lambda s: s.move("battleMiniGame"))

phi11 = Operator("Use accurate move. Hits for small damage",
  lambda s: s.can_move("inBattleMiniGame"),
  lambda s: s.move("battleGame", "accurate"))

phi12 = Operator("Use heavy move. Hits for double damage but has recoil",
  lambda s: s.can_move("inBattleMiniGame"),
  lambda s: s.move("battleGame", "heavy"))

phi13 = Operator("Use heal. Can't heal past initial health",
  lambda s: s.can_move("inBattleMiniGame"),
  lambda s: s.move("battleGame", "heal"))

phi14 = Operator("Use hinder. Weaken enemy attack by 66%",
  lambda s: s.can_move("inBattleMiniGame"),
  lambda s: s.move("battleGame", "hinder"))

phi15 = Operator("End Game",
  lambda s: s.can_move("endBattleGame"),
  lambda s: s.move("endBattleGame"))

phi16 = Operator("Move White Cell Up",
  lambda s: s.can_move("inCatchMiniGame", "Up"),
  lambda s: s.move("catchGame", "Up"))

phi17 = Operator("Move White Cell Down",
  lambda s: s.can_move("inCatchMiniGame", "Down"),
  lambda s: s.move("catchGame", "Down"))

phi18 = Operator("Move White Cell Left",
  lambda s: s.can_move("inCatchMiniGame", "Left"),
  lambda s: s.move("catchGame", "Left"))

phi19 = Operator("Move White Cell Right",
  lambda s: s.can_move("inCatchMiniGame", "Right"),
  lambda s: s.move("catchGame", "Right"))

phi20 = Operator("End Game",
  lambda s: s.can_move("endCatchGame"),
  lambda s: s.move("endCatchGame"))

phi21 = Operator("Select Patient 2",
  lambda s: s.can_move("selectPatient2WaitingRoom"),
  lambda s: s.move("selectPatient2WaitingRoom"))

phi22 = Operator("Move Right",
  lambda s: s.can_move("inMazeMiniGame", 1),
  lambda s: s.move("mazeGame", 1))

phi23 = Operator("Move Down",
  lambda s: s.can_move("inMazeMiniGame", 2),
  lambda s: s.move("mazeGame", 2))

phi24 = Operator("Move Left",
  lambda s: s.can_move("inMazeMiniGame", -1),
  lambda s: s.move("mazeGame", -1))

phi25 = Operator("Move Up",
  lambda s: s.can_move("inMazeMiniGame", -2),
  lambda s: s.move("mazeGame", -2))

phi26 = Operator("Select Patient 3",
  lambda s: s.can_move("selectPatient3WaitingRoom"),
  lambda s: s.move("selectPatient3WaitingRoom"))

phi27 = Operator("End Game",
  lambda s: s.can_move("endMazeGame"),
  lambda s: s.move("endMazeGame"))

phi28 = Operator("Go to next turn.",
  lambda s: s.can_move("nextTurn"),
  lambda s: s.move("nextTurn"))

phi29 = Operator("Buy 1 More Staff --> $10",
  lambda s: s.can_move("buyStaff"),
  lambda s: s.move("buyStaff"))

phi30 = Operator("Buy 1 Stroke Medicine --> $200",
  lambda s: s.can_move("strokeMedicine"),
  lambda s: s.move("strokeMedicine"))

phi31 = Operator("Buy 1 Cancer Medicine --> $400",
  lambda s: s.can_move("cancerMedicine"),
  lambda s: s.move("cancerMedicine"))

phi32 = Operator("Buy 1 Alzheimer's Medicine --> $400",
  lambda s: s.can_move("alzhimerMedicine"),
  lambda s: s.move("alzhimerMedicine"))

phi33 = Operator("Buy 1 Heart Medicine --> $300",
  lambda s: s.can_move("heartMedicine"),
  lambda s: s.move("heartMedicine"))

phi34 = Operator("Buy 1 Lung Disease Medicine --> $200",
  lambda s: s.can_move("lungMedicine"),
  lambda s: s.move("lungMedicine"))

phi35 = Operator("Invest in Stroke Treatment --> $600",
  lambda s: s.can_move("investStroke"),
  lambda s: s.move("investStroke"))

phi36 = Operator("Invest in Lung Disease Treatment --> $600",
  lambda s: s.can_move("investLung"),
  lambda s: s.move("investLung"))

phi37 = Operator("Invest in Cancer Treatment --> $600",
  lambda s: s.can_move("investCancer"),
  lambda s: s.move("investCancer"))

phi38 = Operator("Exit Lab Room",
  lambda s: s.can_move("exitLab"),
  lambda s: s.move("exitLab"))

phi39 = Operator("Exit Waiting Room",
  lambda s: s.can_move("exitWait"),
  lambda s: s.move("exitWait"))

phi40 = Operator("Exit Emergency Room",
  lambda s: s.can_move("exitEmergency"),
  lambda s: s.move("exitEmergency"))

phi41 = Operator("The problem is on the left",
  lambda s: s.can_move("inLuckMiniGame"),
  lambda s: s.move("luckGame", 0))

phi42 = Operator("The problem is in the middle",
  lambda s: s.can_move("inLuckMiniGame"),
  lambda s: s.move("luckGame", 1))

phi43 = Operator("The problem is on the right",
  lambda s: s.can_move("inLuckMiniGame"),
  lambda s: s.move("luckGame", 2))

phi44 = Operator("End Game",
  lambda s: s.can_move("endLuckGame"),
  lambda s: s.move("endLuckGame"))

phi45 = Operator("Select Patient 2",
  lambda s: s.can_move("selectPatient2EmergencyRoom"),
  lambda s: s.move("selectPatient2EmergencyRoom"))

phi46 = Operator("Select Patient 3",
  lambda s: s.can_move("selectPatient3EmergencyRoom"),
  lambda s: s.move("selectPatient3EmergencyRoom"))

phi47 = Operator("Go to Report Screen",
  lambda s: s.can_move("reportScreen"),
  lambda s: s.move("reportScreen"))

phi48  = Operator("End Turn",
  lambda s: s.can_move("endTurn"),
  lambda s: s.move("endTurn"))

phi49 = Operator("Basketball, Bowling, Baseball, Tennis",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 0),
  lambda s: s.move("memoryGame", "answer", 0))

phi50 = Operator("Bowling, Basketball, Tennis, Soccer",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 0),
  lambda s: s.move("memoryGame", "answer", 1))
  
phi51 = Operator("Basketball, Tennis, Bowling, Soccer, Baseball",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 0),
  lambda s: s.move("memoryGame", "answer", 2))

phi52 = Operator("Tennis, Soccer, Basketball, Bowling, Baseball",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 0),
  lambda s: s.move("memoryGame", "answer", 3))

phi53 = Operator("End Game",
  lambda s: s.can_move("endMemoryGame"),
  lambda s: s.move("endMemoryGame"))

phi54 = Operator("Go to End of Game Screen",
  lambda s: s.can_move("goToEndOfGameScreen"),
  lambda s: s.move("goToEndOfGameScreen"))

phi55 = Operator("You don't have enough money to treat more patients!",
  lambda s: s.can_move("ranOutOfMoney"),
  lambda s: s.move("goToEndOfGameScreen"))

phi56 = Operator("Go to the next image.",
  lambda s: s.can_move("inMemoryMiniGame", "progress", -1),
  lambda s: s.move("memoryGame", "progress"))

phi57 = Operator("Grape, Banana, Apple, Pineapple, Orange",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 1),
  lambda s: s.move("memoryGame", "answer", 0))

phi58 = Operator("Pineapple, Apple, Banana, Grape, Orange",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 1),
  lambda s: s.move("memoryGame", "answer", 1))
  
phi59 = Operator("Banana, Grape, Apple, Pineapple, Orange",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 1),
  lambda s: s.move("memoryGame", "answer", 2))

phi60 = Operator("Orange, Grape, Apple, Pineapple, Banana",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 1),
  lambda s: s.move("memoryGame", "answer", 3))
  
phi62 = Operator("Irwin, Carell, Tanimoto, Harvey, Jobs, Minecraft, Aoki",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 2),
  lambda s: s.move("memoryGame", "answer", 0))

phi61 = Operator("Carell, Tanimoto, Minecraft, Aoki, Irwin, Jobs, Harvey",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 2),
  lambda s: s.move("memoryGame", "answer", 1))
  
phi63 = Operator("Minecraft, Aoki, Harvey, Jobs, Tanimoto, Irwin, Carell",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 2),
  lambda s: s.move("memoryGame", "answer", 2))

phi64 = Operator("Harvey, Irwin, Jobs, Tanimoto, Carell, Minecraft, Aoki",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 2),
  lambda s: s.move("memoryGame", "answer", 3))

phi65 = Operator("Markers, Pencil, Pen, Colored pencils, Sharpie",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 3),
  lambda s: s.move("memoryGame", "answer", 0))

phi66 = Operator("Sharpie, Pen, Markers, Pencil, Colored pencils",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 3),
  lambda s: s.move("memoryGame", "answer", 1))
  
phi67 = Operator("Colored pencils, Sharpie, Pen, Marker, Pencil",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 3),
  lambda s: s.move("memoryGame", "answer", 2))

phi68 = Operator("Colored pencils, Markers, Pen, Pencil, Sharpie",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 3),
  lambda s: s.move("memoryGame", "answer", 3))
  
phi69 = Operator("Dolphin, Deer, Giraffe, Polar Bear, Rhino, Snake, Raven",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 4),
  lambda s: s.move("memoryGame", "answer", 0))

phi70 = Operator("Snake, Polar Bear, Giraffe, Deer, Dolphin, Rhino, Raven",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 4),
  lambda s: s.move("memoryGame", "answer", 1))
  
phi71 = Operator("Polar Bear, Dolphin, Deer, Giraffe, Rhino, Snake, Raven",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 4),
  lambda s: s.move("memoryGame", "answer", 2))

phi72 = Operator("Giraffe, Polar Bear, Rhino, Dolphin, Snake, Deer, Raven",
  lambda s: s.can_move("inMemoryMiniGame", "answer", 4),
  lambda s: s.move("memoryGame", "answer", 3))

phi73 = Operator("Game Tutorial",
  lambda s: s.can_move("generalTutorial"),
  lambda s: s.move("generalTutorial"))

phi74 = Operator("Exit Game Tutorial",
  lambda s: s.can_move("exitGeneralTutorial"),
  lambda s: s.move("exitGeneralTutorial"))

phi75 = Operator("View Heart Disease Info",
  lambda s: s.can_move("heartDiseaseInfo"),
  lambda s: s.move("heartDiseaseInfo"))

phi76 = Operator("View Alzheimer's Info",
  lambda s: s.can_move("alzheimersInfo"),
  lambda s: s.move("alzheimersInfo"))

phi77 = Operator("View Lung Disease Info",
  lambda s: s.can_move("lungDiseaseInfo"),
  lambda s: s.move("lungDiseaseInfo"))

phi78 = Operator("View Cancer Info",
  lambda s: s.can_move("cancerInfo"),
  lambda s: s.move("cancerInfo"))

phi79 = Operator("View Stroke Info",
  lambda s: s.can_move("strokeInfo"),
  lambda s: s.move("strokeInfo"))

phi80 = Operator("Enter Visitor Center",
  lambda s: s.can_move("enterVisitorCenter"),
  lambda s: s.move("enterVisitorCenter"))

phi81 = Operator("Return To Visitor Center",
  lambda s: s.can_move("returnToVisitorCenter"),
  lambda s: s.move("returnToVisitorCenter"))

phi82 = Operator("Exit Visitor Center",
  lambda s: s.can_move("exitVisitorCenter"),
  lambda s: s.move("exitVisitorCenter"))

OPERATORS = [phi0, phi1, phi2, phi3, phi4, phi5, phi6, phi7, phi8, phi9, phi10, phi11, phi12, phi13, phi14, phi15, phi16, phi17, phi18, phi19, phi20, phi21, phi22, phi23, phi24, phi25, phi26, phi27, phi28, phi29, phi30, phi31, phi32, phi33, phi34, phi35, phi36, phi37, phi38, phi39, phi40, phi41, phi42, phi43, phi44, phi45, phi46, phi47, phi48, phi49, phi50, phi51, phi52, phi53, phi54, phi55, phi56, phi57, phi58, phi59, phi60, phi61, phi62, phi63, phi64, phi65, phi66, phi67, phi68, phi69, phi70, phi71, phi72, phi73, phi74, phi75, phi76, phi77, phi78, phi79, phi80, phi81, phi82]
#</OPERATORS>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>

#</STATE_VIS>
