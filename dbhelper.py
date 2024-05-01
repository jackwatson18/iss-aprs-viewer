import sqlite3
import psycopg2, psycopg2.extras


class AprsDB():
    def __init__(self):
        self.connection = psycopg2.connect(
            cursor_factory = psycopg2.extras.RealDictCursor,
            host = "localhost",
            database = "aprs_stuff",
            user = "aprs_user",
            password = "password"
        )

        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS aprs (id SERIAL PRIMARY KEY, raw_packet TEXT)")
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def getAllPackets(self):
        self.cursor.execute("SELECT * FROM aprs")
        return self.cursor.fetchall()

    def getLastNPackets(self,n):
        # Get last n packets. ex: if n = 10, return last 10 packets
        n = int(n)
        self.cursor.execute("SELECT * FROM (SELECT * FROM aprs ORDER BY id DESC LIMIT %i) sub ORDER BY id ASC" % n)
        return self.cursor.fetchall()

    def addPacket(self, packet):
        data = [packet]
        self.cursor.execute("INSERT INTO aprs (raw_packet) VALUES (%s)", data)
        self.connection.commit()
