
import solution_01
import solution_02

print()
print("Solution 1: ")
print("    height:  3")
print("     input:  [7, 3, 5, 1]")
print("  expected:  [-1, 7, 6, 3]")
print("    actual: ", solution_01.solution(3, [7, 3, 5, 1]))
print()

print()
print("Solution 2: ")
print("    height:  3")
print("     input:  [7, 3, 5, 1]")
print("  expected:  [-1, 7, 6, 3]")
print("    actual: ", solution_02.solution(3, [7, 3, 5, 1]))
print()

print()
print("Solution 1: ")
print("    height:  5")
print("     input:  [19, 14, 28]")
print("  expected:  [21, 15, 29]")
print("    actual: ", solution_01.solution(5, [19, 14, 28]))
print()

print()
print("Solution 2: ")
print("    height:  5")
print("     input:  [19, 14, 28]")
print("  expected:  [21, 15, 29]")
print("    actual: ", solution_02.solution(5, [19, 14, 28]))
print()


print()
print()
print("Detailed comparison of the results from both solutions:")
print()

h  = 13
v  = [i for i in range(1, 2**h)]

p1 = solution_01.solution(h, v)
p2 = solution_02.solution(h, v)

m  = [(i, v1) for i, (v1, v2) in enumerate(zip(p1, p2)) if v1 != v2]

print("         height: ", h)
print("          total: ", len(v))
print("     mismatched: ", len(m))
if m:
    print("     mismatches: ", m)
print()
