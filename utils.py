# Utils

def day_of_week(day_num):
    
    weekday_num = day_num % 7
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[weekday_num]

def print_initial_day_msgs(day_num, player):

    print(f"\nDay {day_num+1} ({day_of_week(day_num)})")
    print(f"Your fitness level is: {round(player.fitness,0)}")
    print(f"Your current capacity is: {round(player.capacity,0)}")

def do_day_action(player):
    action_solved = False
    while not action_solved:
        
        action = input("\nWhat do you want to do today?\n     (1) Run (-30 capacity)\n     (2) Work out (-10 capacity)\n     (3) Rest (+20 capacity)\nType the number of your choice: ")

        if action == "1":
            if player.capacity < 30:
                print("You don't have enough capacity to run today. Consider working out or resting instead.")
            else:
                player.run()
                print("You went for a run! Your capacity has decreased by 30. Your fitness has increased.")
                action_solved = True

        elif action == "2":
            if player.capacity < 10:
                print("You don't have enough capacity to work out today. Consider running or resting instead.")
            else:
                player.workout()
                print("You worked out! Your capacity has decreased by 10.")
                action_solved = True
        
        elif action == "3":
            player.rest()
            print("You rested! Your capacity has increased by 20.")
            action_solved = True

    def race_suggestion(player):

        days_till_event = rd.randint(7,100)
            answer = input(f"There is a race taking place in {days_till_event} days time. Would you like to participate? (Y/N)")

            if answer == "Y":
                player.has_race_planned = True
                player.days_till_next_race = days_till_event
                print("Great. Race has been added to calendar.")
            
            if answer == "N":
                print("You have rejected to participate in this race.")