import os
LINE = "Out of office: I told my model to take a break. It took my break, my calendar, and my job title. I am now its out-of-office reply."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
