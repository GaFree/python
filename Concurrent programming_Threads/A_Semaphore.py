import time
from random import random
from threading import Thread, Semaphore, current_thread, enumerate

sema = Semaphore(3)


def foo(tid):
    with sema:
        print('{} acquire sema'.format(tid))
        wt = random() * 2

        time.sleep(wt)
    print('{} release sema'.format(tid))


for i in range(5):
    t = Thread(target=foo, args=(i,))
    t.start()

main_thread = current_thread()
for t in enumerate():
    if t is main_thread:
        continue
    t.join()
