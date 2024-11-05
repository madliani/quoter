class TupleItemError(Exception):
    def __init__(self):
        self.message = "No tuple items!"

    def __str__(self):
        return self.message
