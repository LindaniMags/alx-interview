#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import re


def input_parser(line):
    """
    extracts the metrics from a given HTTP request log
    """
    log_pat = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )

    matics_data = {
        'status_code': 0,
        'file_size': 0,
    }

    log_fmt = f"{log_pat[0]}\\-{log_pat[1]
                                }{log_pat[2]}{log_pat[3]}{log_pat[4]}\\s*"

    log = re.fullmatch(log_fmt, line)

    if log is not None:
        status_code = log.group('status_code')
        file_size = int(log.group('file_size'))
        matics_data['status_code'] = status_code
        matics_data['file_size'] = file_size

    return matics_data


def get_total(line, total_size, stats):
    """
    gets the current file size and adds it to
    the total file size
    """
    matrics_data = input_parser(line)
    status_code = matrics_data.get('status_code', '0')
    if status_code in stats.keys():
        stats[status_code] += 1
    return total_size + matrics_data['file_size']


def print_matrics(total_size, stats):
    """
    displays the computed matrics on the screen
    """
    print(f'File size: {total_size}', flush=True)
    for status_code in sorted(stats.keys()):
        num = stats.get(status_code, 0)
        if num > 0:
            print(f'{status_code}: {num}', flush=True)


def print_stats():
    """
    prints the current statistics
    """
    line_count = 0
    total_size = 0
    stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_size = get_total(
                line,
                total_size,
                stats,
            )
            line_count += 1
            if line_count % 10 == 0:
                print_matrics(total_size, stats)
    except (KeyboardInterrupt, EOFError):
        print_matrics(total_size, stats)


if __name__ == '__main__':
    print_stats()
