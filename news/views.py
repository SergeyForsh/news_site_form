from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def news_list(request):
    news_items = News.objects.all().order_by('-pub_date')
    return render(request, 'news_list.html', {'news_items': news_items})

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news_create.html', {'form': form})
