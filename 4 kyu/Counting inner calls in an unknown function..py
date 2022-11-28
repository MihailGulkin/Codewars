from sys import settrace


def count_calls(func, *args, **kwargs):
    calls = [-1]

    def tracer(frame, event, arg):
        if event == 'call':
            calls[0] += 1
        return tracer

    settrace(tracer)
    f = func(*args, **kwargs)

    return calls[0], f
