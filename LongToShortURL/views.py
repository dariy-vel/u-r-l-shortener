from django.shortcuts import render, get_object_or_404, redirect
from .models import LongToShort
from .forms import AddLongURLForm
import string
import random


def generate_short_url():
    output = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=7))
    return output


def home(request, generated_url =""):
    if request.method == 'POST':
        form = AddLongURLForm(request.POST)

        if form.is_valid():
            shortener_obj = form.save(commit=False)
            short_url = generate_short_url()
            while LongToShort.objects.filter(short_url = short_url).exists():
                short_url = generate_short_url()
            shortener_obj.short_url = short_url
            shortener_obj.save()
            return redirect('home', generated_url=shortener_obj.short_url)
    else:
        form = AddLongURLForm()
    return render(request, 'home.html', {'generated_url': generated_url, 'form': form})


def redirecto(request, url):
    redirect_obj = get_object_or_404(LongToShort, short_url=url)
    redirect_url = redirect_obj.long_url
    return redirect(redirect_url)