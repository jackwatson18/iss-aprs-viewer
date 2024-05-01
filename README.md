# ISS APRS Viewer

An application for storing Automatic Packet Reporting System traffic by listening to the APRS-IS service. Filters traffic from APRS-IS and stores them in a database, which is accessible via a simple REST API. A simple front end is provided which uses Javascript and HTML. Meant to be deployed in a server environment using a traditional webserver like Nginx. Future work includes converting the backend to Go or Node Express, and adding SQLite3 support for the backend.
