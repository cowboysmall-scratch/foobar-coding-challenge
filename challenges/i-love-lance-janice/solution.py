import sys
import solution_01



def main(argv):

    print("")
    print("Solution 1: ")
    print("     input: \"vmxibkgrlm\"")
    print("  expected: \"encryption\"")
    print("    actual: \"{}\"".format(solution_01.solution("vmxibkgrlm")))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: \"wrw blf hvv ozhg mrtsg'h vkrhlwv?\"")
    print("  expected: \"did you see last night's episode?\"")
    print("    actual: \"{}\"".format(solution_01.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")))
    print("")

    print("")
    print("Solution 1: ")
    print("     input: \"Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!\"")
    print("  expected: \"Yeah! I can't believe Lance lost his job at the colony!!\"")
    print("    actual: \"{}\"".format(solution_01.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")))
    print("")



if __name__ == "__main__":
    main(sys.argv[1:])
