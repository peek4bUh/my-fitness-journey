def get_file_data(file_path: str) -> str:
    with open(file_path, "r") as file:
        data = file.read()

    return data
