import sys
import solution_01



def main(argv):

    print("")
    print("Solution 1: ")
    print("     input: 2, 3, 4")
    print("  expected: 430")
    print("    actual: {}".format(solution_01.solution(2, 3, 4)))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: 2, 2, 2")
    print("  expected: 7")
    print("    actual: {}".format(solution_01.solution(2, 2, 2)))
    print("")



if __name__ == "__main__":
    main(sys.argv[1:])
