import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import random

def shuffle(deck):
    shuffled_deck = []
    for i in range(len(deck)):
        idx = np.random.randint(0, len(deck))
        shuffled_deck.append(deck.pop(idx))
    return shuffled_deck


def generate_cards(n_cards, suits):
    deck = []
    for suit in suits:
        cards = [suit + ' '+ str(num) for num in np.linspace(1, n_cards, n_cards).astype('int')]
        deck.extend(cards)
    return deck


def distribute(deck, n_cards):
    private_information = []
    for idx in range(n_cards):
        private_information.append(deck.pop(np.random.randint(0, len(deck))))
    return private_information

def mergePrivateAndPublic(privateCards, revealedCards):
    temp = privateCards.copy()
    temp.extend(revealedCards)
    return temp


def calculateProbability(cardsExcluded, n_cards_per_suit, suits):
    d = {}
    for s in suits:
        d[s] = n_cards_per_suit

    for c in cardsExcluded:
        suit, _ = c.split(' ')
        d[suit] -= 1
    # convert to prob
    return [round(d[key] / n_cards_per_suit, 3) for key in suits]


def executeTrade(seller, buyer, bidAskPrice, contract, numContracts, idx, action, trade):
    seller.sell(buyer, bidAskPrice, contract, numContracts, idx, action, trade)
    buyer.buy(seller, bidAskPrice, contract, numContracts, idx, action, trade)
