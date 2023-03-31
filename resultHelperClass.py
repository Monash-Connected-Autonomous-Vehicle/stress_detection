from typing import Any


class Result:
    def __init__(self):
        self.value: [None, Any] = None

    def update_value(self, val):
        self.value = val

    def get_value(self):
        return self.value

    def is_done(self) -> bool:
        if self.value is None:
            return False
        else:
            return True
