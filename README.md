# Elevator Simulator 
### by Jie Kulbida

## Requirements:
Python must be installed on the OS 

## Usage: 
python elevator.py start=[start floor num] floors=[floors to visit]

## Arguments:
[start floor num]: an integer specifying the starting floor

[floors to visit]: a comma separated list of numbers, specifying the floors to visit

Note: <floors to visit> should not contain white space, unless the entire string is surrounded by quotes

## Example:

python elevator.py start=20 floors=4,7,-6,20

or

python elevator.py start=20 floors="4, 7, -6, 20"

## Output:
[Total travel time] [start floor num] [floors to visit]

For the example above, output: 580 20,4,7,-6,20

## Assumptions:

1. Each floor must be identified with an integer value (0, positive or negative)
2. Each floor number must be within the range of [min_floor_number, max_floor_number]
3. For demonstration, min_floor_number and max_floor_number are constants set to -100 and 200, respectively 
4. min_floor_number and max_floor_number should be modified to reflect the actual elevator being simulated
5. If any of the conditions 1-4 above are not met, program will abort with error
6. Repeating floor numbers (in succession) will raise warning, but output will be generated with repeated floors removed
7. If no errors in arguments, and no valid floors are received, a warning will be raised, but output will be generated with: 0 [starting_floor]