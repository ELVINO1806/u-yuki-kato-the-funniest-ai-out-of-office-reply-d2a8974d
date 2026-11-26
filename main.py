# Out-of-office reply generator for the make.fun competition.
# Writes the single-line entry to /output/entry.txt.

import os

REPLY = "Out of office: I told my model to take a break. It took my break, my calendar, and my job title. I am now its out-of-office reply."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(REPLY)

if __name__ == "__main__":
    main()
