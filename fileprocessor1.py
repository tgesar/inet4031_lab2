#!/usr/bin/env python3

with open('fileprocessor.input') as file:
    print("Printing out User Data:\n")

    for line in file:
        if line.startswith('#'):
            skipped_data = line.strip().split(':')
            if len(skipped_data) > 1:
                print(f"{skipped_data[0]} is skipped because it starts with a hashtag (commented out)")
        else:
            data = line.strip().split(':')
            if len(data) == 4:
                print(f"The user {data[0]} has a password of {data[1]} and has a userid {data[2]} and groupid {data[3]}")

    print("\nEnd of User Data")

