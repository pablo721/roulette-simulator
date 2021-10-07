import sys
import random
import pandas as pd
from constants import *
from PyQt6.QtWidgets import QApplication


class RouletteSimulator:
    def __init__(self):
        pass


    @staticmethod
    def get_win_chance(n_numbers):
        return n_numbers / 37

    @staticmethod
    def place_bet(numbers):
        return random.randint(0, 36) in numbers

    def play_martingale(self, start_cash, start_stake, exit_cash, numbers, multiplier_after_win=0,
                        multiplier_after_loss=2):
        cash = start_cash
        stake = start_stake
        max_stake = 0
        wins = 0
        count = 0
        return_ratio = 36 / len(numbers) - 1
        while True:
            print(f'cash: {cash}, stake: {stake}')
            if self.place_bet(numbers):
                cash += stake * return_ratio
                wins += 1
                stake = stake * multiplier_after_win if multiplier_after_win else start_stake
            else:
                cash -= stake
                stake *= multiplier_after_loss
                stake = min(cash, stake)
                max_stake = max(stake, max_stake)
            count += 1
            if cash >= exit_cash:
                return True, count, max_stake, (100 * wins / count).__round__(2)
            elif cash == 0:
                return False, count, max_stake, (100 * wins / count).__round__(2)

    def run_simulation(self, start_cash, start_stake, exit_cash, numbers, attempts, multiplier_after_win,
                       multiplier_after_loss):
        logs = pd.DataFrame(columns=['won', 'games', 'max stake', '% won'])
        winning_numbers = NUMBER_RANGES[numbers] if type(numbers) == str else [numbers]

        for i in range(attempts):
            logs.loc[i] = self.play_martingale(start_cash, start_stake, exit_cash, winning_numbers, multiplier_after_win,
                                               multiplier_after_loss)
        won = list(logs['won']).count(True)
        summary = pd.DataFrame({'won': [won], 'lost': [attempts-won], 'max games': [max(logs['games'])],
                   'max stake': [max(logs['max stake'])], 'average win %': [logs['% won'].mean().__round__(2)]})
        return summary, logs






