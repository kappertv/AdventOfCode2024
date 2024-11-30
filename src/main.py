def hello_world():
    return "Hello, World!"

def process_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    # Verwerk de inhoud
    return data.upper()  # Bijvoorbeeld