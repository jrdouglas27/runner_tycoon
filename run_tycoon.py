import numpy as np
import pandas as pd
import random as rd

def day_of_week(day_num):
    
    weekday_num = day_num % 7
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[weekday_num]

class Runner:
    def __init__(self):
        self.name = "Ennis"
        self.fitness = 30 # Also the percent of people he is fitter than
        self.capacity = 100 # How much energy he has to do things, like run or work out
        self.injury_tendency = 1 # Multiplier for how likely he is to get injured, higher means more likely
        self.flake_tendency = 1 # Multiplier for how likely he is to skip a run, higher means more likely
        
        self.sprint_factor = None # TBD, higher means better at short distances, lower means better at long distances
        self.stamina = None # TBD, how much capacity he has within a run

Ennis = Runner()

days_to_sim = 100
for day_num in range(days_to_sim):
    
    print(f"\nDay {day_num+1} ({day_of_week(day_num)})")
    print(f"Your fitness level is: {Ennis.fitness}")
    print(f"Your current capacity is: {Ennis.capacity}")

    action = input("\nWhat do you want to do today?\n     (1) Run (-30 capacity)\n     (2) Work out (-10 capacity)\n     (3) Rest (+10 capacity)\nType the number of your choice: ")

    if action == "1":
        if Ennis.capacity < 30:
            print("You don't have enough capacity to run today. Consider working out or resting instead.")
        else:
            Ennis.capacity -= 30
            Ennis.fitness *= 1.01 # Increase fitness by 1% each run
            Ennis.fitness = min(Ennis.fitness, 100) # Cap fitness at 100 
            print("You went for a run! Your capacity has decreased by 30. Your fitness has increased.")

    elif action == "2":
        if Ennis.capacity < 10:
            print("You don't have enough capacity to work out today. Consider running or resting instead.")
        else:
            Ennis.capacity -= 10
            Ennis.fitness *= 1.005 # Increase fitness by 0.5% each workout
            Ennis.fitness = min(Ennis.fitness, 100) # Cap fitness at 100
            print("You worked out! Your capacity has decreased by 10.")
    
    elif action == "3":
        Ennis.capacity += 10
        Ennis.capacity = min(Ennis.capacity, 100) # Cap capacity at 100
        Ennis.fitness *= 0.995 # Decrease fitness by 0.5% each rest day
        Ennis.fitness = max(Ennis.fitness, 0) # Floor fitness at 0
        print("You rested! Your capacity has increased by 10.")
    
