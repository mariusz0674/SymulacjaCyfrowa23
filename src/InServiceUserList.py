from collections import deque

from src.EnvironmentalConstants import EnvironmentalConstants


class InServiceUserList(deque):
    def __init__(self, maxlen=EnvironmentalConstants.MAX_USSERS_IN_SYSTEM):
        super().__init__(maxlen=maxlen)
        self.userCount = 0

    def append(self, user):
        if self.userCount >= EnvironmentalConstants.MAX_USSERS_IN_SYSTEM:
            return False
        super().append(user)
        self.userCount += 1

