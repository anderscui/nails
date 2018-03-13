# coding=utf-8
import datetime
import ujson as json


class Date(object):
    def __init__(self, year=None, month=None, day=None, until_now=False):

        self.validate(day, month, until_now, year)

        self.year = year
        self.month = month
        self.day = day
        self.until_now = until_now

    @staticmethod
    def format_date(dt):
        return '{0}/{1}/{2}'.format(dt.year, dt.month, dt.day)

    @staticmethod
    def parse_date(s):
        return datetime.datetime.strptime(s, '%Y/%m/%d').date()

    def validate(self, day, month, present, year):
        if not present and year is None:
            raise ValueError('Use present or a specific date')

        if not (month is None or 1 <= month <= 12):
            raise ValueError('month must be in 1..12')

        if not (day is None or 1 <= day <= 31):
            raise ValueError('day must be in 1..31')

    @property
    def date(self):
        if self.until_now:
            return datetime.date.today()
        else:
            return datetime.date(self.year if self.year else datetime.date.today().year,
                                 self.month if self.month else 1,
                                 self.day if self.day else 1)

    @property
    def missing_year(self):
        return self.year is None

    @property
    def missing_month(self):
        return self.month is None

    @property
    def missing_day(self):
        return self.day is None

    def formated(self):
        return Date.format_date(self.date)

    def __str__(self):
        if self.until_now:
            return '至今'

        parts = []
        elems = [self.year, self.month, self.day]
        for elem in elems:
            if elem:
                parts.append(unicode(elem))
            else:
                break
        return '/'.join(parts)


class DateRange(object):
    def __init__(self, date_from, date_to):

        if date_from is None or date_to is None:
            raise ValueError('Both data_from and date_to should be set.')

        self.date_from = date_from
        self.date_to = date_to

    def tojson(self):
        return json.dumps({'from': {'date': Date.format_date(self.date_from.date), 'until_now': self.date_from.until_now},
                           'to': {'date': Date.format_date(self.date_to.date), 'until_now': self.date_to.until_now}})
