import os
import requests
from maprequest import MapRequest
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar

BLABLACARAPI_KEY = os.getenv("BLABLACAR_API")
BLABLA_ENDPOINT = "https://public-api.blablacar.com/api/v3/trips"


class BlaBlaCar:

    def locale_details(self):
        df_locale = pd.read_excel("locale_sheet.xlsx", index_col=None, engine='openpyxl')
        get_country_input = input("Enter the Locale Settings Here ")
        if get_country_input in df_locale["Country"].tolist():
            locale = str(list(df_locale[df_locale["Country"] == get_country_input]["Locale"])[0])
            currency = str(list(df_locale[df_locale["Country"] == get_country_input]["Default Currency"])[0])
        return locale, currency

    def get_blablacar_json(self):
        start_date_local = str(self.get_calender())
        end_date_local = str(self.get_calender())
        locale, currency = self.locale_details()
        coordinate = MapRequest()
        from_coordinate = getattr(coordinate, 'from_coordinate')
        to_coordinate = getattr(coordinate, 'to_coordinate')

        params_blabla = {
            "key": BLABLACARAPI_KEY,
            "from_coordinate": from_coordinate,
            "to_coordinate": to_coordinate,
            "locale": locale,
            "currency": currency,
            "start_date_local": start_date_local + "T00:00:00",
            "end_date_local": end_date_local + "T23:59:59",
            "count": self.get_trips,
            "requested_seats": self.get_seats
        }
        response = requests.get(BLABLA_ENDPOINT, params=params_blabla)
        trip_data = response.json()
        return trip_data

    def get_calender(self):
        def cal_done():
            top.withdraw()
            root.quit()

        root = Tk()
        root.withdraw()
        top = tk.Toplevel(root)
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1")
        cal.pack(fill="both", expand=True)
        tk.Button(top, text="ok", command=cal_done).pack()
        selected_date = None
        root.mainloop()
        return cal.selection_get()

    @property
    def get_seats(self) -> int:
        seats = 1
        seats_list = np.arange(2, 9)
        selection_list = ["yes", "no"]
        while True:

            try:
                seat_selection = input("Want to search for more than 1 seat ? (Yes/No) ").lower()
                if seat_selection not in selection_list:
                    raise Exception("Please enter Yes or No")
            except Exception as e:
                print("Yes or NO")
                continue
            if seat_selection == "yes":
                try:
                    seats = int(input("Enter number of seats you want to search for (between 1 and 8)"))
                except ValueError:
                    print("Sorry didn't understand it, please enter a number of seats between 1 and 8")
                    continue
                if seats not in seats_list:
                    print("Please enter seat number between 1 and 8")
                else:
                    break
            else:
                break
        return seats

    def get_address_details(self, main_trips_data, i, j):
        address = main_trips_data["trips"][i]['waypoints'][j]['place']['address']
        place = main_trips_data["trips"][i]['waypoints'][j]['place']['city']
        date_time = main_trips_data["trips"][i]['waypoints'][j]['date_time']
        return address, place, date_time

    def trips_extract(self, main_trips_data, no_of_trips_available):
        trip_main_list = []
        for i in range(0, no_of_trips_available):
            trip_main_dict_temp = {"trip_number": i + 1, "price": main_trips_data["trips"][i]['price']['amount'] + " " + \
                                                                  main_trips_data["trips"][i]['price']['currency']}

            for j in range(0, 2):
                if j == 0:
                    from_address, from_location, date_time = BlaBlaCar().get_address_details(main_trips_data, i, j)
                    trip_main_dict_temp["from_address"] = from_address
                    trip_main_dict_temp["from_location"] = from_location
                    trip_main_dict_temp["from_date_time"] = date_time

                if j == 1:
                    to_address, to_location, date_time = BlaBlaCar().get_address_details(main_trips_data, i, j)
                    trip_main_dict_temp["to_address"] = to_address
                    trip_main_dict_temp["to_location"] = to_location
                    trip_main_dict_temp["to_date_time"] = date_time
            trip_main_list.append(trip_main_dict_temp)
        return trip_main_list

    @property
    def get_trips(self) -> int:
        count = 10
        trip_range = np.arange(1, 101)
        while True:
            try:
                count = int(input("The number of trips to return per page, up to a maximum of 100"))
            except ValueError:
                print("Sorry please enter integer number of trips to return per page")
                continue
            if count not in trip_range:
                print("Please enter values between 1 and 100")
            else:
                break

        return count

    def save_file(self,trip_main_list):
        with open('data.txt', 'w') as f:
            for item in trip_main_list:
                f.write("%s\n" % item)
        string_data = str(trip_main_list)
        print(string_data)
