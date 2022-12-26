# Property of JargonBots
# Written by Armaan Kapoor on 12-26-2022

import os
import random
import string
import time

from api_request_handler import openai_request


def request_formatter():
    print("\n")
    print('"LazyDev"\n\n')
    print("Advanced Python Code Generation Powered by GPT-3 Davinci-003.\n\n")

    in_args = None
    out_args = None
    time.sleep(1)  # prevent spamming the USER and API
    grabtxt = input(
        "Describe A Function and GPT-3 will program it! \n\tex 1. 'Takes a list and returns the sum of the list'\n\tex 2.'Takes in a temprature in degres celcius and converts to degres kelvin' \n\n ----> "
    )
    time.sleep(0.5)

    in_args_flag = input("Would you like to specify input arguements? \nY/N\n")
    time.sleep(0.5)

    if in_args_flag == "Y" or in_args_flag == "y" or in_args_flag == "yes" or in_args_flag == "Yes":
        in_args = input(
            "Describe the input arguements in natural language \n\tex. 'an array of integers length N, and a target integer\n\n ---->"
        )
    time.sleep(0.25)
    out_args_flag = input("Would you like to specify output arguements? \nY/N\n")
    time.sleep(0.25)

    if out_args_flag == "Y" or out_args_flag == "y" or out_args_flag == "yes" or out_args_flag == "Yes":
        out_args = input(
            "Describe the output arguements in natural language \nex. 'the position of the indices of two integers from the array that sum to target\n\n ---->"
        )
    time.sleep(0.25)

    resstr = (
        "\nWrite Python Function"
        + grabtxt
        + "2*\n"
        + "The Input Arguments: "
        + str(in_args)
        + "\n"
        + "The Output Arguments: "
        + str(out_args)
        + "\n"
        + "def function_name():"
        + "\n"
        + "    # Your code here"
        + "\n"
        + "    return"
        + "\n"
    )
    # resstr = '\nWrite a Python program that ' + grabtxt + "." + '2*\n' + 'The Input Arguments: ' + str(in_args) + '\n' + 'The Output Arguments: ' + str(out_args) + '\n' + '#'
    # resstr = '\nWrite a helm chart for a webserver and MySQL database'
    time.sleep(0.25)
    return resstr


def ask_to_make_changes(generated_function):
    changes_flag = input("Would you like to make changes to the code? \nY/N\n")
    changes = None
    time.sleep(0.25)
    if changes_flag == "Y" or changes_flag == "y" or changes_flag == "yes" or changes_flag == "Yes":
        working_flag = input("Does the function work as intended on test cases? \nY/N\n")
        if working_flag == "Y" or working_flag == "y" or working_flag == "yes" or working_flag == "Yes":
            still_make_change_flag = input(
                "Great! The function is working. Would you still like to make changes? \nY/N\n"
            )
            if (
                still_make_change_flag == "Y"
                or still_make_change_flag == "y"
                or still_make_change_flag == "yes"
                or still_make_change_flag == "Yes"
            ):
                changes = (
                    "change the function, "
                    + input(
                        "What changes would you like to make to the code? \n\tex 1. Reduce the worst case time complexity of a loop \n\tex 2. reformat or use a different alogrithm \n\n ---->"
                    ).strip()
                )
            else:
                print("Exiting LazyDev!")
        else:
            provide_case_flag = input(
                "Would you like to provide an example of a test case and its matching desired output? \nY/N\n"
            )
            if (
                provide_case_flag == "Y"
                or provide_case_flag == "y"
                or provide_case_flag == "yes"
                or provide_case_flag == "Yes"
            ):
                test_case = input("Provide a test case: ").strip()
                desired_output = input("Provide the desired output: ").strip()
                changes = (
                    "Fix the function so that it passes the test case "
                    + test_case
                    + " with the desired output "
                    + desired_output
                )
            else:
                misc_prblm = input(
                    "Describe the problem\n\tex. The function returned the error 'Exceeded Max Recursion Depth'\n\n ---->"
                ).strip()
                changes = "There was a problem with the function. " + misc_prblm

    else:
        print("Exiting LazyDev!")
    return changes


def main():
    formatted = request_formatter()
    resp = openai_request(formatted)
    ret = resp.return_tokens(temprature=0, max_tokens=1000, frequency_penalty=0.0, stop=None)

    print(10 * "\n")
    print(ret)
    print(10 * "\n")

    time.sleep(2)

    changes = ask_to_make_changes(ret)

    if changes != None:
        resp_w_changes = openai_request("The code so far:\n" + ret + "\n" + str(changes) + ":\n")
        ret2 = resp.return_tokens(temprature=0, max_tokens=3000, frequency_penalty=0.0, stop=None)
    else:
        ret2 = ret

    print(formatted + "/n" + str(changes) + ":")
    print(5 * "\n")
    print(ret2)
    print(5 * "\n")

    output_dir = "output"
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    output_file = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    outfile = open(f"{output_dir}/{output_file}.txt", "wt")
    outfile.write(ret2)
    outfile.close()

    # make an interactive function to program builder.


main()
