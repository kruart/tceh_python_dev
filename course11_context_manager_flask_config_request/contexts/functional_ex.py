from contextlib import contextmanager


@contextmanager
def do_work(value, mode='r'):
    print('some work before, __enter__')
    open_file = open(value, mode)
    try:
        yield open_file
    except Exception as e:
        print('Exception was here!')
        #yield None
    else:
        #yield open_file
        open_file.close()
    print('some work after, __exit__')


with do_work('to_open.txt') as w:
    print(w)
    if w is not None:
        print(w.read())