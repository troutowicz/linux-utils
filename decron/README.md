# decron

> Cron job parsing for humans

```bash
usage: decron.py [-h] [-f] [cronjob]

positional arguments:
  cronjob

optional arguments:
  -h, --help  show this help message and exit
  -f, --file
```

### Examples

```bash
$ ./decron.py '* * * * * command'
[every minute] of [every hour] on [every day] of [every month] on [every weekday]
command
```

```bash
$ ./decron.py '30/5 0,2-12 * 1 0 command'
[every 5 minutes when minute 30] of [hour 0 AND hours 2-12] on [every day] of [month 1] on [weekday 0]
command
```

```bash
$ ./decron.py -f /var/spool/cron/root
```
