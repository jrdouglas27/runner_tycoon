import numpy as np
import pandas as pd
import random as rd
from utils import day_of_week
from runner import Runner
from config import days_to_sim

Ennis = Runner()

for day_num in range(days_to_sim):
    
    print(f"\nDay {day_num+1} ({day_of_week(day_num)})")
    print(f"Your fitness level is: {Ennis.fitness}")
    print(f"Your current capacity is: {Ennis.capacity}")

    action = input("\nWhat do you want to do today?\n     (1) Run (-30 capacity)\n     (2) Work out (-10 capacity)\n     (3) Rest (+10 capacity)\nType the number of your choice: ")

    if action == "1":
        if Ennis.capacity < 30:
            print("You don't have enough capacity to run today. Consider working out or resting instead.")
        else:
            Ennis.run()
            print("You went for a run! Your capacity has decreased by 30. Your fitness has increased.")

    elif action == "2":
        if Ennis.capacity < 10:
            print("You don't have enough capacity to work out today. Consider running or resting instead.")
        else:
            Ennis.workout()
            print("You worked out! Your capacity has decreased by 10.")
    
    elif action == "3":
        Ennis.rest()
        print("You rested! Your capacity has increased by 10.")
    
