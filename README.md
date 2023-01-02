# Drive Scheduler
---
Drive Scheduler is a python collection of Jupyter Notebooks intended for use by non-coding users on mobile devices. It calculates driver/client pairings with a greedy algorithm using distances between clients, drivers, and locations.  It then creates drive schedules based on those pairings.

1 - Setup.ipynb - This script has a cell that installs dependancies for use with the Carnets app (an IOS Jupyter Notebook app). It also has a cell that calculates and writes distances between every 1 to 1 combination of drivers/clients into data.xlsx using the harversine formula.

2 - MorningDrives.ipynb - This script creates pickup schedules based on the home locations of drivers and clients. It reads info from data.xlsx. Based on that info it allows you to deselect any clients or drivers that should not be on the Schedule. In the last 2 cells you can create and refresh schedules. The first cell creates a more varied but less efficient schedule, and the second creates a more consistent, and efficient schedule.

3 - DrivesFromLocation.ipynb - This script creates dropoff schedules for clients that are all leaving the same location. It reads info from data.xlsx. It then allows you to choose the departing location and deselect any clients or drivers that should not be on the Schedule. In the last 2 cells you can create and refresh schedules. The first cell creates a more varied but less efficient schedule, and the second creates a more consistent, and efficient schedule.

---
### Key Features

- Creates driver schedules from homes to a location as well as from a location to a home.
- Can be used on PC, Mac, and IOS (through use of the Carnets app). Android has not been tested.
- Security. The coords.py standalone script (converts address strings to coordinates and writes them to your data.xlsx file) is the only file that connects to an external api. All others access, manipulate and display data from data.xlsx strictly on your device.
- Quick - Designed for users to be able to quickly generate new schedules at a moments notice.