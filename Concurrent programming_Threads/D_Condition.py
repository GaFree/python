import time
import threading


def consumer(cond):
    t = threading.current_thread()
    with cond:
        cond.wait()  # 创建了一个锁，等待producer解锁
        print('{}: Resource is available to consumer'.format(t.name))


def producer(cond):
    t = threading.current_thread()
    with cond:
        print('{}:Making resource available'.format(t.name))
        cond.notifyAll()  # 释放锁,唤醒消费者


condition = threading.Condition()

c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))

c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p.start()
