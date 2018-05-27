import threading
import time

mutex = threading.RLock()


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):
        mutex.acquire()  # 如果锁被占用,则阻塞在这里,等待锁的释放

        print("I am %s , get res: %s---%s" % (self.name, "ResA", time.time()))

        mutex.acquire()
        print("I am %s , get res: %s---%s" % (self.name, "ResB", time.time()))
        mutex.release()
        mutex.release()

    def fun2(self):
        mutex.acquire()
        print("I am %s , get res: %s---%s" % (self.name, "ResB", time.time()))
        time.sleep(0.2)

        mutex.acquire()
        print("I am %s , get res: %s---%s" % (self.name, "ResA", time.time()))
        mutex.release()

        mutex.release()


if __name__ == "__main__":

    print("start---------------------------%s" % time.time())

    for i in range(0, 10):
        my_thread = MyThread()
        my_thread.start()
