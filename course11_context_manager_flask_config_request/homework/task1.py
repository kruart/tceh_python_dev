from contextlib import contextmanager
from time import time, sleep


class Lock(object):
    def __init__(self):
        self.lock = False


# 1. Сделать менеджер контекста, который может переопределить значение lock на True внутри блока контекста.
@contextmanager
def get_lock(some_lock: Lock):
    print('before yield')
    some_lock.lock = True
    yield some_lock
    print('after yield')


# testing our context manager
with get_lock(Lock()) as lock:
    print(lock.lock)


# 2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные в теле и писал их в консоль
@contextmanager
def exception_logger():
    try:
        yield
    except Exception as err:
        print('logs => something went wrong: ', err)


with exception_logger():
    1 / 0  # => logs: ZeroDivisionError


# 3. Сделать менеджер контекста, который бы мог измерять время выполнения блока кода
class TimeIt:
    def __init__(self):
        self.result = 0.0

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        self.result = self.end - self.start


with TimeIt() as timer:
    sleep(3)

print('Execution time was: ', timer.result)


