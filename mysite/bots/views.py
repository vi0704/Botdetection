# sabse pahle 'python manage.py makemigrations' likhna niche terminal me fir 'python manage.py migrate'
# fir python manage.py createsuperuser
# fir runserver karna
from django.shortcuts import render
from .models import Botsdetection
from .forms import Sessioncountform
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import glob
import pandas as pd
from .models import Botsdetection
from .forms import Sessioncountform



def session_count(request):
    form = Sessioncountform(request.POST)
    data = Botsdetection.objects.all()
    if request.method == 'POST':

        if form.is_valid():
            date = form.cleaned_data['date']
            if Botsdetection.objects.filter(date=date).exists():
                objects = Botsdetection.objects.get(date=date)
                date = objects.date
                sessions = objects.sessions
                users = objects.users
                sessions_per_user = objects.sessions_per_user
                context = {'date': date, 'users': users, 'sessions': sessions, 'sessions_per_user': sessions_per_user,
                           'form': form, 'data': data}
                return render(request, 'concept-master/index.html', context=context)

            else:
                form = Sessioncountform()
                path = "/home/user/Desktop/Botdetection/mysite/bots/clean_log"
                file = glob.glob(path + '*{}.log.gz'.format(date))
                for k in file:
                    clean_data = pd.read_csv(k)
                    users = clean_data['uniqueid'].nunique()
                    sessions = clean_data['sessionid'].nunique()
                    sessions_per_user = round(sessions / users, 2)
                    Botsdetection.objects.create(date=date, users=users, sessions=sessions,
                                                    sessions_per_user=sessions_per_user)
                    context = {'date': date, 'users': users, 'sessions': sessions, 'sessions_per_user': sessions_per_user,
                                'form': form, 'data': data}
                    return render(request, 'concept-master/index.html', context=context)

        else:
            form = Sessioncountform(request.POST)
    return render(request, 'concept-master/index.html', {'form': form, 'data': data})



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


