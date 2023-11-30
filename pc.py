#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author by wangcw
# @generate at 2023-11-28 16:14:31

import os

home_dir = os.path.expanduser("~")
ssh_config = os.path.join(home_dir, ".ssh/config")

with open(ssh_config, "r") as file:
    lines = file.readlines()

excluded_hosts = ['github.com', 'ssh.wongjc.cn']
result = []

line = 0
while line < len(lines):
    if lines[line].startswith('Host') and not any(host in lines[line] for host in excluded_hosts):
        host_line = lines[line].strip().split(' ')
        host = host_line[1]
        user = ''
        hostname = ''
        line += 1
        while line < len(lines) and not lines[line].startswith('Host'):
            if lines[line].startswith('  User'):
                user = lines[line].strip().split(' ')[1]
            elif lines[line].startswith('  HostName'):
                hostname = lines[line].strip().split(' ')[1]
            line += 1
        if user and hostname:
            result.append(f'{host} {user}@{hostname}')
    else:
        line += 1

output = '\n'.join(result)
print(output)
