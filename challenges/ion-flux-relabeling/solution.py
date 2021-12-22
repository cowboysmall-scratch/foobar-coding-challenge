import sys
import solution_01
import solution_02



def main(argv):

    print()
    print("Solution 1: ")
    print("    height: 3")
    print("     input: [7, 3, 5, 1]")
    print("  expected: [-1, 7, 6, 3]")
    print("    actual: {}".format(solution_01.solution(3, [7, 3, 5, 1])))
    print()

    print()
    print("Solution 2: ")
    print("    height: 3")
    print("     input: [7, 3, 5, 1]")
    print("  expected: [-1, 7, 6, 3]")
    print("    actual: {}".format(solution_02.solution(3, [7, 3, 5, 1])))
    print()

    print()
    print("Solution 1: ")
    print("    height: 5")
    print("     input: [19, 14, 28]")
    print("  expected: [21, 15, 29]")
    print("    actual: {}".format(solution_01.solution(5, [19, 14, 28])))
    print()

    print()
    print("Solution 2: ")
    print("    height: 5")
    print("     input: [19, 14, 28]")
    print("  expected: [21, 15, 29]")
    print("    actual: {}".format(solution_02.solution(5, [19, 14, 28])))
    print()



    print()
    print()
    print("Detailed comparison of the results from both solutions for height 10:")
    print()

    h  = 10
    q  = list(range(1, 2**h))

    p1 = solution_01.solution(h, q)
    p2 = solution_02.solution(h, q)

    m  = [(v0, v1, v2) for (v0, v1, v2) in zip(q, p1, p2) if v1 != v2]

    print("         height: {}".format(h))
    print("          total: {}".format(len(q)))
    print("     mismatched: {}".format(len(m)))
    if m:
        print("     mismatches: {}".format(m))
    print()



if __name__ == "__main__":
    main(sys.argv[1:])
