# sabse pahle 'python manage.py makemigrations' likhna niche terminal me fir 'python manage.py migrate'
# fir python manage.py createsuperuser
# fir runserver karna
from django.shortcuts import render
from .models import Botsdetection
from .forms import Sessioncountform


def session_count(request):
    form = Sessioncountform(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            date = form.cleaned_data['date']
            if Botsdetection.objects.filter(date=date).exists():
                data = Botsdetection.objects.filter(date=date)
                return render(request, 'admin/index.html', {'data': data})
            else:
                # apna wala code yaha par date ke correspondind dal de aur jpo niche 8000 aur 5000 hai waha par returnd data de de
                # khubsurat aur features thik kar rha tab tak

                Botsdetection.objects.create(date=date, users=8000, session_count=5000)
                data = Botsdetection.objects.filter(date=date)
                return render(request, 'admin/index.html', {'data': data})
        else:
            form = Sessioncountform(request.POST)
    return render(request, 'bots/admin.html', {'form': form})
