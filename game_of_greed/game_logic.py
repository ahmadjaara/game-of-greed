from collections import Counter
from random import randint
from typing import Tuple

class GameLogic:
    """"Handle calculating score for dice roll"""
    @staticmethod
    def roll_dice(num):
        """this method take an integer represent the tuple length and give a tuple with 
        integer elements between 1 and 6
        input: is an integer between 1 and 6 which represent the length of the tuple
        output: tuple with random value element between 1 and 6"""
        
        roll_dice_data=[]

        for i in range(num):
            roll_dice_data+=[randint(1, 6)]

        return tuple(roll_dice_data)


    @staticmethod
    def calculate_score(dice_results):
        """A method to calculate the score for the dice , the output is an integer representing the roll’s 
        score according to rules of game.
        Input: tuple of integers that represent a dice roll."""
        
        ctr = Counter(dice_results)
        ctr = list(ctr.items())
        # print(ctr)
        score = 0
        if len(ctr) == 6 :
            score = 1500
        elif len(ctr) == 3 and ctr[0][1] == 2 and ctr[1][1] == 2 and ctr[2][1] == 2:
            score += 1500
        else: 
            for i in ctr: 
                if i[1] <= 6 and i[1] >= 3 and i[0] != 1:
                    score += i[0] * 100 * (int(i[1])-2)
                if i[1] < 3 and i[0] == 1:
                    score += 100 * i[1]
                if i[1] < 3 and i[0] == 5:
                    score += 50 * i[1]
                if i[1] <= 6 and i[1] >= 3 and i[0] == 1:
                    score += 1000 * (int(i[1])-2)
        return score


if __name__ == "__main__":
    print("The score is:",GameLogic.calculate_score(GameLogic.roll_dice(5)))
    




