from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dbhelper import AprsDB

origins = [
    "*"
]

aprs = FastAPI()
aprs.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@aprs.get("/packets")
async def root():
    db = AprsDB()
    return db.getLastNPackets(100)