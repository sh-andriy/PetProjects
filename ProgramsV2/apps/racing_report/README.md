# Report of Monaco 2018 Racing
This is a data parsing/procesing/outputing package, which get folder path (**IMPORTANT! - in directory must be files: abbreviations.txt; start.log; end.log**).
And generate beautiful output for all racers in descending and ascending [_default_] order.
Have ability to print full data about racer by his name.<br />
## How to use
Examples:
- `python <your_file.py> --files <folder_path> [--asc | --desc]`
- `python <your_file.py> --files <folder_path> driver “Sebastian Vettel”`
```
usage: __init__.py [-h] -f  [-a | -d] [-D]

optional arguments:
  -h, --help      show this help message and exit
  -f , --files    Directory with files (abbreviation.txt; end.log; start.log)
  -a, --asc       Output report in ascending order (default)
  -d, --desc      Output report in descending order
  -D , --driver   Show racer statistic (example: 'Sebastian Vettel')
```