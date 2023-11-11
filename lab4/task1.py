import json

INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE) as input_file:
        data = json.load(input_file)
    sum_ = sum([items["score"] * items["weight"] for items in data])
    return round(sum_, 3)

print(task())
