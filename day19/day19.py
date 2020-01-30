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

        computer = Computer(instructions=list(instructions), pointer=pointer)
        computer.run_until_finished()
        print(computer.register)

        # computer = Computer(instructions=list(instructions), pointer=pointer, register=[1, 0, 0, 0, 0, 0])
        # computer.run_until_finished()
        # print(computer.register)

        # Part 2 is summing all the divisors of 10551264
        out = 0
        endnum = 10551264
        for i in range(1, endnum+1):
            if endnum % i == 0:
                out += i
        print(out)

