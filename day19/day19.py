from computer import Computer
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')


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

        # computer = Computer(instructions=list(instructions), pointer=pointer)
        # computer.run_until_finished()
        # print(computer.register)

        # computer = Computer(instructions=list(instructions), pointer=pointer, register=[0, 1, 0, 10551263, 6, 10551264])
        computer = Computer(instructions=list(instructions), pointer=pointer, register=[1, 0, 0, 0, 0, 0])
        computer.run_until_finished()
        print(computer.register)

