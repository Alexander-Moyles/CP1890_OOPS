import datetime

class Event:

    def __init__(self, name='', location='', start_date='', end_date=''):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

    def duration(self):
        return self.end_date - self.start_date

class Conference(Event):
    def __init__(self, name='', location='', start_date='', end_date='', attendees=''):
        Event.__init__(self, name, location, start_date, end_date)

        self.attendees = attendees

