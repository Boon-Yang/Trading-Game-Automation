import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# player includes market makers and speculator
class Player:
    suits = ['S', 'H', 'C', 'D']
    n_cards_per_suit = 13

    def __init__(self, privateCards, name):
        self.name = name
        self.privateCards = privateCards

        self.ledger = pd.DataFrame(columns=['Action', 'CounterParty', 'Contract', 'Price', 'Quantity', 'Buy/Sell'] + \
                                           suits + ['Cash'])
        self.inventories = {'S': 0, 'H': 0, 'C': 0, 'D': 0}
        self.cash = 0

        d = {}
        for key in ['Private Prob ' + str(suit) for suit in suits]:
            d[key] = [1.0]
        self.privateInformation = pd.DataFrame.from_dict(d, orient='columns')

    def updateProbability(self, idx, revealedCards):
        # update private probability
        self.privateInformation.loc[idx] = calculateProbability( \
            mergePrivateAndPublic(self.privateCards, revealedCards), n_cards_per_suit, suits)

    def revealPrivateCard(self, cardToBeRevealed):
        if cardToBeRevealed in self.privateCards:
            idx = self.privateCards.index(cardToBeRevealed)
            cardRevealed = self.privateCards.pop(idx)
            return cardRevealed
        raise Exception("Card not in private deck.")

    #     bid is higher than ask, [bid, ask]
    def buy(self, counterParty, bidAskPrice, contract, numContracts, idx, action, trade):
        self.inventories[contract] += numContracts
        tradeNum = float(str(action) + '.' + str(trade))
        if contract == self.name:
            self.cash -= numContracts * bidAskPrice[1]
            entry = [tradeNum, counterParty.name, contract, -1 * bidAskPrice[1], numContracts, 'Buy'] + \
                    [self.inventories[key] for key in suits] + \
                    [self.cash]
        else:
            self.cash -= numContracts * bidAskPrice[0]
            entry = [tradeNum, counterParty.name, contract, -1 * bidAskPrice[0], numContracts, 'Buy'] + \
                    [self.inventories[key] for key in suits] + \
                    [self.cash]
        # update ledger
        self.ledger.loc[idx] = entry

    def sell(self, counterParty, bidAskPrice, contract, numContracts, idx, action, trade):
        self.inventories[contract] -= numContracts
        tradeNum = float(str(action) + '.' + str(trade))
        if contract == self.name:
            self.cash += numContracts * bidAskPrice[0]
            entry = [tradeNum, counterParty.name, contract, bidAskPrice[0], numContracts, 'Sell'] + \
                    [self.inventories[key] for key in suits] + \
                    [self.cash]
        else:
            self.cash += numContracts * bidAskPrice[1]
            entry = [tradeNum, counterParty.name, contract, bidAskPrice[1], numContracts, 'Sell'] + \
                    [self.inventories[key] for key in suits] + \
                    [self.cash]
        # update ledger
        self.ledger.loc[idx] = entry

