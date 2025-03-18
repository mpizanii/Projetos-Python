import threading
import time
import random

BUFFER_SIZE = 5
buffer = [None] * BUFFER_SIZE
in_pos = 0
out_pos = 0
empty_slots = threading.Semaphore(BUFFER_SIZE)
full_slots = threading.Semaphore(0)
buffer_lock = threading.Lock()
total_produced = 0
total_consumed = 0
run_time = 2


def producer(start_time):
    global in_pos, total_produced
    while time.time() - start_time < run_time:
        time.sleep(random.uniform(0.1, 0.5))
        item = random.randint(1, 100)
        empty_slots.acquire()

        with buffer_lock:
            buffer[in_pos] = item
            in_pos = (in_pos + 1) % BUFFER_SIZE
            total_produced += 1
            print(f"Inserido {item} {buffer} {in_pos} {out_pos} "
                  f"{BUFFER_SIZE - sum(x is not None for x in buffer)} {sum(x is not None for x in buffer)}")

        full_slots.release()


def consumer(start_time):
    global out_pos, total_consumed
    while time.time() - start_time < run_time:
        full_slots.acquire()

        with buffer_lock:
            item = buffer[out_pos]
            buffer[out_pos] = None
            out_pos = (out_pos + 1) % BUFFER_SIZE
            total_consumed += 1
            print(f"Removido {item} {buffer} {in_pos} {out_pos} "
                  f"{BUFFER_SIZE - sum(x is not None for x in buffer)} {sum(x is not None for x in buffer)}")

        empty_slots.release()
        time.sleep(random.uniform(0.1, 0.5))


def run_producer_consumer():
    start_time = time.time()
    threads = []

    for _ in range(3):
        t = threading.Thread(target=producer, args=(start_time,))
        t.start()
        threads.append(t)

    for _ in range(2):
        t = threading.Thread(target=consumer, args=(start_time,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Total de itens produzidos: {total_produced}")
    print(f"Total de itens consumidos: {total_consumed}")

run_producer_consumer()
