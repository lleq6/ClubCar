# Project CS436 By Baboon Team

class Address:
    Firstname = ""
    Lastname = ""
    StreetAddress = ""
    State = ""
    City = ""
    ZipCode = ""

    def ToString(self):
        return f"{self.Firstname} {self.Lastname}\n{self.StreetAddress}\n{self.City} {self.ZipCode}\n{self.State}"

    def IsEmpty(self):
        return self.Firstname == "" and self.Lastname == "" and self.StreetAddress == "" and self.State == "" and self.City == "" and self.ZipCode == ""