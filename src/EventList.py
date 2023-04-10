from collections import deque


class EventList(deque):
    def giveLast2Elements(self):
        if len(self) < 2:
            return None
        else:
            return (self[-2], self[-1])