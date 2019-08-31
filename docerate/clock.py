import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        args_str = ','.join(repr(arg) for arg in args)
        name = func.__name__
        print('[%0.8fs] %s(%s) -> %s' % (elapsed, name, args_str, result))
        return result
    return clocked


@clock
def snooze(n):
    time.sleep(n)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__ == "__main__":
    print('*'*40, 'Call snooze(.345)', snooze.__name__)
    snooze(.345)
    print('*'*40, 'Call factorial(6)', factorial.__name__)
    factorial(6)
