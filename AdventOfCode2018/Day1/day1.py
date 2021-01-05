def part1():
    with open('advent1prob.txt') as f:
        advent_text = [int(i) for i in f]
    advent_text = sum(advent_text)
    print(advent_text)
    
def part2():
    with open('advent1prob.txt') as f:
        advent_text = [int(i) for i in f]
    sum1 = 0
    sum_list = []
    end = False
    while end == False:
        for num in advent_text:
            sum1 += num
            print(sum1)
            if sum1 in sum_list:
                print(sum1)
                end = True
                break
            sum_list.append(sum1)
            

                
            
part2()
