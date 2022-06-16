from report_monaco_f1.central_calculator import dir_path
from report_monaco_f1.central_calculator import print_report
import argparse


parser = argparse.ArgumentParser(description="Report of Monaco 2018 Racing")
parser.add_argument(
    "-f",
    "--files",
    type=dir_path,
    metavar="",
    required=True,
    help="Directory with files (abbreviation.txt; end.log; start.log)")

group_order = parser.add_mutually_exclusive_group()
group_order.add_argument(
    "-a",
    "--asc",
    action="store_false",
    help="Output report in ascending order (default)")
group_order.add_argument(
    "-d",
    "--desc",
    action="store_true",
    help="Output report in descending order")


parser.add_argument(
    "-D",
    "--driver",
    type=str,
    default=None,
    metavar="",
    help="Show racer statistic (example: 'Sebastian Vettel')"
)


args = parser.parse_args()


def main():
    if args.desc:
        print_report(
            args.files, descending=args.desc, driver=args.driver)
    else:
        print_report(args.files, driver=args.driver)
