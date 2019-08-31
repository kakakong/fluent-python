import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t0 = time.time() - t0
        name = func.__name__
        args_list = []
        if args:
            args_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ', '.join('%s:%r' % (k, v)
                              for k, v in sorted(kwargs.items()))
            args_list.append(pairs)
        args_str = ', '.join(args_list)
        print('[%0.6f] %s(%s) -> %s' % (t0, name, args_str, result))
        return result
    return clocked


@clock
def snooze_hello(n, d=None):
    if d is None:
        d = {}
    else:
        d = dict(d)
    time.sleep(n)
    print('%s:%s' % (k, v) for k, v in sorted(d.items()))


if __name__ == "__main__":
    print('*'*40, 'Call %s' % snooze_hello.__name__)
    snooze_hello(3, {"zrg": "handsome"})
