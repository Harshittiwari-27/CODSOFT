#                            ROCK - PAPER - SCISSOR  GAME  :-

import random

battle_moves = ['rock', 'paper', 'scissor']

# Get player choice
player_move = input("Enter your move (rock, paper, or scissor): ").lower()
ai_move = random.choice(battle_moves)

print(f"\nYou choice: {player_move}")
print(f"Opponent choice: {ai_move}")
#                                Game decision logic :-
if player_move == ai_move:
    print("It's a draw!")
elif (player_move == 'rock' and ai_move == 'scissor') or \
     (player_move == 'paper' and ai_move == 'rock') or \
     (player_move == 'scissor' and ai_move == 'paper'):
    print("You won this round!")
else:
    print("You lost this round!")
