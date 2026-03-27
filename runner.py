class Runner:
    
    def __init__(self):
        self.name = "Ennis"
        self.fitness = 30 # Also the percent of people he is fitter than
        self.capacity = 100 # How much energy he has to do things, like run or work out
        self.injury_tendency = 1 # Multiplier for how likely he is to get injured, higher means more likely
        self.flake_tendency = 1 # Multiplier for how likely he is to skip a run, higher means more likely
        
        self.sprint_factor = None # TBD, higher means better at short distances, lower means better at long distances
        self.stamina = None # TBD, how much capacity he has within a run
    
    def run(self):

        self.capacity -= 30
        self.fitness *= 1.01 # Increase fitness by 1% each run
        self.fitness = min(self.fitness, 100) # Cap fitness at 100 

    def workout(self):

        self.capacity -= 10
        self.fitness *= 1.005 # Increase fitness by 0.5% each workout
        self.fitness = min(self.fitness, 100) # Cap fitness at 100

    def rest(self):

        self.capacity += 10
        self.capacity = min(self.capacity, 100) # Cap capacity at 100
        self.fitness *= 0.995 # Decrease fitness by 0.5% each rest day
        self.fitness = max(self.fitness, 0) # Floor fitness at 0