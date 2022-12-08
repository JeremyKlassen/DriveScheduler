# Drive Scheduler
---
Drive Scheduler is a python project in development. It takes in a list of driver locations, and a list of client locations. It then calculates the optimal pickup pairings based on total distance or time.
---
### Minimum Viable Product
The first iteration's features are:

- A SQLite database that users can input data to, from the script. It has 4 tables (clients, drivers, distances and API keys).
- The script will consume 2 APIs. One that will convert an address/location string into GPS coordinates, and one that will return drive distances between each driver coordinates (one) and all the listed clients' coordinates (many).
- Create an algorithm that calculates and outputs a list of Driver/Client pairings that collectively require the least amount of drive distance for each client to be picked up.
---
### Additional Features (in order of need) to include in future interations.
- Optionally outputs a list based on drive time instead of drive distance.
- Ability to set specific driver/client pairs and exclude specific drivers or clients before calculating a schedule.
- Read data into database from .csv or spreadsheet files.
- Expand the algorithm
    - Calculates optimal drives that also average out mileage per driver over a week.
- GUI for Pythonista (IOS). So that the script can run from a cellphone.