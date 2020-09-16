# Trading-Game-Automation
This piece of work aims to automate the trading game coursework in the Finance and Financial Management module. The rules are listed as follow, with some simplifications.

The game can be played with 4(optimal) or 5 players. The objective for all players is to optimise respective portfolio such that the most positive inventory (suit) ends up as the last public card and gives a payoff of 100 (dollars or any other currency) per unit hold. However, a deduction of 100 dollars per unit hold will be incurred from all players' cashflow if they position for the last suit revealed is negative. Players with highest and positive cashflow after revealing the final public card wins. 

See the rules below for more details.

# General rules
0. Shuffle the poker cards(remove joker).
1. Each player will receive a number of private cards (ideally four cards). Only the player themselves will have access to these "private information".
2. Place the deck with remaining cards facing downwards and revealing one card from the deck at each action. This simulates the influx of "public information".
3. Players may wish to buy or sell their inventory(suits) and they can only sell or buy a particular suit from the suit market maker. Note, the quantity of suits hold per action will be registered into individual ledger.
4. Buying means deducting from cashflow and increasing in inventory vice versa for selling. Both inventories and cashflow can be negative.
5. The last card results in 100 points x position of last card's suit for all the players. Meaning, if the last card is a 'C', and you hold -2 of it, you will have -200 added to your current cashflow. Holding all other suits will, regardless of how much, will not give additional loss/profit once the last public card has been revealed. 
6. Occassionally, all players will reveal one card from their private deck. As of which action, this is decided by the players themselves. All cards must be revealed by the end of the game, before the last reveal from the public deck.

In other words, you are betting to hold a very big and positive position for the last card's suit. Players may predict the last card's suit based on the influx of market information/ public information. Players may wish to limit the bid ask spread prior to starting the game.

# Market Maker (mm)
* Market Makker are responsible to set bid and ask price when a counterparty approach to trade. Once these pricings have been set, the mm must trade if the counterparty agrees with the pricings. In other words, though mm have the power to set price, they cannot deny anyone who approach to trade with them.
* Players can only trade particular suits with the corresponding suit market maker.

# Speculator
* Speculator holds the least amount of private information and have no say in setting prices.


I intend to develop this work as a tool for people who are interested in testing out their trading strategies against other baselines. In the future, I might continue with this and make an app out of it.
