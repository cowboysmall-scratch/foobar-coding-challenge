import sys
import solution_01



def main(argv):

    print("")
    print("Solution 1: ")
    print("     input: \"<<>><\"")
    print("  expected: 4")
    print("    actual: {}".format(solution_01.solution("<<>><")))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: \">----<\"")
    print("  expected: 2")
    print("    actual: {}".format(solution_01.solution(">----<")))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: \"--->-><-><-->-\"")
    print("  expected: 10")
    print("    actual: {}".format(solution_01.solution("--->-><-><-->-")))
    print("")



if __name__ == "__main__":
    main(sys.argv[1:])
