import sys
import solution_01


def main(argv):

    print("")
    print("Solution 1: ")
    print("     input: 4")
    print("  expected: 2")
    print("    actual: {}".format(solution_01.solution(4)))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: 15")
    print("  expected: 5")
    print("    actual: {}".format(solution_01.solution(15)))
    print("")



if __name__ == "__main__":
    main(sys.argv[1:])
