# ISS APRS Viewer

An application for storing and viewing Automatic Packet Reporting System traffic by listening to the APRS-IS service. Filters traffic from APRS-IS and stores them in a database, which then is visualized in a simple webapp. Postgres is used to store data persistently, python is used for the backend, and javascript is used to create the front end interface. Postgres is probably overkill for this project and will eventually be changed to Sqlite3. Future work includes converting the backend to Go or Node Express.
