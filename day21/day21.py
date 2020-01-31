import pathlib
from computer import Computer

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


if __name__ == '__main__':
    with open(dpath, 'r') as f:
        instructions = []
        for line in f:
            line = line.strip()
            if '#ip' in line:
                pointer = int(line.split()[-1])
            else:
                line = line.split()
                line = [line[0]] + list(map(int, line[1:]))
                instructions.append(line)
        # register = [0, 10664125, 45538, 22, 0, 175]
        # register = [0, 2813690, 177, 28, 1, 1]
        register = [2813690, 431003, 65536, 21, 0, 253]
        # register = [0] * 6
        # register[0] = 11592302
        register[0] = 0
        computer = Computer(instructions=instructions, register=register, pointer=pointer)
        # computer.run_until_finished()
        output = []
        output_set = set()
        instr_index = 0
        while instr_index < len(computer.instructions):
            instr = computer.instructions[computer.get_pointer()]
            if instr[0] == 'eqrr':
                val = computer.register[1]
                if val in output_set:
                    print(f'FOUND A REPEATED NUM')
                    break
                output_set.add(val)
                output.append(val)
                print(output)
            computer.run()
            instr_index = computer.get_pointer()

        print(output)

