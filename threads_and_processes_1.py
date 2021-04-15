import threading
import time
from concurrent.futures import ThreadPoolExecutor


def target():
    time.sleep(2)


def active_count():
    print(f'active are {threading.active_count()}')


with ThreadPoolExecutor(max_workers=2) as ex:
    ex.submit(target)
    ex.submit(target)
    active_count()
active_count()
