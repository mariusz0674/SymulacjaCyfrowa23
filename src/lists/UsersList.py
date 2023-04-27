from collections import deque

class UsersList(deque):
    def czyToFunkcja(self, element):
        """
        Sprawdza czy dany element jest funkcją
        """
        return callable(element)