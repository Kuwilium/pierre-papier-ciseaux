import random

# je demande que ce l'utilisateur veut choisir
ol = input("Allez-y...")
user_choice = ol

# points du joueur
point = 0

# nombres de tours
count = 0

# les choix possibles
paper_library = ['papier', 'Papier', 'papiers', 'Papiers']
rock_library = ['pierre', "Pierre", "pierres", "Pierres"]
scissors_library = ["ciseau", "Ciseau", "ciseaux", "Ciseaux"]

# l'ordinateur choisi
computer_choice_1 = paper_library
computer_choice_2 = rock_library
computer_choice_3 = scissors_library
computer_final_choice = random.choice([computer_choice_1, computer_choice_2, computer_choice_3])


'''
The game start and I'll create 3 conditions about the choice of the computer and then I'll introduce 
the conditions (there are 3) for each choice depending on the user_choice.
'''
while point > 3:
    if point <= 3:
        # condition one : the choice of the computer corresponding at the paper_library

        if computer_final_choice == paper_library:
            if user_choice == computer_final_choice:
                count += 1
                point = point + 0
                print("Egalité !")
                print("Vous avez", point, "points et vous en êtes au", count, "tours.")
            elif user_choice == rock_library:
                count += 1
                point -= 1
                print("Perdu !!!")
                print("Vous avez", point, "points et vous en êtes au", count, "tours.")
            else:
                count += 1
                point += 1
                print("Gagné")
                print("Vous avez", point, "points et vous en êtes au", count, "tours.")


        # condition two : the choice of the computer corresponding at the rock_library

        if computer_final_choice == rock_library:
            if user_choice == computer_final_choice:
                count += 1
                point = point + 0
                print("Egalité")
                print("Vous avez", point, "points et vous en êtes au", count, "tours.")
            elif user_choice == paper_library:
                count += 1
                point += 1
                print("Gagné")
                print("Vous avez", point, "points et vous en êtes au", count, "tours.")
            else:
                count += 1
                point -= 1
                print("Perdu")
                print("Vous avez", point, "points et vous en êtes au", count, "tours.")

        # condition three : the choice of the computer corresponding at the scissors_library

        if computer_final_choice == scissors_library:
            if user_choice == computer_final_choice:
                count += 1
                point = point + 0
                print("Egalité")
                print("Vous avez", point, "points et vous en êtes au", count, "tours.")
            elif user_choice == rock_library:
                count += 1
                point += 1
                print('Gagné')
                print("Vous avez", point, "points et vous en êtes au", count, "tours.")
            else:
                count += 1
                point -= 1
                print('Perdu')
                print("Vous avez", point, "points et vous en êtes au", count, "tours.")
    elif point > 3:
        print("Vous avez gagné")








