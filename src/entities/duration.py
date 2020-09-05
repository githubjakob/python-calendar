from datetime import time


class Duration:
    def __init__(self, start: str, end: str):
        self.start = time.fromisoformat(start)
        self.end = time.fromisoformat(end)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
