import sys
import solution_01


def main(argv):

    print()
    print("Solution 1: ")
    print("     input: [1, 1]")
    print("  expected: 2")
    print("    actual: {}".format(solution_01.solution([1, 1])))
    print()

    print()
    print("Solution 1: ")
    print("     input: [1, 7, 3, 21, 13, 19]")
    print("  expected: 0")
    print("    actual: {}".format(solution_01.solution([1, 7, 3, 21, 13, 19])))
    print()

    print()
    print("Solution 1: ")
    print("     input: [3, 3, 2, 6, 6]")
    print("  expected: 1")
    print("    actual: {}".format(solution_01.solution([3, 3, 2, 6, 6])))
    print()

    print()
    print("Solution 1: ")
    print("     input: [1, 7, 21]")
    print("  expected: 3")
    print("    actual: {}".format(solution_01.solution([1, 7, 21])))
    print()



if __name__ == "__main__":
    main(sys.argv[1:])
