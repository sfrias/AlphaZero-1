from Coach import Coach

from tictactoe.TicTacToeGame import TicTacToeGame as Game
from tictactoe.tensorflow.NNet import NNetWrapper as nn

from othello.OthelloGame import OthelloGame as Game1
from othello.tensorflow.NNet import NNetWrapper as nn1

from gobang.GobangGame import GobangGame as Game2
from gobang.tensorflow.NNet import NNetWrapper as nn2

from connect4.Connect4Game import Connect4Game as Game3
from connect4.tensorflow.NNet import NNetWrapper as nn3



from utils import *


args = dotdict({
    'numIters': 75,
    'numEps': 50,
    'tempThreshold': 15,
    'updateThreshold': 0.6,
    'maxlenOfQueue': 2000,
    'numMCTSSims': 25,
    'arenaCompare': 40,
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': False,
    'load_folder_file': ('/dev/models/8x100x50','best.pth.tar'),
    'numItersForTrainExamplesHistory': 50,

})

if __name__=="__main__":

    choice="tictactoe"

    if choice=="tictactoe":
        g = Game(3)
        nnet = nn(g)
        args.update({'trainExampleCheckpoint': './temp/tictactoe/'})
    if choice=="othello":
        g = Game1(6)
        nnet = nn1(g)
        args.update({'trainExampleCheckpoint': './temp/othello/'})
    if choice=="gobang":
        g=Game2(14,14)
        nnet = nn2(g)
        args.update({'trainExampleCheckpoint': './temp/gobang/'})
    if choice=="connect4":
        g=Game3(6,6)
        nnet=nn3(g)
        args.update({'trainExampleCheckpoint': './temp/connect4/'})

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()