from datetime import datetime, timedelta
import sys
import os


def log_reader(file_location, data_base, time):
    """Update dict data_base by log file"""
    with open(file_location, "r") as log:
        for log_data in log:
            racer_id = log_data[:3]
            racer_start_time = log_data[3:].rstrip().split("_")
            racer_start_time_str = f"{racer_start_time[0]} {racer_start_time[1]}"
            data_base[racer_id][time] = datetime.strptime(
                racer_start_time_str, '%Y-%m-%d %H:%M:%S.%f')
    return data_base


def build_report(folder_path, descending=False):
    """
    Building dictionary from 'Report of Monaco 2018 Racing'
    from files abbreviations.txt; start.log; end.log and
    creating dictionary with this structure:

    ID: dict
    ├── full_name: str
    ├── car: str
    ├── start_time: datetime.datetime
    ├── end_time: datetime.datetime
    └── lap_time: datetime.timedelta

    At the end sorting by lap_time
    """
    data_base = {}
    try:
        with open(f"{folder_path}/abbreviations.txt", "r") as abbreviations:
            for racer_data in abbreviations:
                racer_data = racer_data.rstrip().split("_")
                temp_dict = {
                    racer_data[0]: {
                        "full_name": racer_data[1],
                        "car": racer_data[2]}}
                data_base.update(temp_dict)

        data_base = log_reader(f"{folder_path}/start.log", data_base, "start_time")
        data_base = log_reader(f"{folder_path}/end.log", data_base, "end_time")

    except FileNotFoundError:
        sys.exit("\nError - Files not found in directory!\n")

    for racer_id, racer_data in data_base.items():
        lap_time = racer_data["end_time"] - racer_data["start_time"]
        if lap_time.days >= 0:
            racer_data["lap_time"] = lap_time
        else:
            racer_data["lap_time"] = timedelta(days=9999)

    data_base = {
        k: v for k,
        v in sorted(
            data_base.items(),
            key=lambda x: x[1]["lap_time"],
            reverse=descending)}

    return data_base


def print_racer(data_base, driver):
    """Print data about one racer"""
    present_in_list = False
    for racer_id, racer_data in data_base.items():
        if racer_data["full_name"] == driver:
            present_in_list = True
            racer_lap_time = racer_data["lap_time"]
            if racer_lap_time.days == 9999:
                racer_lap_time = "Disqualified!"
            else:
                racer_lap_time = str(racer_lap_time)[:-3][3:]
            print(f"""
                    {"-" * 35}
                    ID: {racer_id}
                    Full name: {racer_data["full_name"]}
                    Car: {racer_data["car"]}

                    Best lap:
                        start - {racer_data["start_time"].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}
                        end   - {racer_data["end_time"].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}

                    Lap result: {racer_lap_time}
                    {"-" * 35}
                    """)

    if present_in_list is False:
        sys.exit("\nError - Driver name not found!\n")


def print_line():
    print("-" * 79)


def print_disqualified_line(counter, limit):
    if counter == limit:
        print_line()


def print_all(data_base, descending):
    """Print list for all racers in given order"""
    if descending:
        top_counter = len(data_base)
    else:
        top_counter = 1
    print(
        "{}  {:<25}\t  {:<30}  {}".format(
            "#",
            "Racer full name",
            "Car",
            "Best lap time"))
    print_line()
    for racer_id, racer_data in data_base.items():
        racer_name = racer_data["full_name"]
        racer_car = racer_data["car"]
        racer_lap_time = racer_data["lap_time"]
        if racer_lap_time.days == 9999:
            racer_lap_time = "Disqualified!"
        else:
            racer_lap_time = str(racer_lap_time)[:-3][3:]
        print(
            f"{top_counter}. {racer_name:<25}\t| {racer_car:<30}| {racer_lap_time}")

        if descending:
            top_counter -= 1
            print_disqualified_line(top_counter, 15)
        else:
            print_disqualified_line(top_counter, 15)
            top_counter += 1


def print_report(folder_path, descending=False, driver=None):
    """
    Generating beautiful output for "build_report" function
    """
    data_base = build_report(folder_path, descending=descending)
    if driver is None:
        print_all(data_base, descending)
    else:
        print_racer(data_base, driver)


def dir_path(string):
    """Check if entered folder is PATH"""
    try:
        if os.path.isdir(string):
            return string
        else:
            raise NotADirectoryError
    except NotADirectoryError:
        sys.exit("\nError - Path is not directory or does not exist!\n")
