def main():
    total_count = 0
    file1 = 'input_problem6.txt'
    input_file = open(file1).read().split("\n\n")
    for group in input_file:
        group = len(set(group.replace('\n', '')))
        total_count += group
    print(total_count)

main()