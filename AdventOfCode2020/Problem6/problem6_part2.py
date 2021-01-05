import collections

def main():
    total_count = 0
    file1 = 'input_problem6.txt'
    input_file = open(file1).read().split("\n\n")
    for group in input_file:
        counter1 = collections.Counter(group.replace("\n", ""))
        group = group.split("\n")
        for letter in counter1:
            if counter1[letter] == len(group):
                total_count += 1
    print(total_count)

main()

