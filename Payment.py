# Project CS436 By Baboon Team

class Payment:
    MCardHoldername = ""
    MCardNumber = ""
    MExpirationMonth = ""
    MExpirationYear = ""
    MCVC = ""
    VCardHoldername = ""
    VCardNumber = ""
    VExpirationMonth = ""
    VExpirationYear = ""
    VCVC = ""
    TransactionId = ""

    def IsEmpty(self, Type):
        return (Type == 1 and self.VCardHoldername == "" and self.VCardNumber == "" and self.VExpirationMonth == "" and self.VExpirationYear == "" and self.VCVC == "") or (Type == 2 and self.MCardHoldername == "" and self.MCardNumber == "" and self.MExpirationMonth == "" and self.MExpirationYear == "" and self.MCVC == "")
