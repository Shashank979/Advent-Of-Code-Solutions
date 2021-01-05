
def by_line():
    """ takes a file and then reads it by line so you get a list with each variable
    being a line from the file"""
    file1 = 'input_test.txt'
    input_file = open(file1).read().splitlines()
    print(input_file)

def by_comma():
    """ splits the file by comma"""
    file1 = 'input_test.txt'
    input_file = [int(x) for x in open(file1).read().split(",")]
    print(input_file)

def by_all():
    """ takes file as one string """
    file1 = 'input_test.txt'
    input_file = open(file1).read()
    print(input_file)

