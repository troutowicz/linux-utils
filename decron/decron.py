#!/usr/bin/env python

from argparse import ArgumentParser

field_names = ['minutes', 'hours', 'days', 'months', 'weekdays']

def format_field_name(field, name):
    return name[:-1] if '-' not in field else name

def decron(job):
    columns = job.split(' ', 5)
    fields = columns[:5]
    cmd = columns[5] if len(columns) == 6 else None
    when = ''
    for idx, field in enumerate(fields):
        field_split = field.split(',')
        if idx > 0:
            when += ' of ' if idx % 2 else ' on '
        when += '['
        for idx2, field in enumerate(field_split):
            field, delim, step = field.partition('/')
            if idx2 > 0: when += ' AND '
            if field == '*' and step != '':
                when += 'every ' + step + ' ' + field_names[idx]
            elif field == '*':
                when += 'every ' + field_names[idx][:-1]
            elif step != '':
                when += 'every ' + step + ' ' + field_names[idx] + ' when ' + \
                    format_field_name(field, field_names[idx]) + ' ' + field
            else:
                when += format_field_name(field, field_names[idx]) + ' ' + field
        when += ']'
    return when, cmd

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', action = 'store_true')
    parser.add_argument('cronjob', nargs = '?')
    args = parser.parse_args()

    if args.file:
        with open(args.cronjob) as jobs:
            for job in jobs:
                if job[0] != '#' and job.strip() != '':
                    when, cmd = decron(job)
                    print when
                    if cmd:
                        print cmd
    else:
        when, cmd = decron(args.cronjob)
        print when
        if cmd:
            print cmd

