import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from utils import *

# player includes market makers and speculator
class Player:

    def __init__(self, privateCards, name, suits=['S', 'H', 'C', 'D'], n_cards_per_suit=13):
        self.name = name
        self.privateCards = privateCards

        self.suits = suits
        self.n_cards_per_suit = n_cards_per_suit

        self.ledger = pd.DataFrame(columns=['Action', 'CounterParty', 'Contract', 'Price', 'Quantity', 'Buy/Sell'] + \
                                           self.suits + ['Cash'])
        self.inventories = {'S': 0, 'H': 0, 'C': 0, 'D': 0}
        self.cash = 0

        d = {}
        for key in ['Private Prob ' + str(suit) for suit in suits]:
            d[key] = [1.0]
        self.privateInformation = pd.DataFrame.from_dict(d, orient='columns')

    def updateProbability(self, idx, revealedCards):
        # update private probability
        self.privateInformation.loc[idx] = calculateProbability( \
            mergePrivateAndPublic(self.privateCards, revealedCards), self.n_cards_per_suit, self.suits)

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
                    [self.inventories[key] for key in self.suits] + \
                    [self.cash]
        else:
            self.cash -= numContracts * bidAskPrice[0]
            entry = [tradeNum, counterParty.name, contract, -1 * bidAskPrice[0], numContracts, 'Buy'] + \
                    [self.inventories[key] for key in self.suits] + \
                    [self.cash]
        # update ledger
        self.ledger.loc[idx] = entry

    def sell(self, counterParty, bidAskPrice, contract, numContracts, idx, action, trade):
        self.inventories[contract] -= numContracts
        tradeNum = float(str(action) + '.' + str(trade))
        if contract == self.name:
            self.cash += numContracts * bidAskPrice[0]
            entry = [tradeNum, counterParty.name, contract, bidAskPrice[0], numContracts, 'Sell'] + \
                    [self.inventories[key] for key in self.suits] + \
                    [self.cash]
        else:
            self.cash += numContracts * bidAskPrice[1]
            entry = [tradeNum, counterParty.name, contract, bidAskPrice[1], numContracts, 'Sell'] + \
                    [self.inventories[key] for key in self.suits] + \
                    [self.cash]
        # update ledger
        self.ledger.loc[idx] = entry

    def viz(self):
        self.privateInformation.plot(marker='x', figsize=(20, 10))



class MarketMaker(Player):
    def __init__(self, privateCards, name, suits, n_cards_per_suit):
        super().__init__(privateCards, name, suits, n_cards_per_suit)

    def arbitrageAlert(self, counterPartyName, bidAskPrice):

        temp = self.ledger.query('CounterParty == "{}"'.format(counterPartyName))[['Price', 'Buy/Sell']]

        historicalAsks = temp['Price'][temp['Buy/Sell'] == 'Buy'].abs()
        historicalBids = temp['Price'][temp['Buy/Sell'] == 'Sell'].abs()

        # initiate conditions either one is True then arbitrage opportunity
        cond1 = False
        cond2 = False
        if len(historicalBids) > 0 and bidAskPrice[1] > historicalBids.values.min():
            cond2 = True
            print('Ask Price too high. Suggested Ask price {}'.format(historicalBids.values.min() - 1))
        if len(historicalAsks) > 0 and bidAskPrice[0] < historicalAsks.values.max():
            cond1 = True
            print('Bid Price too low. Suggested Bid price {}'.format(historicalAsks.values.max() + 1))

        return cond1 and cond2
