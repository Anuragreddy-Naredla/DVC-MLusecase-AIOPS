import yaml
import os

def read_yaml(path_to_yaml: str) -> dict:
    """
    This function is used to read the yaml file.
    """
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_dir(dirs:list):
    """
    This function is used to create directories from list.
    """
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directories is created at {dir_path}")
        