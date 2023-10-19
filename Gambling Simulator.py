from random import *
import matplotlib.pyplot as plt

__run__ = True

def game():
    print("Welcome to the gambler's ruin simulation!\nPlease refrain from putting numbers that are too high because it will take a long time!")

    money = int(input("Input the starting money... "))

    goal = int(input("Input the goal... "))

    winChance = int(input("Input a win chance out of 100... "))

    games = int(input("Input the number of simulations to run... "))

    winChance = winChance/100

    gamesDone = 0
    timesWon = 0

    coinFlip = False
    money_over_time = []
    win_rate_over_time = []

    steps_for_game = 0

    while gamesDone < games:
        stake = money
        while stake > 0 and stake < goal:
            seed(random())
            if random() < winChance:
                stake = stake + 1
            else:
                stake = stake - 1
            steps_for_game += 1
        money_over_time.append(stake)
        if stake >= goal:
            timesWon += 1
        gamesDone+=1
        win_rate_over_time.append(timesWon / gamesDone)
        print("Game " + str(gamesDone) + " finished...")

    plt.plot(range(1, games + 1), money_over_time)
    plt.xlabel("Game Number")
    plt.ylabel("Money at end")
    plt.title("Games won and lost (Not visible at higher game values)")
    plt.show()

    plt.plot(range(1, games + 1), win_rate_over_time)
    plt.xlabel("Game Number")
    plt.ylabel("Win Rate")
    plt.title("Win Rate Over Time")
    plt.show()


    print("\nYou won %s times and lost %s times!" % (timesWon,games - timesWon))

    percentageWin = (timesWon/gamesDone)*100
    stepsPerGame = (steps_for_game/games)

    print("Your game had a percentage winrate of %s!\n" % percentageWin)
    print("Each game took an average of %s steps to finish!\n" % stepsPerGame)
    retry()

def retry():
    print("Would you like to run more simulations?\nType Y to continue, type anything else to exit...")
    retryChoice = input()
    if retryChoice.lower() == "y":
        print("\n")
        game()
    else:
        exit()

if __run__ == True:
    game()
