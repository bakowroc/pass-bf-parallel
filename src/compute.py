def compute(args):
    import socket
    import itertools
    import string

    def generate_strings(length):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        for item in itertools.product(chars, repeat=length):
            yield "".join(item)

    host = socket.gethostname()
    comparator = args[0]
    base_string = args[1]
    is_correct = False
    answer = ''

    for generated in generate_strings(length=len(comparator) - len(base_string)):
        generated_string = f'{base_string}{generated}'
        is_correct = generated_string == comparator
        if is_correct:
            dispy_provisional_result((host, generated_string, is_correct))
            break

    return host, answer, is_correct
