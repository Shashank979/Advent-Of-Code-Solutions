def main():
    input_file = open('input_problem8.txt').read()
    print(input_file)
    list_nums = [int(num) for num in input_file]
    width = 25
    height = 6
    layers = []
    for num in range(0, len(list_nums), width * height):
        if num != len(list_nums) - 1:
            layers.append(list_nums[num : num + width * height])
    #print(layers)
    layer_least_zeros = 0
    for index, layer in enumerate(layers):
        if layer.count(0) < layers[layer_least_zeros].count(0):
            layer_least_zeros = index
    ones = layers[layer_least_zeros].count(1)
    twos = layers[layer_least_zeros].count(2)
    return ones * twos 

print(main())