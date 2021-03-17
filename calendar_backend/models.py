from django.db import models
from users.models import Staff, Customer


class Appointment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET("canceled"))
    staff = models.ForeignKey(Staff, on_delete=models.SET("canceled"))
    start_time = models.DateTimeField()
    duration = models.DurationField()
