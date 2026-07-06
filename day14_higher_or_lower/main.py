import art
from game_data import data
import random
print(art.logo)


score = 0
def game():
    global score
    option1 = data[random.randint(0, len(data) - 1)]
    option2 = data[random.randint(0, len(data) - 1)]
    option3 = data[random.randint(0, len(data) - 1)]
    if option1 != option2:
        print("Compare A: " + option1['name'] + ', ' + option1['description'] + ', ' + "from " +option1['country'])
        print(art.vs)
        # print("Against B: " + data[random.randint(0, len(data)-1)])
        print("Against B: " + option2['name'] + ', ' + option2['description'] + ', ' + "from " + option2['country'])
        answer = input("Who has more followers 'A' or 'B': ").lower()
        if answer == 'a':
            if option1['follower_count'] > option2['follower_count']:
                score += 1
                print(f"You're right! Score: {score}")
                print("Compare A: " + option2['name'] + ', ' + option2['description'] + ', ' + "from " + option2[
                    'country'])
                print(art.vs)
                # print("Against B: " + data[random.randint(0, len(data)-1)])
                print("Against B: " + option3['name'] + ', ' + option3['description'] + ', ' + "from " + option3[
                    'country'])
                answer = input("Who has more followers 'A' or 'B': ").lower()
                if answer == 'a':
                    if option2['follower_count'] > option3['follower_count']:
                        score += 1
                        print(f"You're right! Score: {score}")
                        game()
                    else:
                        print(f"HAHA YOU LOSE! {score}")
                if answer == 'b':
                    if option3['follower_count'] > option2['follower_count']:
                        score += 1
                        print(f"You're right! Score: {score}")
                        game()
                    else:
                        print(f"HAHA YOU LOSE! {score}")
            else:
                print(f"HAHA YOU LOSE! {score}")
        elif answer == 'b':
            if option2['follower_count'] > option1['follower_count']:
                score += 1
                print(f"You're right! Score: {score}")
                print("Compare A: " + option2['name'] + ', ' + option2['description'] + ', ' + "from " + option2[
                    'country'])
                print(art.vs)
                # print("Against B: " + data[random.randint(0, len(data)-1)])
                print("Against B: " + option3['name'] + ', ' + option3['description'] + ', ' + "from " + option3[
                    'country'])
                answer = input("Who has more followers 'A' or 'B': ").lower()
                if answer == 'a':
                    if option2['follower_count'] > option3['follower_count']:
                        score += 1
                        print(f"You're right! Score: {score}")
                        game()
                    else:
                        print(f"HAHA YOU LOSE! {score}")
                if answer == 'b':
                    if option3['follower_count'] > option2['follower_count']:
                        score += 1
                        print(f"You're right! Score: {score}")
                        game()
                    else:
                        print(f"HAHA YOU LOSE! {score}")

            else:
                print(f"HAHA YOU LOSE! {score}")




# print(option1)
game()
