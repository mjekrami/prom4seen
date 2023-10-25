from datetime import datetime, timedelta, date



class Range:
    _UNIT_MAP = {
        "m": "minutes",
        "h": "hours",
        "d": "days",
        "w": "weeks"
    }

    def __init__(self, step: int, unit: str) -> None:
        self.step = step
        self.unit = unit

        if self.unit not in Range._UNIT_MAP:
            raise ValueError(f"Unit {self.unit} is not supported")

        self._from = None
        self._to = None

    def from_now(self):
        if self._from is not None:
            raise ValueError("From time is already defined.")
        self._from = datetime.now()
        return self

    def from_t(self, date_obj: date):
        if self._from is not None:
            raise ValueError("From time is already defined.")
        self._from = datetime.combine(date_obj, datetime.min.time())
        return self

    def to(self, date_obj: date):
        if self._to is not None:
            raise ValueError("To time is already defined.")
        self._to = datetime.combine(date_obj, datetime.max.time())
        if self._from and self._from > self._to:
            raise ValueError("Invalid date range.")
        return self

    def calculate_range(self):
        if self._from is None or self._to is None:
            raise ValueError("Both 'from' and 'to' must be defined.")
        
        return {"start_time": self._from,
                "end_time": self._to
                }
    def __iter__(self):
        return iter({
            'start_time': self._from,
            'end_time': self._to
        })


r = Range(5,"m")
res = r.from_now().to(datetime.now()).calculate_range()
print(res)