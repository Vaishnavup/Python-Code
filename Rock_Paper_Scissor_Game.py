import random

player_point = 0
system_point = 0

while (True):
    player_choice = int(input('Enter 1 for Rock 2 for paper and 3 for seissors : '))
    system_choice = random.randint(1,3)

    if player_choice == system_choice:
        print('Its a tie, No point')

    elif player_choice == 1:
        if system_choice == 2:
            print('System choice paper and won this round')
            system_point += 1
            print('System Point : ' + str(system_point))
            print('Your Point : ' + str(player_point))

        if system_choice == 3:
            print('System choice Scissor. You won this round')
            player_point += 1
            print('System Point : ' + str(system_point))
            print('Your Point : ' + str(player_point)) 



    elif player_choice == 2:
        if system_choice == 1:
            print('System choice Rock. You won this round')
            player_point += 1
            print('System Point : ' + str(system_point))
            print('Your Point : ' + str(player_point))
            
        if system_choice == 3:
            print('System choice Scissor and won this round')
            system_point += 1
            print('System Point : ' + str(system_point))
            print('Your Point : ' + str(player_point)) 

    else:
        if system_choice == 1:
            print('System choice Rock and won this round')
            system_point += 1
            print('System Point : ' + str(system_point))
            print('Your Point : ' + str(player_point))
            
        if system_choice == 2:
            print('System choice Paper. You won this round')
            player_point += 1
            print('System Point : ' + str(system_point))
            print('Your Point : ' + str(player_point))
    
    if player_point == 2:
        print('You won. Best of three')
        break

    if system_point == 2:
        print('System won, But you lost')
        break
        

      