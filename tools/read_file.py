


def read_file(filename:str) -> list:
    
    with open(filename) as f:
        file_data = [line.rstrip() for line in f.readlines()]
    
    return file_data

