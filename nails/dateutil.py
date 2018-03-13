# coding=utf-8
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

class DateFormats(object):
    Full = '%m/%d/%Y %H:%M:%S.%f'


def epoch_seconds(dt):
    return (dt - epoch).total_seconds()


def formated(dt, format_str=DateFormats.Full):
    return dt.strftime(format_str)


if __name__ == '__main__':
    print(formated(datetime.datetime.now()))
