from datatypes import Strategy
from strats.MLRandomForest import MLRandomForest
import zmq
import time
import sys

mapping = {
    b'C': Strategy.COOPERATE,
    b'D': Strategy.DEFECT
}

class ZMQPlayer:

    def __init__(self):

        self.my_strat = MLRandomForest()
        print("Ready to roll")

        self.my_responses = []
        self.opponent_responses = []
        self.turn = 0

    def ping(self, payload):
        socket.send_multipart([b"pong"])

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
        socket.send_multipart([b"result", response])

    def reset(self, payload):
        self.turn = 0
        self.my_responses = []
        self.opponent_responses = []

        socket.send_multipart([b"reset:ok"])
        print("New Match")

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


z = ZMQPlayer()
# define the handlers
handlers = {'ping': z.ping, 'iterate': z.iterate, 'reset': z.reset}

# initialise the zmq context
context = zmq.Context()

# create a REQ socket, and set the socket identity
socket = context.socket(zmq.REQ)

# connect
socket.connect("tcp://rtchub:1441")

# register our strategy
socket.send_multipart(["reg".encode(), "github.com/hardbyte/mandela".encode()])

while True:
    message = socket.recv_multipart()
    handler = handlers[message[0].decode('utf8')]

    #print("handler for message: ", message, handler)
    handler(message[1:])