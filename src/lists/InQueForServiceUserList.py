from collections import deque


class InQueForServiceUserList(deque):
    def __init__(self):
        super().__init__()
        self.userCount = 0

    def append(self, user):
        super().append(user)
        self.userCount += 1

    def pop(self):
        self.userCount -= 1
        return super().pop()
    def isEmpty(self):
        return self.userCount == 0
