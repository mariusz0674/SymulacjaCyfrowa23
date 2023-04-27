from bisect import insort
from collections import deque


class EventList(deque):
    def __init__(self):
        super().__init__()
        self.currentIndex = 0


    def giveLast2Elements(self):
        if len(self) < 2:
            return None
        else:
            return (self[-2], self[-1])

    def append(self, event):
        insort(self, event, key=lambda e: e.timeOfTheEvent)

    def getNext(self):
        if self.currentIndex >= len(self):
            return None
        nextItem = self[self.currentIndex]
        self.currentIndex += 1
        return nextItem

    def isEnd(self):
        if self.currentIndex >= len(self):
            return True
        return False
