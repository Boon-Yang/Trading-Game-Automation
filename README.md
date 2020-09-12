# Trading-Game-Automation
Automating the Finance and Financial Management Coursework (Trading Game)

The game can be played with 4(optimal) or 5 players

# General rules
0. Shuffle the poker cards(remove joker).
1. Each player will receive a number of private cards (ideally four cards). Only the player themselves will have access to these "private information".
2. Place the deck with remaining cards facing downwards and revealing one card from the deck at each action. This simulates the influx of "public information".
3. Players may wish to buy or sell their inventory(suits) and they can only sell or buy a particular suit with the suit market maker.
4. Buying means deducting from cashflow and increasing in inventory vice versa for selling.
5. The last card results in 100 points x position of last card's suit for all the players. Meaning, if the last card is a 'C', and you hold -2 of it, you will have -200 added to ur current cashflow. Holding all other suits will, regardless of how much, will not give additional loss/profit once the last card has been revealed. 
6. Occassionally, all players will reveal one card from their private deck. As of which action, this is decided by the players themselves. All cards must be revealed by the end of the game, before the last reveal from the public deck.

In other words, you are betting to hold positive and a very big position for the last card's suit. Players may predict the last card's suit based on the influx of market information/ publlic information.

# Market Maker (mm)
* Market Makker are responnsible to set bid and ask price when a counterparty approach to trade. Once these pricings have been set, the mm must trade if the counterparty agrees with the pricings. In other words, though mm have the power to set price, they cannot deny anyone who approach to trade with them.
* Players can only trade particular suits with the corresponding suit market maker.

# Speculator
* Speculator holds the least amount of private information and have no say in setting prices.


I intend to develop this work as a tool for people who are interested in testing out their trading strategies against other baselines. In the future, I might continue with this and make an app out of it.
