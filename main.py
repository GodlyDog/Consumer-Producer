import signal
import threading
from random import randint, sample
from typing import List

global run


class ConsumerQueue(object):
    def __init__(self, consumer_list: List):
        self.lock = threading.Lock()
        self.list = consumer_list


def run_producer_thread(queue1: ConsumerQueue, queue2: ConsumerQueue, queue3: ConsumerQueue):
    while run:
        l1_s = len(queue1.list)
        l2_s = len(queue2.list)
        l3_s = len(queue3.list)
        min_size = min(len(queue1.list), len(queue2.list), len(queue3.list))
        potentials = []
        if l1_s == min_size:
            potentials.append(1)
        if l2_s == min_size:
            potentials.append(2)
        if l3_s == min_size:
            potentials.append(3)
        if len(potentials) == 1:
            picker = potentials[0]
        else:
            picker = sample(potentials, 1)[0]
        randomNumber = randint(1, 30)
        if picker == 1:
            with queue1.lock:
                queue1.list.append(randomNumber)
                print_list(queue1, True, 1)
        if picker == 2:
            with queue2.lock:
                queue2.list.append(randomNumber)
                print_list(queue2, True, 2)
        if picker == 3:
            with queue3.lock:
                queue3.list.append(randomNumber)
                print_list(queue3, True, 3)


def run_consumer_thread(q: ConsumerQueue, list_number):
    while run:
        if len(q.list) != 0:
            with q.lock:
                q.list.pop()
                print_list(q, False, list_number)


def print_list(queue: ConsumerQueue, adding: bool, list_number: int):
    if adding:
        list_string = ""
        for elem in queue.list:
            list_string = list_string + str(elem) + ", "
        list_string = list_string[:-2]
        print("Added to list " + str(list_number) + ": " + list_string + "\n")
    else:
        list_string = ""
        for elem in queue.list:
            list_string = list_string + str(elem) + ", "
        list_string = list_string[:-2]
        print("Removed from list " + str(list_number) + ": " + list_string + "\n")


def signal_handler(sig, frame):
    print("\nStopping gracefully...\n")
    global run
    run = False


if __name__ == '__main__':
    run = True
    print("Initializing lists...")
    # initialize lists
    signal.signal(signal.SIGINT, signal_handler)
    l1 = [i + 1 for i in range(randint(10, 20))]
    l2 = [i + 1 for i in range(randint(10, 20))]
    l3 = [i + 1 for i in range(randint(10, 20))]
    q1 = ConsumerQueue(l1)
    q2 = ConsumerQueue(l2)
    q3 = ConsumerQueue(l3)
    # create producer thread
    print("Initializing producer thread...")
    producer = threading.Thread(target=run_producer_thread, args=(q1, q2, q3))
    print("Starting producer thread...")
    producer.start()
    print("Initializing consumer threads...")
    consumer1 = threading.Thread(target=run_consumer_thread, args=(q1, 1))
    consumer2 = threading.Thread(target=run_consumer_thread, args=(q2, 2))
    consumer3 = threading.Thread(target=run_consumer_thread, args=(q3, 3))
    print("Starting consumer threads...")
    consumer1.start()
    consumer2.start()
    consumer3.start()
    producer.join()
    consumer1.join()
    consumer2.join()
    consumer3.join()
