#!/usr/bin/python3
import re

input_format = re.compile(r'\d+\.\d+\.\d+\.\d+ - \[.+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

count = 0
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
while True:
    try:
        line = input()
        match = input_format.match(line)
        if match:
            cur_status_code, cur_file_size = match.groups()
            cur_status_code, cur_file_size = int(cur_status_code), int(cur_file_size)
            if cur_status_code in status_code_count.keys():
                status_code_count[cur_status_code] += 1
            total_file_size += cur_file_size
        else:
            continue
        count += 1
        if count == 10:
            print(f"File size: {total_file_size}")
            for k, v in status_code_count.items():
                print(f"{k}: {v}")
            count = 0
    except KeyboardInterrupt:
        print(f"File size: {total_file_size}")
        for k, v in status_code_count.items():
            print(f"{k}: {v}")
