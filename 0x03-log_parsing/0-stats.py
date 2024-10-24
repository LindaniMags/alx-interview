#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_stats():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """Handles keyboard interruption."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0

for line in sys.stdin:
    line_count += 1

    try:
        parts = line.split()
        ip = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        if status_code in status_counts:
            status_counts[status_code] += 1

        total_size += file_size

        if line_count % 10 == 0:
            print_stats()

    except (IndexError, ValueError):
        continue


if __name__ == '__main__':
    print_stats()

