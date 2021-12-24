import sys
import solution_01



def main(argv):

    print()
    print("Solution 1: ")
    print("     input: [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]")
    print("  expected: 7")
    print("    actual: {}".format(solution_01.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])))
    print()

    print()
    print("Solution 1: ")
    print("     input: [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]")
    print("  expected: 11")
    print("    actual: {}".format(solution_01.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])))
    print()



if __name__ == "__main__":
    main(sys.argv[1:])
