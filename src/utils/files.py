import re


def get_file_data(file_path: str) -> str:
    with open(file_path, "r") as file:
        data = file.read()

    return data


def parse_line(line):
    match = re.match(r"^(\d+)\|(.*?): (.*)$", line)

    if not match:
        return None

    order_id = int(match.group(1))
    exercise_name = match.group(2).strip()
    sets_data = match.group(3).split(", ")
    sets = []

    for set_data in sets_data:
        set_match = re.match(r"(\d+)x(\d+)x(\d+(?:\.\d+)?)", set_data)
        if set_match:
            sets.append((int(set_match.group(1)), int(
                set_match.group(2)), float(set_match.group(3))))

    return order_id, exercise_name, sets


"""
con = sqlite3.connect(DB_NAME)
cursor = con.cursor()

for root, dirs, files in os.walk(DATA_FOLDER):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    result = parse_line(line)
                    print(result)

        con.commit()
"""
