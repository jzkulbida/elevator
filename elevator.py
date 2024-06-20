import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Elevator Simulator')
    parser.add_argument("--start", type=int, required=True, help="Starting floor number")
    parser.add_argument("--floors", required=True, help="Floors to visit (separated by comma), e.g.: 3,5,-1,0")
    args = parser.parse_args()

    # get the starting floor number
    start_floor = args.start

    # parse the "floors" argument and split it into one or more floors
    floors_to_visit = []
    splits = args.floors.split(',')
    parse_ok = True
    for i, f in enumerate(splits):
        try:
            floor_int = int(f)
            floors_to_visit.append(floor_int)
        except ValueError:
            print(f"*** Found invalid floor number in field #{i+1}: {f}")
            print(f"*** Please use comma separated integers")
            parse_ok = False
            break

    if not parse_ok:
        print (f"*** Error occurred in parsing 'floors' string: {args.floors}")
        exit(-1)

    if len(floors_to_visit) == 0:
        print("Warning: no floors to visit!")

    # construct the output string and compute total time
    travel_time_per_floor = 10
    output_floors = ""
    total_time = 0
    previous_floor = start_floor
    for current_floor in floors_to_visit:
        if previous_floor == current_floor:
            print(f"*** Warning: found repeated floors: {previous_floor},{current_floor}, ignoring one")
        else:
            output_floors += f",{current_floor}"
            total_time += travel_time_per_floor * abs(current_floor - previous_floor)
        previous_floor = current_floor

    # output results
    print(f"{total_time} {start_floor}{output_floors}")

