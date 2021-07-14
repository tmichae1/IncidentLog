from django.db import models
import datetime
from django.utils import timezone
import time

# Create your models here.


class StaffRole(models.Model):
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role


class Profile(models.Model):
    name = models.CharField(max_length=75, null=True)
    staff_role = models.ForeignKey(StaffRole, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IncidentLocation(models.Model):
    incident_location = models.CharField(max_length=50)

    def __str__(self):
        return self.incident_location


class IncidentType(models.Model):
    incident_type = models.CharField(max_length=100)

    def __str__(self):
        return self.incident_type


class Report(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    current_date = datetime.datetime.now()
    date = models.DateField(default=timezone.now)
    localtime = time.localtime()
    current_time = time.strftime("%H:%M", localtime)
    time = models.TimeField(default=current_time)
    incident_location = models.ForeignKey(IncidentLocation, on_delete=models.CASCADE)
    incident_type = models.ForeignKey(IncidentType, on_delete=models.CASCADE)
    incident_description = models.TextField()

    def __str__(self):
        return "{0}({1}) - reported on {2} at {5} - incident type {3} - located at {4}".format(self.profile.name,
                                                                                        self.profile.staff_role,
                                                                                        self.date.strftime("%d/%m/%Y"),
                                                                                        self.incident_type,
                                                                                        self.incident_location,
                                                                                        self.time.strftime("%H:%M"))




class AppSetting(models.Model):
    email_receiver = models.EmailField()

    def __str__(self):
        return "App Settings"