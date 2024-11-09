class History:
    def __init__(self):
        self._history = []

    def add_calculation(self, calculation):
        if not isinstance(calculation, str):
            raise TypeError("calculation must be a string")
        self._history.append(calculation)

    def get_history(self):
        return self._history.copy()

    def clear_history(self):
        self._history.clear()

    def undo_last(self):
        if self._history:
            return self._history.pop()
        else:
            print("History is already empty.")