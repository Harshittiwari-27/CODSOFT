#                            ROCK - PAPER - SCISSOR  GAME  :-

import random

#                                Game options :-
battle_moves = ['rock', 'paper', 'scissor']

#                                Score Tracking :-
user_score = 0
computer_score = 0

while True:
    #                            Get player choice :-
    player_move = input("Enter your move (rock, paper, or scissor): ").lower()
    ai_move = random.choice(battle_moves)

    print(f"\nYou choice: {player_move}")
    print(f"Opponent choice: {ai_move}")

    #                            Game decision logic :-
    if player_move == ai_move:
        print("It's a draw!")
    elif (player_move == 'rock' and ai_move == 'scissor') or \
         (player_move == 'paper' and ai_move == 'rock') or \
         (player_move == 'scissor' and ai_move == 'paper'):
        print("You won this round!")
        user_score += 1
    else:
        print("You lost this round!")
        computer_score += 1

    #                            Display Score :-
    print(f"Score -> You: {user_score} | Opponent: {computer_score}")

    #                            Play Again Option :-
    play_more = input("Do you want to play again? (yes/no): ").lower()
    if play_more != 'yes':
        print("Thank you for playing !")
        break
