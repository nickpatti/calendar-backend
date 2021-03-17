BRIEF V1
======

To create a calendar that will show available times, and show when the staff member is busy.

- Only the staff member, customer, and any superuser may see the details of the appointment
- The calendar must show the monthly and weekly calendars
- To book an appointment, click on the slot in the weekly appointment. This should open a modal confirming the time and date of appointment, and length (30 or 60mins)
- Slots should only be clickable if the staff member is marked as available for that time and date.
- Show how many appointments the staff member has and total time for the week.


TUESDAY 09/03
==============

MODELS
=======
- BaseAbstractUser [ done
    - Name
    - User Type
]

- Availability [ done
    - start time
    - end time
]

- Staff (only created if baseabstractuser user type = staff) [ done
    - ForeignKey to User
    - manytomany to availability
]


SERIALIZERS
===========
- Availability [ done
    - start
    - end
    - datetime range(serializer method field)
]

- Appointment [ done
    - ForeignKey to User
    - ForeignKey to Staff
    - start
    - duration
]


WEDNESDAY 10/03
===============

create manager to bulk create users, adding any account without a customer or staff to an array
make the newly created accounts auto assign to customer or staff, probably at a ratio of 4:1 would work best
create a webscraper that will create random email addresses for each account


THURSDAY 11/03
===============

- Look over results from REST data to see if any improvements need to be made
- Create a management command for availability?
- Write tests for each model
- Ensure all necessary data is present before progressing with the front end.
