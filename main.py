import random
from art import logo, vs
from game_data import data

print(logo)


# function to chose two random people
def choosing_two_random_people():
    two_random_people = random.sample(data, 2)
    first_person = two_random_people[0]
    second_person = two_random_people[1]
    return first_person, second_person


# print of the correct values for the game for the first person
def choosing_first_random_person(person):
    print(person['name'], 'a', person['description'], 'from', person['country'])


# print of the correct values for the game for the second person
def choosing_second_random_person(person):
    print(person['name'], 'a', person['description'], 'from', person['country'])

def play_again():
    """Function to check whether the player wants to play again"""
    new_game = input("Do you want to play again? Type 'y' or 'n'. "). lower()
    if new_game == 'y':
        playing_game()
    elif new_game == 'n':
        print("Goodbye")
    else:
        print("You've entered a typo. Please try again.")
        play_again()




# Main function of the game
def playing_game():
    game_over = False
    players_score = 0

    while not game_over:
        first_person, second_person = choosing_two_random_people()
        print("Compare A")
        choosing_first_random_person(first_person)
        print(vs)
        print("Compare B")
        choosing_second_random_person(second_person)
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        choosing_two_random_people()
        number_of_followers_person_a = int(first_person['follower_count'])
        number_of_followers_person_b = int(second_person['follower_count'])
        if player_choice == 'a' and number_of_followers_person_a > number_of_followers_person_b:
            players_score += 1
            print(f"You're right! Your current score is {players_score}")
        elif player_choice == 'b' and number_of_followers_person_b > number_of_followers_person_a:
            players_score += +1
            print(f"You're right! Your current score is {players_score}")
        elif player_choice != 'a' and player_choice != 'b':
                print("I think that was a typo - please chose 'a' or 'b'")
        else:
            print(f"Sorry that's wrong. Final score: {players_score}")
            game_over = True
            play_again()


playing_game()







# Dodaj możliwość gry wieloosobowej. Dwa lub więcej graczy zgaduje, kto ma więcej obserwujących, a gracz z największą liczbą prawidłowych odpowiedzi wygrywa.
# Dodaj funkcję, która śledzi i wyświetla najlepszy wynik gracza.
# Dodaj do gry element losowości. Na przykład, możesz losowo mnożyć liczbę obserwujących przez pewien czynnik, co sprawi, że gra będzie trudniejsza i mniej przewidywalna.








