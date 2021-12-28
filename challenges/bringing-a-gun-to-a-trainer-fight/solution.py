import sys
import solution_01



def main(argv):

    print("")
    print("Solution 1: ")
    print("     input: [3, 2], [1, 1], [2, 1], 4")
    print("  expected: 7")
    print("    actual: {}".format(solution_01.solution([3, 2], [1, 1], [2, 1], 4)))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: [300, 275], [150, 150], [185, 100], 500")
    print("  expected: 9")
    print("    actual: {}".format(solution_01.solution([300, 275], [150, 150], [185, 100], 500)))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: [2, 5], [1, 2], [1, 4], 11")
    print("  expected: 27")
    print("    actual: {}".format(solution_01.solution([2, 5], [1, 2], [1, 4], 11)))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: [23, 10], [6, 4], [3, 2], 23")
    print("  expected: 8")
    print("    actual: {}".format(solution_01.solution([23, 10], [6, 4], [3, 2], 23)))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: [1250, 1250], [1000, 1000], [500, 400], 10000")
    print("  expected: 196")
    print("    actual: {}".format(solution_01.solution([1250, 1250], [1000, 1000], [500, 400], 10000)))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: [10, 10], [4, 4], [3, 3], 5000")
    print("  expected: 739323")
    print("    actual: {}".format(solution_01.solution([10, 10], [4, 4], [3, 3], 5000)))
    print("")



if __name__ == "__main__":
    main(sys.argv[1:])
