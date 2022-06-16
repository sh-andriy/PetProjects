import click
import custom_modules


def calculate_char(string):
    return custom_modules.unique_character_calculator(string)


@click.command()
@click.option("--string",
              "-s",
              type=str,
              cls=custom_modules.MutuallyExclusiveOption,
              help="Enter string and get amount of unique characters",
              mutually_exclusive=["file"])
@click.option("--file",
              "-f",
              type=click.Path(exists=True),
              cls=custom_modules.MutuallyExclusiveOption,
              help="Enter file.txt path and get amount of unique characters",
              mutually_exclusive=["string"])
def string_input(string=None, file=None):
    """Calculate unique characters from input data (string/file)"""
    if all([string is None, file is None]):
        print(
            click.style(
                "Error! - Enter some arguments...\nUse --help for more info",
                fg="red"))
    elif file is None:
        print(
            click.style(
                f"Unique characters in string '{string}' is {calculate_char(string)}",
                fg="green"))
    else:
        with open(file, "r") as raw_string:
            string = raw_string.read().replace("\n", " ")
            print(
                click.style(
                    f"Unique characters in file '{file}' is {calculate_char(string)}",
                    fg="green"))


if __name__ == "__main__":
    string_input()
