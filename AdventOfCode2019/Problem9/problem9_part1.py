'''
class Computer:
    def __init__(self):
        self.memory = [int(x) for x in open('input_problem9.txt').read().split(",")]
        self.instruction_pointer = 0
        self.relative_pointer = 0 
        self.halt = False 

    def run_instruction(self):
        #print(self.memory)
        first_instruction = self.memory[self.instruction_pointer]
        #print("Relative Pointer : ", self.relative_pointer)
        #print(self.memory[0:1200])

        # opcode input 
        if int(str(first_instruction)[-1]) == 3:
            input_value = int(input("Enter Input: "))
            # position mode 
            if len(str(first_instruction)) == 1:
                output_address = self.memory[self.instruction_pointer + 1]
                self.memory[output_address] = input_value
            # relative mode 
            elif len(str(first_instruction)) == 3:
                print(first_instruction)
                output_address = self.memory[self.instruction_pointer + 1] + self.relative_pointer
                self.memory[output_address] = input_value
            # not inclduing fact that immediate mode could be there ? this could cause issues or not?
            self.instruction_pointer += 2

        # TBD (Need to account for relative mode)
        # opcode output 
        elif int(str(first_instruction)[-1]) == 4:
            # positional 
            if len(str(first_instruction)) == 1:
                output_address = self.memory[self.instruction_pointer + 1]
                print(self.memory[output_address])
            # immediate or relative
            elif len(str(first_instruction)) == 3:
                # immediate mode 
                if int(str(first_instruction)[-3]) == 1:
                    print(self.memory[self.instruction_pointer + 1])
                # relative mode 
                elif int(str(first_instruction)[-3]) == 2:
                    relative_mode = self.memory[self.instruction_pointer + 1]
                    print(self.memory[self.relative_pointer + relative_mode])
                # error 
                else:
                    print("ERROR IN OPCODE 4")
            # error 
            else: 
                print("ERROR IN OPCODE 4")
            self.instruction_pointer += 2

        # opocode halt 
        elif first_instruction == 99:
            self.halt = True 

        # opcode addition
        elif int(str(first_instruction)[-1]) == 1:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            value3 = self.memory[self.instruction_pointer + 3]
            self.memory[value3] = value1 + value2
            self.instruction_pointer += 4

        # opcode multiplication 
        elif int(str(first_instruction)[-1]) == 2:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            value3 = self.memory[self.instruction_pointer + 3]
            self.memory[value3] = value1 * value2
            self.instruction_pointer += 4

        # opcode 5 
        elif int(str(first_instruction)[-1]) == 5:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            #print("Value1: ", value1)
            #print("Value2: ", value2)
            if value1 != 0:
                self.instruction_pointer = value2
            else:
                self.instruction_pointer += 3

        # opcode 6
        elif int(str(first_instruction)[-1]) == 6:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            if value1 == 0:
                self.instruction_pointer = value2
            else:
                self.instruction_pointer += 3

        # opcode 7
        elif int(str(first_instruction)[-1]) == 7:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            value3 = self.memory[self.instruction_pointer + 3]
            if value1 < value2: 
                self.memory[value3] = 1
            else:
                self.memory[value3] = 0
            self.instruction_pointer += 4

        # opcode 8
        elif int(str(first_instruction)[-1]) == 8:
            value1, value2 = self.get_values([int(number) for number in str(first_instruction)].copy())
            value3 = self.memory[self.instruction_pointer + 3]
            if value1 == value2: 
                self.memory[value3] = 1
            else:
                self.memory[value3] = 0
            self.instruction_pointer += 4

        # opcode 9 : relative base offset 
        # TBD 
        elif int(str(first_instruction)[-1]) == 9:
            # positional 
            if len(str(first_instruction)) == 1:
                relative_mode = self.memory[self.instruction_pointer + 1]
                self.relative_pointer += self.memory[relative_mode]
            # immediate or relative
            elif len(str(first_instruction)) == 3:
                # immediate mode 
                if int(str(first_instruction)[-3]) == 1:
                    self.relative_pointer += self.memory[self.instruction_pointer + 1]
                # relative mode 
                elif int(str(first_instruction)[-3]) == 2:
                    relative_mode = self.memory[self.instruction_pointer + 1] + self.relative_pointer
                    self.relative_pointer += self.memory[relative_mode]
                # error 
                else:
                    print("ERROR IN OPCODE 9")
            # error 
            else: 
                print("ERROR IN OPCODE 9")
            self.instruction_pointer += 2

    def get_values(self, instruction):
        # editing instruction so easy to read 
        for num in range(4 - len(instruction)):
            instruction.insert(0, 0)

        # getting value1
        # position mode 
        if instruction[-3] == 0:   
            address1 = self.memory[self.instruction_pointer + 1]
            value1 = self.memory[address1]
        # immediate mode
        elif instruction[-3] == 1:  
            value1 = self.memory[self.instruction_pointer + 1]
        # relative mode 
        elif instruction[-3] == 2:
            relative_mode = self.memory[self.instruction_pointer + 1]
            value1 = self.memory[self.relative_pointer + relative_mode]
        else:
            print("ERROR")

        # getting value2
        # position mode 
        if instruction[-4] == 0:   
            address2 = self.memory[self.instruction_pointer + 2]
            value2 = self.memory[address2]
        # immediate mode
        elif instruction[-4] == 1:  
            value2 = self.memory[self.instruction_pointer + 2]
        # relative mode 
        elif instruction[-4] == 2:
            relative_mode = self.memory[self.instruction_pointer + 2]
            value2 = self.memory[self.relative_pointer + relative_mode]
        else:
            print("ERROR")

        # returning both values 
        return value1, value2 

    def get_halt(self):
        return self.halt 

def main():
    intcode_computer = Computer()   
    intcode_computer.memory += ([0] * 100000000)
    # running problem 5
    # do something like this: while computer_finished 
    while not intcode_computer.get_halt():
        intcode_computer.run_instruction()
        #print(intcode_computer.memory[0:2000])
        #print("---------------------------------------", '\n')
main()
'''


'''
NEED TO add relative base support (this inlcuded opcode 9)
Should be able to support numbers not in memory 
getting stuck at instruction 203 (maybe error with the 9 which is relative base? but first test case worked 
'''

'''
IM GOING TO REWORK EVERYTHING STARTING FROM 2 SO BASICALLY GOING FROM 2, 5 and then doing 9 
MAKE A GOOD INTCODE COMPUTER 
'''