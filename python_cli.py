import os
import sys


def display_tool_name():
    print("         **************************")
    print("         *    COMMANDLINE TOOL    *")
    print("         **************************")


def show_tool_usage():
    print("")
    print("0 = For exiting the tool")
    print("1 = Command One")
    print("2 = Command Two")
    print("3 = All the above")
    print("")


def command_one():
    print("         **********************")
    print("         *     Command One    *")
    print("         **********************")
    os.system("echo 'Executed command one....!'")


def command_two():
    print("         **********************")
    print("         *     Command Two    *")
    print("         **********************")
    os.system("echo 'Executed command two....!'")


def run_all_cli_options():
    command_one()
    command_two()


def show_user_confirmation():
    print("\nDo You Want to execute any other option in CLI Tool?\n")
    print("Please press (yes/no) or (y/n)\n")
    option = input()
    if "yes" in option or "y" in option:
        status = True
    else:
        status = False
    return status


def exit_cli_tool():
    print("\nExiting CLI Tool")
    sys.exit()


def show_invalid_option_message():
    print("Invalid Option..!")


def launch_cli():
    try:
        loop_flag = True
        user_confirmation_flag = False

        display_tool_name()
        show_tool_usage()
        try:
            options = int(input("Enter the option: \n" ))
        except ValueError:
            print("Error! This is not a number. Try again.")
            launch_cli()

        switcher = {
            0: exit_cli_tool,
            1: command_one,
            2: command_two,
            3: run_all_cli_options
        }

        while loop_flag:
            if options == 0:
                loop_flag = False
                exit_cli_tool()

            selected_func = switcher.get(options, lambda: "Noting")
            selected_func()

            if loop_flag:
                user_confirmation_flag = show_user_confirmation()
            else:
                loop_flag = False

            if user_confirmation_flag:
                show_tool_usage()
                try:
                    options = int(input("Enter the option: \n" ))
                except ValueError:
                    print("Error! This is not a number. Try again.")
                    launch_cli()
                user_confirmation_flag = False
            else:
                loop_flag = False
                exit_cli_tool()

    except KeyboardInterrupt:
        exit_cli_tool()


launch_cli()
