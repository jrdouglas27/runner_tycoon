import numpy as np
import pandas as pd
import random as rd
from utils import print_initial_day_msgs, race_suggestion
from runner import Runner
from config import days_to_sim

Ennis = Runner()

game_state = True
day_num = 0

while game_state and day_num < days_to_sim:
    
    print_initial_day_msgs(day_num=day_num, player=Ennis)

    if rd.random() < event_prob and not Ennis.has_race_planned:
        race_suggestion(player)

    do_day_action(player)

    day_num += 1