# decorators take functions as arguments and use them inside itself

def caps(function):
    def ups():
        function("Kevin")

    return ups


def naming(k):
    print(k.upper())


f = caps(naming)
f()