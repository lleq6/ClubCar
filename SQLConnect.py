# Project CS436 By Baboon Team

import sqlite3

class SQLConnect:
    def GetConnect():
        return sqlite3.connect("Database/CarForRent.db")