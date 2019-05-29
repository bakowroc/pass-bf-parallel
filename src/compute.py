def compute(args):
    import socket
    host = socket.gethostname()
    comparator = args[0]
    strings = args[1]

    is_correct = False
    answer = ''

    for s in strings:
        is_correct = s == comparator
        if is_correct:
            answer = s
            dispy_provisional_result((host, answer, is_correct))

    return host, answer, is_correct
