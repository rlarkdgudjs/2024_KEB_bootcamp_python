def desc(func):
    def wrap():
        print("w")
        func()
        print("w")
    return wrap


def some():
    print("do some")


Play = desc(some)
Play()
