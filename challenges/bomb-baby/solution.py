import sys
import solution_01



def main(argv):

    print("")
    print("Solution 1: ")
    print("     input: 4, 7")
    print("  expected: 4")
    print("    actual: {}".format(solution_01.solution("4", "7")))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: 2, 1")
    print("  expected: 1")
    print("    actual: {}".format(solution_01.solution("2", "1")))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: 2, 4")
    print("  expected: impossible")
    print("    actual: {}".format(solution_01.solution("2", "4")))
    print("")



if __name__ == "__main__":
    main(sys.argv[1:])
