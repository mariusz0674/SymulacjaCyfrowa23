from collections import deque

from src.EnvironmentalConstants import EnvironmentalConstants


class InQueForServiceUserList(deque):
    def __init__(self):
        super().__init__()
        self.userCount = 0

    def append(self, user):
        super().append(user)
        self.userCount += 1

