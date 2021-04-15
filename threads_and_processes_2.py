'''2. Print current date by using 2 threads.
#1. Define a subclass using Thread class.
#2. Instantiate the subclass and trigger the thread. '''
import datetime
import time
from multiprocessing import Process


class Worker(Process):
    def run(self) -> None:
        print(f'In {self.name}')
        time.sleep(2)
        print(f'Date is {datetime.date.today()}')


thread = Worker()
thread.start()
thread.join()
