from hstest import *


class CliTest(StageTest):
    @dynamic_test()
    def test_1(self):

        main = TestedProgram()
        output = main.start("-h")

        solution = "h: true"

        len_output = sum(len(s) for s in output.split("\n"))

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len_output > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output + "You may have printed extra parameters!")

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following line in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_2(self):

        main = TestedProgram()
        output = main.start("--help", "-p")

        solution = "help: true\np: true"

        len_output = sum(len(s) for s in output.split("\n"))
        len_solution = sum(len(s) for s in solution.split("\n"))

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len_output > len_solution:
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output + "You may have printed extra parameters!")

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_3(self):

        main = TestedProgram()
        output = main.start("-l", "--create=file.txt", "--debug")

        solution = "l: true\ncreate: file.txt\ndebug: true"

        len_output = sum(len(s) for s in output.split("\n"))
        len_solution = sum(len(s) for s in solution.split("\n"))

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len_output > len_solution:
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output + "You may have printed extra parameters!")

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_4(self):

        main = TestedProgram()
        output = main.start("-l", "--save=", "-a")

        solution = "It seems you forget to specify argument!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output + "You may have printed extra parameters!")

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()


if __name__ == '__main__':
    CliTest().run_tests()
