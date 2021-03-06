from datatypes import Strategy
import strats
import multiprocessing
from strats.MLRandomForest import MLRandomForest
import zmq
import time
import sys

mapping = {
    b'C': Strategy.COOPERATE,
    b'D': Strategy.DEFECT
}

class ZMQPlayer:

    def __init__(self, strat):

        self.my_strat = strat
        print(strat)
        print("Ready to roll - ")

        self.my_responses = []
        self.opponent_responses = []
        self.turn = 0

    def run(self):
        print("Running new thread")

        # define the handlers
        handlers = {'ping': self.ping, 'iterate': self.iterate, 'reset': self.reset}

        # initialise the zmq context
        context = zmq.Context()

        # create a REQ socket, and set the socket identity
        self.socket = context.socket(zmq.REQ)

        # connect
        self.socket.connect("tcp://rtchub:1441")

        # register our strategy
        self.socket.send_multipart(["reg".encode(), "mandela:{}".format(str(self.my_strat)).encode()])


        while True:
            message = self.socket.recv_multipart()
            handler = handlers[message[0].decode('utf8')]

            #print("handler for message: ", message, handler)
            handler(message[1:])

    def ping(self, payload):
        self.socket.send_multipart([b"pong"])

    def iterate(self, payload):
        if (payload[0] != b""):
            self.opponent_responses.append(
                mapping[payload[0]]
            )

        # run the strategy
        response = self.run_strategy()

        # add the new response to my responses array
        self.my_responses.append(mapping[response])

        # send back the response to the server
        self.socket.send_multipart([b"result", response])

    def reset(self, payload):
        self.turn = 0
        self.my_responses = []
        self.opponent_responses = []

        self.socket.send_multipart([b"reset:ok"])
        print("New Match for {}".format(str(self.my_strat)))

    def run_strategy(self):

        move = self.my_strat.determine_action(
            self.my_responses,
            self.opponent_responses,
            self.turn
        )
        self.turn += 1
        if move == Strategy.DEFECT:
            return b'D'
        else:
            return b'C'



possible_strats = [
    strats.NaivePeaceMaker(1.0),
    strats.NaivePeaceMaker(1.0),
    strats.RemorsefulProber(0.05),
    strats.MLRandomForest(),
    strats.TitForTatsRand(0.0)
]


if __name__ == "__main__":
    threads = []
    for strat in possible_strats:
        z = ZMQPlayer(strat)

        t = multiprocessing.Process(target=z.run)
        threads.append(t)
        t.start()


