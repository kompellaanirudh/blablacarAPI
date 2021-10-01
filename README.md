In this project, the complete code will let the user to get an email of the trips in particular date range using BlaBlaCar API.
I have used following APIs 
1. MapRequest to get the geographic coordinates, it will give the coordinates of the location user selects which
will be used as inputs for BlaBlaCar API.
2. Tkinter, it will give a calender input to user to select the Date as required to search for the trips
3. Requests, this package is used to send the API calls to BlaBlaCar and take the response using get method
4. SMTP, after all the processing of the JSON reponse from the request, all the trip data will be saved as text file and send to the email id
given by user.

The code will check for the user exceptions for user inputs while selecting more seats, and ValueError exception for number of seats and ask user until 
they give correct input and many other exceptions can be added in future.
After collecting the data into the JSON, we extract the trips data, followed by saving in list of dict for the trip details

It can be deployed and can be run at the required timeslot, which further will be send an email to the email addreess provided in the to field.

Sample data sent to user can be seen in data.txt file.

Please let me know if there are further modifications adding to this file, we can create a branch and work together.

Packages used
--python3.9
--mime
--pandas
--requests
--os
--tkinter
--tkcalendar
--smtp


