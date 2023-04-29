# Project CS436 By Baboon Team

from tkinter import messagebox

class Cart:
    Items = {}
    Periods = {}

    def Add(self, Car, Period):
        try:
            self.Items.update({ Car.Id : Car })
            self.Periods.update({ Car.Id : Period })
        except Exception as ex:
            messagebox.showerror("Club Car", f"Unexpected {ex=}")
            return

    def Remove(self, Car):
        try:
            self.Items.pop(Car.Id)
            self.Periods.pop(Car.Id)
        except Exception as ex:
            messagebox.showerror("Club Car", f"Unexpected {ex=}")
            return

    def Clear(self):
        try:
            self.Items.clear()
            self.Periods.clear()
        except Exception as ex:
            messagebox.showerror("Club Car", f"Unexpected {ex=}")
            return