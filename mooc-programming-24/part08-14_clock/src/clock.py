class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        if self.seconds != 59:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes != 59:
                self.minutes += 1
            else:
                if self.hours != 23:
                    self.hours += 1
                else:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0

    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        hours = "{:02d}".format(self.hours)
        minutes = "{:02d}".format(self.minutes)
        seconds = "{:02d}".format(self.seconds)
        return f"{hours}:{minutes}:{seconds}"
