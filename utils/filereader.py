import os

def read_input_file(file_path):
    """
    Reads the content of a plain text file, resolving paths relative to the module's directory.
    """
    # Get the directory of the current script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.join(base_dir, file_path)
    
    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"The file '{absolute_path}' does not exist.")

    with open(absolute_path, "r", encoding="utf-8") as file:
        return file.read()

def format_input(filepath, split_criteria, should_split=False):
    data = read_input_file(filepath)
    if should_split:
        if split_criteria is None:
            split_data = data.split()
        else:
            split_data = data.split(split_criteria)
        return split_data
    else:
        return data
