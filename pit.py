import Arena
from MCTS import MCTS


from tictactoe.TicTacToeGame import TicTacToeGame, display
from tictactoe.TicTacToePlayers import *
from tictactoe.tensorflow.NNet import NNetWrapper as NNet

from gobang.GobangGame import GobangGame, display as display1
from gobang.GobangPlayers import *
from gobang.tensorflow.NNet import NNetWrapper as NNet1


from othello.OthelloGame import OthelloGame, display as display2
from othello.OthelloPlayers import *
from othello.tensorflow.NNet import NNetWrapper as NNet2

from connect4.Connect4Game import Connect4Game, display as display3
from connect4.Connect4Players import *
from connect4.tensorflow.NNet import NNetWrapper as NNet3

import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""
choice ="othello"

if choice == "tictactoe":
    g = TicTacToeGame(5)
    n1 = NNet(g)
    n1.load_checkpoint('./temp/', 'best75_eps95_dim5.pth.tar')
    display=display
    hp = MinMaxTicTacToePlayer(g,4).play
if choice == "gobang":
    g=GobangGame(6,6)
    n1 = NNet1(g)
    n1.load_checkpoint('./temp/', 'temp:iter75:eps5:dim6.pth.tar')
    display=display1
    hp = MinMaxGobangPlayer(g,6).play
if choice == "othello":
    g=OthelloGame(6)
    n1 = NNet2(g)
    n1.load_checkpoint('./temp/', 'best75:eps140:dim6.pth.tar')
    display=display2
    hp = MinMaxOthelloPlayer(g,4).play
if choice == "connect4":
    g=Connect4Game(6,7)
    n1=NNet3(g)
    n1.load_checkpoint('./temp/','best75:eps1:dim6.pth.tar')
    display=display3
    hp=MinMaxConnect4Player(g,9).play

# all players
#rp = RandomPlayer(g).play
#gp = GreedyOthelloPlayer(g).play


# nnet players
args1 = dotdict({'numMCTSSims': 1600, 'cpuct':1.0,'epsilon': 0,'dirAlpha':0.3})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))


#n2 = NNet(g)
#n2.load_checkpoint('/dev/8x50x25/','best.pth.tar')
#args2 = dotdict({'numMCTSSims': 25, 'cpuct':1.0})
#mcts2 = MCTS(g, n2, args2)
#n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

arena = Arena.Arena(n1p, hp, g,mcts1,display=display,evaluate=True)
print(arena.playGames(2, verbose=True))
