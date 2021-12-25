import sys
import solution_01


def main(argv):

    print()
    print("Solution 1: ")
    print("     input: [3,2], [1,1], [2,1], 4")
    print("  expected: 7")
    print("    actual: {}".format(solution_01.solution([3,2], [1,1], [2,1], 4)))
    print()

    print()
    print("Solution 1: ")
    print("     input: [300,275], [150,150], [185,100], 500")
    print("  expected: 9")
    print("    actual: {}".format(solution_01.solution([300,275], [150,150], [185,100], 500)))
    print()



if __name__ == "__main__":
    main(sys.argv[1:])
