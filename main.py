from blablacar import BlaBlaCar
from emailsending import send_email


class BlaBlaCarMain:
    object_blablacar = BlaBlaCar()
    main_trips_data = object_blablacar.get_blablacar_json()
    no_of_trips_available = main_trips_data['search_info']['count']
    trip_main_list = object_blablacar.trips_extract(main_trips_data = main_trips_data, no_of_trips_available= no_of_trips_available)
    object_blablacar.save_file(trip_main_list)
    send_email(no_of_trips_available)


if __name__ == '__main__':
    BlaBlaCarMain()
