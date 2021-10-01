import requests
from blablacar import BlaBlaCar
import smtplib
from emailsending import send_email

class BlaBlaCarMain:
    locale = BlaBlaCar()
    main_trips_data = locale.get_blablacar_json()
    no_of_trips_available = main_trips_data['search_info']['count']
    trip_main_list = BlaBlaCar().trips_extract( main_trips_data, no_of_trips_available)
    BlaBlaCar.save_file(trip_main_list)
    send_email(no_of_trips_available)


if __name__ == '__main__':
    BlaBlaCarMain()

