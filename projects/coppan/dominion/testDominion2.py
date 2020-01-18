# -*- coding: utf-8 -*-
"""
Created on 1-17-2020
@author: Natalie Coppa
"""

import Dominion
import random
from collections import defaultdict
import testUtility

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

# number of curses and victory cards
if len(player_names) < 2:       #TEST: changed '>' to '<' to produce wrong number of victory cards
    nV = 12
else:
    nV = 8
nC = -10 + 10 * len(player_names)

# Define box
box = testUtility.getBoxes(nV)
# Get supply order
supply_order = testUtility.getSupplyOrder()

# Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list, [(k, box[k]) for k in random10])

# The supply always has these cards
testUtility.buildSupply(supply, nV, nC, player_names)

# initialize the trash
trash = []

# Construct the Player objects
players = []
for name in player_names:
    testUtility.constructPlayers(name, players)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name, player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)