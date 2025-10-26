from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
class FeedView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'feed/feed.html')
