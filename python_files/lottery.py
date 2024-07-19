# 2024-07-13 09:52:02
from random import choice

def generate_random_ticket(lottery):
    ticket = []
    while len(ticket) < 4:
        pull_num = choice(lottery)
        if pull_num not in ticket:
            ticket.append(pull_num)
    return ticket

def generate_winning_ticket(lottery):
    winning_ticket = []
    while len(winning_ticket) < 4:
        pull_num = choice(lottery)
        if pull_num not in winning_ticket:
            winning_ticket.append(pull_num)
    return winning_ticket

def check_ticket(my_ticket, winning_ticket):
    for index in my_ticket:
        if index not in winning_ticket:
            return False
    return True
        
for count in range(5):
    average = 0

    lottery = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e']
    winning_ticket = generate_winning_ticket(lottery)

    limit = 1_000_000
    won = False 
    total_runs = 0

    while not won:
        playing_ticket = generate_random_ticket(lottery)
        won = check_ticket(winning_ticket, playing_ticket)
        total_runs += 1
        
        if total_runs > limit:
            break
    if won:
        print("you win!")
        print(f"your ticket: {playing_ticket}")
        print(f"the winning ticket: {winning_ticket}")
        print(f"total runs: {total_runs}")
    else:
        print("you didn't have a winning ticket!")
        print(f"{playing_ticket}")

  
    