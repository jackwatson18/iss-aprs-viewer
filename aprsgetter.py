import aprslib
from dbhelper import AprsDB

def callback(packet):
    if "RS0ISS*" in str(packet):
        db = AprsDB()
        print(str(packet))
        db.addPacket(str(packet))



if __name__ == "__main__":
    print("Connecting to APRS-IS...")
    AIS = aprslib.IS("N0CALL")
    AIS.connect()
    print("Connected to APRS-IS!")
    # by default `raw` is False, then each line is ran through aprslib.parse()
    AIS.consumer(callback, raw=True)
