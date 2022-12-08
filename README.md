# Drive Scheduler
---
Drive Scheduler is a python project in development. It will calculate optimal driver/client pairings based on their home locations. It is split into 3 main scripts.

1 - coords - This script reads the address fields in the clients and drivers tables in the spreadsheet. It then sends API requests to get the Coordinates of that location and writes them back into the spreadsheet.

2 - distance - This script reads the coordinates from each driver and client. It then calculates the distance between all clients and drivers, and writes them to the spreadsheet.

3 - calculator - This Jupyter notebook takes all the distances and calculates the optimal drives.
---
### Possible future additions (in order of implementation)

- Can calculate drives based on time instead of distance.
- Allow user to set specific client/driver pairings before calculation.
- Calculate a weeks worth of drives.
- Track rough mileage allocated to drivers over time.
- Calculate optimal pairings for a drive home from a specific location.