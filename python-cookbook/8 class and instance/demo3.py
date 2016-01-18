class Tieba:
    def __init__(self):
        self.a = 10

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.a

