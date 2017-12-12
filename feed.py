class Feed(object):
    def __init__(self, message, name, picture, reactions):
        self.values = [message, name, picture, reactions]
        # Heapq
        self.reactions = -1 * reactions

    def __lt__(self, other):
        return self.reactions < other.reactions

    def __eq__(self, other):
        return self.reactions == other.reactions