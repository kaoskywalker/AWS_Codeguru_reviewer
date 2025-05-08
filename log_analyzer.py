# flawed_script.py

import os
import time
import json
from datetime import datetime

logfile = 'server.log'
log_data = []
cache = {}

# Global mutable variable
user_sessions = {}

def read_log_file():
    f = open(logfile, 'r')
    lines = f.readlines()
    f.close()
    return lines

def parse_log_line(line):
    parts = line.split(" ")
    if len(parts) < 5:
        return None
    return {
        'timestamp': parts[0] + " " + parts[1],
        'ip': parts[2],
        'user': parts[3],
        'action': parts[4].strip()
    }

def process_logs():
    lines = read_log_file()
    for line in lines:
        parsed = parse_log_line(line)
        if parsed is not None:
            log_data.append(parsed)

def get_most_active_user():
    counts = {}
    for entry in log_data:
        user = entry['user']
        if user not in counts:
            counts[user] = 1
        else:
            counts[user] += 1
    max_user = ''
    max_count = 0
    for u in counts:
        if counts[u] > max_count:
            max_user = u
            max_count = counts[u]
    return max_user

def print_all_actions():
    for i in range(len(log_data)):
        print("Action by", log_data[i]['user'], ":", log_data[i]['action'])

def write_summary_file():
    summary = {
        'generated_at': str(datetime.now()),
        'most_active_user': get_most_active_user(),
        'total_logs': len(log_data)
    }
    f = open("summary.json", "w")
    f.write(json.dumps(summary))  # no indentation
    f.close()

def simulate_delay_and_cache(ip):
    if ip in cache:
        return cache[ip]
    time.sleep(2)  # simulate slow fetch
    info = {"country": "unknown"}  # not real lookup
    cache[ip] = info
    return info

def enrich_logs_with_geo():
    for entry in log_data:
        ip = entry['ip']
        geo = simulate_delay_and_cache(ip)
        entry['geo'] = geo

def clear_all_logs():
    global log_data
    log_data = []

def main():
    print("Starting log analysis...")
    process_logs()
    print_all_actions()
    enrich_logs_with_geo()
    write_summary_file()
    print("Log analysis complete.")

if __name__ == '__main__':
    main()
