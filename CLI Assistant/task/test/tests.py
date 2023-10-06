import os
from hstest import *


class CliTest(StageTest):
    @dynamic_test()
    def test_1(self):

        os.mkdir("super_folder")
        main = TestedProgram()
        output = main.start("--isFolder=super_folder")
        os.rmdir("super_folder")

        solution = "The super_folder is a folder!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_2(self):

        main = TestedProgram()
        output = main.start("--isFolder=fake_folder")

        solution = "It seems that some specified files don't exist!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_3(self):

        main = TestedProgram()
        output = main.start("--isFolder=main.js")

        solution = "The main.js is not a folder!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_4(self):

        size = os.path.getsize("main.js")

        main = TestedProgram()
        output = main.start("--size=main.js")

        solution = f"The size of the specified files is {size} kilobytes"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_5(self):

        with open("data.txt", "w") as file:
            file.write("Some text of data")

        size = os.path.getsize("main.js") + os.path.getsize("data.txt")

        main = TestedProgram()
        output = main.start("--size=main.js-data.txt")

        os.remove("data.txt")

        solution = f"The size of the specified files is {size} kilobytes"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_6(self):

        main = TestedProgram()
        output = main.start("--size=fake.txt")

        solution = f"It seems that some specified files don't exist!"

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if len(output.split("\n")[-2]) > len(solution):
            return CheckResult.wrong(f"The output of your program is longer than the expected output: \n" + solution +
                                     "\nYour output is:\n" + output)

        if solution not in output:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + solution +
                                     "\nBut your output is:\n" + output)

        return CheckResult.correct()

    @dynamic_test()
    def test_7(self):

        main = TestedProgram()
        output = main.start("--content")

        listdir_from_js = sorted(output.split("\n")[:-1])
        listdir = sorted(os.listdir())

        if len(output) == 0:
            return CheckResult.wrong("It seems that your program does not print anything to the console!")

        if listdir_from_js != listdir:
            return CheckResult.wrong(f"Expected to see the following lines in the console: \n" + "\n".join(listdir) +
                                     f"\nBut your output is:\n" + "\n".join(listdir_from_js))

        return CheckResult.correct()


if __name__ == '__main__':
    CliTest().run_tests()
