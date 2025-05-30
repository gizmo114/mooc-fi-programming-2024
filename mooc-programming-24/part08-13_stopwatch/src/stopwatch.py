# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds != 59:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes != 59:
                self.minutes += 1
            else:
                self.minutes = 0
                self.seconds = 0

    def __str__(self):
        minutes = "{:02d}".format(self.minutes)
        seconds = "{:02d}".format(self.seconds)
        return f"{minutes}:{seconds}"
