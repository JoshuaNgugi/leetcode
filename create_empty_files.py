import sys

if __name__ == '__main__':
    file_name = 'test'
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Usage: python create_empty_file [filename]")
    print(f"Creating {file_name}in java and python dir...")
    with open(f"python/{file_name}.py", 'w'):
        pass
    with open(f"java/{file_name}.java", 'w'):
        pass
    print("Done!")
