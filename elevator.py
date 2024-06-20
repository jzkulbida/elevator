import argparse
import sys


def print_usage():
    print(f"Usage: {sys.argv[0]} start=<starting floor> floor=<floors to visit>")


# ==================================================================================
# Not used - Leverage the Python argparse library (must specify arguments using --start and --floors)
# ==================================================================================
"""
def get_arguments_using_argparser():
    parser = argparse.ArgumentParser(description='Elevator Simulator')
    parser.add_argument("--start", type=int, required=True, help="Starting floor number")
    parser.add_argument("--floors", required=True, help="Floors to visit (separated by comma), e.g.: 3,5,-1,0")
    args = parser.parse_args()

    # get the starting floor number
    start = args.start

    # parse the "floors" argument and split it into one or more floors
    floors = args.floors
    return start, floors
"""


# ==================================================================================
# Extract attribute-value pairs of interest (start, floors) from command-line arguments
# ==================================================================================

def get_arguments_using_avps():
    start = 0
    floors = ""

    error_occurred = False
    start_keyword = "start"
    floors_keyword = "floor"
    if len(sys.argv) < 3:
        print(f"Expecting 2 arguments, but got {len(sys.argv) - 1}")
    else:
        for arg in sys.argv[1:]:
            # arg should be an attribute/value pair separated by "="
            fields = arg.split('=')
            if len(fields) == 2:
                key = fields[0]
                value = fields[1]
                if key == start_keyword:
                    try:
                        start = int(value)
                    except ValueError:
                        print(f'*** Error: Value for starting floor is not an integer: {arg}')
                        error_occurred = True
                        break
                elif key == floors_keyword:
                    floors = value
                else:
                    print(f"Unknown key found in argument: {arg} - ignored")
            else:
                print(f'***Warning: each argument should contain one "=". Ignoring "{arg}"')
                error_occurred = True
                break

    return error_occurred, start, floors


# ===================================================
# Elevator Simulator Entry point
# ===================================================

if __name__ == '__main__':

    arg_error, start_floor, floors_string_orig = get_arguments_using_avps()

    if arg_error:
        print(f"*** Error in parsing arguments")
        print_usage()
        exit(-1)

    """
    As an alternative, here is an implementation using argparser package
    start_floor, floors_string = get_arguments_using_argparser()
    """

    # extract and validate floor numbers in floors_string
    floors_to_visit = []
    # replace ',' with space, so that we can tolerate leading, trailing, or repeating commas
    floors_string = floors_string_orig.replace(",", " ")

    # iterate the split fields, and append floor number to floors_to_visit
    splits = floors_string.split()
    parse_ok = True
    max_floor_number = 200
    min_floor_number = -100
    for i, f in enumerate(splits):
        try:
            floor_int = int(f)
            if min_floor_number <= floor_int <= max_floor_number:
                floors_to_visit.append(floor_int)
            else:
                print(f"Error: floor number must be within the range: [{min_floor_number}, {max_floor_number}]: {f}")
                parse_ok = False
                break
        except ValueError:
            print(f"*** Error: Found invalid floor number in field #{i + 1}, found {f}")
            parse_ok = False
            break

    # handle exceptions
    if not parse_ok:
        print(f"*** Error occurred in parsing 'floors' string: {floors_string_orig}")
        print_usage()
        exit(-1)

    if len(floors_to_visit) == 0:
        print("Warning: no floors to visit!")
        print_usage()

    # construct the output string and compute total time
    travel_time_per_floor = 10
    output_floors = ""
    total_time = 0
    previous_floor = start_floor
    for current_floor in floors_to_visit:
        if previous_floor == current_floor:
            print(f"*** Warning: found repeating floors: {previous_floor},{current_floor}, keeping one")
        else:
            output_floors += f",{current_floor}"
            total_time += travel_time_per_floor * abs(current_floor - previous_floor)
        previous_floor = current_floor

    # output results
    print(f"{total_time} {start_floor}{output_floors}")
