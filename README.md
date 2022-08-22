# Gokomodo Python Test
by: Muhammad Fadlil Ismail

fadlil.ismail@gmail.com

# Problems : Toy Robot Simulator

Description

The application is a simulation of a toy robot moving on a square tabletop, of
dimensions 5 units x 5 units.

There are no other obstructions on the table surface.

The robot is free to roam around the surface of the table, but must be prevented from
falling to destruction. Any movement that would result in the robot falling from the table
must be prevented, however further valid movement commands must still be allowed.

Create an application that can read in commands of the following form:

PLACE X,Y,F MOVE LEFT RIGHT REPORT

PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH,
EAST or WEST.

The origin (0,0) can be considered to be the SOUTH WEST most corner.

The first valid command to the robot is a PLACE command, after that, any sequence of
commands may be issued, in any order, including another PLACE command. The
application should discard all commands in the sequence until a valid PLACE command
has been executed.

MOVE will move the toy robot one unit forward in the direction it is currently facing.
LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without
changing the position of the robot. REPORT will announce the X,Y and F of the robot.
This can be in any form, but standard output is sufficient.

A robot that is not on the table can choose the ignore the MOVE, LEFT, RIGHT and
REPORT commands.

Input can be from a file, or from standard input, as the developer chooses. Provide test
data to exercise the application.

Constraints

The toy robot must not fall off the table during movement. This also includes the initial
placement of the toy robot. Any move that would cause the robot to fall must be ignored.

Example Input and Output:

Example a PLACE 0,0,NORTH MOVE REPORT

Expected output:

0,1,NORTH

Example b PLACE 0,0,NORTH LEFT REPORT 

Expected output:

0,0,WEST

Example c PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT

Expected output:

3,3,NORTH

Deliverables :

- Source code (Python)
- Test Data
- Any test code.
It is not required to provide any graphical output showing the movement of the toy robot.

# Requirements
To run this python program, you need these programs:
1. Python 3.x
2. Command Prompt
3. Notepad or other IDEs

# How to run the program?
If you have several test cases and want to test them at the same time, you can follow these steps:
1. Open test.txt (using Notepad or other IDEs) and delete all its contents.
2. Write your test cases, one row for one test case.
3. Save and close test.txt.
4. Open Command Prompt and change the directory to program location.
5. Write this command inside Command Prompt to run the test cases: `python run_testcase.py`.
6. The program will display the test cases and the results (the last location and direction of the robot).

If you want to test the program but don't want to change the test.txt, simply just follow these steps:
1. Open Command Prompt and change the directory to program location.
2. Write this command inside Command Prompt: `python main.py`.
3. Write your order for the robot (example : PLACE 1,1,NORTH MOVE RIGHT MOVE LEFT MOVE RIGHT RIGHT REPORT)
4. Click enter to send the order to robot.
5. The program will diplay the last location and last direction of the robot.
