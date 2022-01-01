import sys
import solution_01



def main(argv):

    print("")
    print("Solution 1: ")
    print("     input: Maze 1")
    print("  expected: 7")
    print("    actual: {}".format(solution_01.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: Maze 2")
    print("  expected: 11")
    print("    actual: {}".format(solution_01.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: Maze 3")
    print("  expected: 13")
    print("    actual: {}".format(solution_01.solution([[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]])))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: Maze 4")
    print("  expected: 13")
    print("    actual: {}".format(solution_01.solution([[0, 0, 0, 1, 0],[0, 1, 0, 1, 0],[0, 1, 0, 1, 0],[1, 1, 0, 1, 0],[0, 0, 0, 0, 0],[0, 1, 1, 1, 1],[0, 1, 0, 0, 0],[0, 1, 0, 1, 0],[0, 0, 0, 1, 0]])))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: Maze 5")
    print("  expected: 17")
    print("    actual: {}".format(solution_01.solution([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]])))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: Maze 6")
    print("  expected: 21")
    print("    actual: {}".format(solution_01.solution([[0, 1, 0, 0, 0, 1, 0, 0, 0],[0, 1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1, 0],[0, 0, 0, 1, 0, 0, 0, 1, 0]])))
    print("")



if __name__ == "__main__":
    main(sys.argv[1:])
