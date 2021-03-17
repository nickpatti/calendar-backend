# calendar-backend
Backend for an appointment calendar application I am working on.


Brief:

-Must work in both a weekly and monthly view.

-Must show all appointments booked by the customer currently logged in.

-Must not show personal details of other customers appointments.

-Should show all details of all of the currently logged in staff members' appointments.

-Should show all available appointments

-Should try to add as little as possible to the database within the availability model - done via a serializer method field



Possible improvements to be made:
- edit the serializer method field that pushes the date range of availability into an array. Remove the appointment time + duration from the array.
- automatically remove availability objects where the start and end date have passed after x amount of days/months?
