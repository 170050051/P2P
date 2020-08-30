import csv
import socket
import json

port = 12345

if __name__ == "__main__":
    # file = open('config.csv', mode='r')
    # csv_reader = csv.DictReader(file)
    # line_count = 0
    #
    # seed_list = []
    #
    # for row in csv_reader:
    #     if line_count == 0:
    #         line_count = 1
    #     else:
    #         seed_list.append(row)

    peer = socket.socket()

    peer.connect(('127.0.0.1', port))

    peer.send(b'send CL')

    peer_list = peer.recv(10000)
    peer_list = json.loads(peer_list.decode('ASCII'))

    print(peer_list)
    peer.close()