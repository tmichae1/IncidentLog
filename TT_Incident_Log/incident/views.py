from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReportForm
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail.message import EmailMessage
from io import StringIO
from .models import AppSetting
import datetime
import sys
import csv
import os


@login_required
def incident_form(request):
    template = "incident/report.html"
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            with open('csv.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                labels = ['Reported by (Name)',
                          'Reported by type',
                          'Date of incident',
                          'Time of incident',
                          'Type of incident',
                          'Location',
                          'Description']
                writer.writerow(labels)
                writer.writerow(['{}'.format(form.instance.profile.name),
                                 '{}'.format(form.instance.profile.staff_role),
                                 '{}'.format(form.instance.date),
                                 '{}'.format(form.instance.time.strftime("%H:%M")),
                                 '{}'.format(form.instance.incident_type),
                                 '{}'.format(form.instance.incident_location),
                                 '{}'.format(form.instance.incident_description)])

            with open('csv.csv', 'r') as f:
                message = ''
                app_settings_query = AppSetting.objects.first()
                mail_id = app_settings_query.email_receiver
                email = EmailMessage('Csv file', message, 'tmichae1coder@gmail.com', [mail_id])
                email.attach("report.csv", f.read(), 'text/csv')
                email.send()
            os.remove('csv.csv')
            messages.success(request, "Incident Reported.")
            return redirect('report')
    else:
        form = ReportForm(initial={'date': datetime.datetime.now(),
                                   'time': datetime.datetime.now().strftime("%H:%M")})

    context = {'form': form}
    return render(request, template, context)


