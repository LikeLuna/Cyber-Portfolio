#!/usr/bin/env python3

import base64

FILE_PATH = "/dev/shm/home/o.deer/westtech_projects/thm_flags.txt"

with open(FILE_PATH, "r") as file:

    for line_number, line in enumerate(file, 1):

        line = line.strip()

        if not line:
            continue

        try:
            decoded = base64.b64decode(line).decode("utf-8")

            print(f"[Line {line_number}] {decoded}")

        except Exception as error:

            print(f"[Line {line_number}] Failed to decode -> {error}")

