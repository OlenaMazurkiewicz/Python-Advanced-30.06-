# receive a message
  # print it as f"Process{getpid()} got message: {msg}"
  # sleep before responding
  # send response message back


# create 2 pipes
# create 2 processes that will use ponger, give them different sides of pipes
# they also need a specific message (either ping or pong)
# start both processes
# initiate ping-pong by sending first message to one of the pipes


from multiprocessing import Process, Pipe
from time import sleep
from os import getpid


def ponger(receiver, sender, response):
  while True:
    msg = receiver.recv()
    print(f"Process{getpid()} got message: {msg}")
    sleep(1)
    sender.send(f"{response}")


if __name__ == "__main__":

  receiver_1, sender_1 = Pipe()
  receiver_2, sender_2 = Pipe()


  process_1 = Process(target=ponger, args=(receiver_2, sender_1, 'ping')).start()
  process_2 = Process(target=ponger, args=(receiver_1, sender_2, 'pong')).start()

  sender_1.send('ping')


