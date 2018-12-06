from picar import front_wheels
from picar import back_wheels
from picar import ADC
import time
import picar

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
adc = ADC()


fw.turn(70)
bw.foward()
