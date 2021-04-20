"""
Create a script that should find the lines by provided pattern in the provided path directory with recursion
(it means if the directory has other directories,
the script should get all the info from them as well) and threads.
"""
import glob
from concurrent.futures import ThreadPoolExecutor


def find_by_pattern(filename, pattern):
    line_container = set()
    with open(filename) as f:
        for line in f:
            if pattern in line:
                line_container.add(line)
    return line_container


def find_all_files(directory_path, pattern):
    files = glob.glob(f'{directory_path}/*.py')
    container = set()
    # with ThreadPoolExecutor() as pool:
    #     result = pool.map(find_by_pattern, files, pattern * len(files))
    for file in files:
        result = find_by_pattern(file, pattern)
        container.update(result)
    try:
        directories = glob.glob(f'{directory_path}/*')
        for directory in directories:
            content = find_all_files(directory, pattern)
            container.update(content)
    except:
        print('bad')
    return container


if __name__ == '__main__':
    search_by_pattern = find_all_files('..', pattern='==')
    for row in search_by_pattern:
        print(row)
