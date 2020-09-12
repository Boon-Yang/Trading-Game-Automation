import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from utils import *

suits = ['S', 'H', 'C', 'D']
n_cards_per_suit = 13

class PublicBoard:

    def __init__(self):
        self.revealedCards = []
        self.bidAsk = dict(zip(suits, [[] for _ in range(len(suits))]))
        self.bidAskInfo = pd.DataFrame(columns=['Action'] + suits)
        d = {}
        for key in ['Public Prob ' + str(suit) for suit in suits]:
            d[key] = [1.0]
        self.publicInformation = pd.DataFrame.from_dict(d, orient='columns')

    def updateProbability(self, idx):
        # update public probability
        self.publicInformation.loc[idx] = calculateProbability(self.revealedCards, n_cards_per_suit, suits)

    def revealedFromPublicDeck(self, deck):
        revealedCard = deck.pop()
        self.revealedCards.append(revealedCard)
        return revealedCard

    def updateBidAsk(self, suit, bidAskPrice, action, trade, idx):
        self.bidAsk[suit].append(bidAskPrice)
        [self.bidAsk[s].append([None, None]) for s in suits if s != suit]
        self.bidAskInfo.loc[idx] = [float(str(action) + '.' + str(trade))] + [self.bidAsk[key][idx - 1] for key in
                                                                              suits]

    def viz(self):
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))
        axes = axes.flat
        temp = self.bidAskInfo.copy()
        temp['Action'] = temp.agg({'Action': np.floor})
        for s in suits:
            temp[s + ' Mid Value'] = temp[s].apply(lambda x: 0.5 * (x[0] + x[1]) if None not in x else None)
            temp.groupby('Action')[s + ' Mid Value'].mean().interpolate().plot(label=s + ' Avg. Mid Price', ax=axes[1],
                                                                               marker='x')

        self.publicInformation.plot(ax=axes[0], marker='x')
        axes[0].set_ylim(-0.1, 1.1)
        axes[0].set_xlim(0, temp['Action'].max() + 1)
        axes[0].set_title('Perceived Information (Risk)')
        axes[0].legend()
        axes[1].set_xlim(0, temp['Action'].max())
        axes[1].set_title('Avg. Mid Price Per Action')
        axes[1].legend()

        plt.tight_layout()

