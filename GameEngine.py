# CLI Rock - Paper - Scissors Game 

import random
print("	    Instructions       ")
print("    How To Play        ")
print("User have to enter their moves in console")
print("For example : Your Moves : 'Paper' ")
print("The Game Engine will randomly choose a move")
print("The Game will start in countdown of 3")


print("Enter 'START' in console to start the game")
user_input = input("")
game = False
if user_input == 'START':
   game = True


game_moves = ['Rock', 'Paper', 'Scissor']
while game:
     print(f"Enter your move from {game_moves}")
     user_move = input("")
     print("Let's see what computer have selected")
     print("Game is starting: 3")
     print("2")
     print("1")
     cpu_move = random.choice(game_moves)
     if user_move == 'Rock' and cpu_move == 'Rock':
        print("Tie")
     elif user_move == 'Rock' and cpu_move == 'Paper':
        print("Loose, Computer win")
     elif user_move == 'Rock' and cpu_move == 'Scissor':
        print("You Win!")
     elif user_move == 'Paper' and cpu_move == 'Paper':
        print("Tie")
     elif user_move == 'Paper' and cpu_move == 'Scissor':
        print("Loose, Computer win")
     elif user_move == 'Paper' and cpu_move == 'Rock':
        print("You Win!")
     elif user_move == 'Scissor' and cpu_move == 'Scissor':
        print("Tie")
     elif user_move == 'Scissor' and cpu_move == 'Rock':
        print("Loose, Computer win")
     elif user_move == 'Scissor' and cpu_move == 'Paper':
        print("You Win!")
     user_input = input("Wanna play AGAIN?(Y/N): ")
     if user_input == 'N':
        print("Thank You for Playing!")
        break

        
     
