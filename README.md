# Drive Scheduler
## Jeremy Klassen
---
Drive Scheduler is a python project in development. It takes in a list of drivers locations, and a list of clients locations and then calculates the optimal pickup pairings based on total distance or time.
---
### Minimum Viable Product features
The minimum features this project will include are:

- A SQLite database that you create and input data from the script. It has 3 tables (clients, drivers, and API keys).
- The script will consume 2 APIs one that will convert an address string into GPS coordinates, and one that will return drive distances between each driver coordinates and the client coordinates (one to many).
- Calculate and output a list of Driver/Client pairings that collectively require the least amount of drive distance.

---
### Potential Additional Features (in order of need)
- optionally outputs a list based on drive time instead of drive distance.
- GUI for Pythonista (IOS). So that the script can be optimally run from a cellphone.
- Read data into database from .csv or spreadsheet files.
- Ability to set specific driver/client pairs before calculating a schedule.