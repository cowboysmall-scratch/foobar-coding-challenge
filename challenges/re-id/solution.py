import sys
import solution_01



def main(argv):

    print()
    print("Solution 1: ")
    print("     input: 0")
    print("  expected: 23571")
    print("    actual: {}".format(solution_01.solution(0)))
    print()

    print()
    print("Solution 1: ")
    print("     input: 3")
    print("  expected: 71113")
    print("    actual: {}".format(solution_01.solution(3)))
    print()



if __name__ == "__main__":
    main(sys.argv[1:])
