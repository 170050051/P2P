import socket
import json


port = 12345

if __name__ == "__main__":
    Peer_List = []

    seed = socket.socket()
    seed.bind(('', port))
    print(" server started")
    seed.listen(5)

    while True:
        conn, addr = seed.accept()
        req = conn.recv(10000)
        print(addr)

        if req == b'send CL':
            conn.send(json.dumps(Peer_List).encode('ASCII'))
            print("Sent Peer list to address = " + addr)

            # peer_info = conn.recv(10000)
            #
            # if peer_info != b'':
            #     peer_info = json.loads(peer_info.decode('ASCII'))
            #     Peer_List.append(peer_info)

            conn.close()

        if req == b'dead':
            dead_info = conn.recv(10000)
            dead_info = json.loads(dead_info.decode('ASCII'))
            Peer_List.remove(dead_info)

            print("Received dead info about address = " + dead_info)

            conn.close()


