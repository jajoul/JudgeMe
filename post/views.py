from django.shortcuts import render
from django.views.generic import View

# Create your views here.


from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post

class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'post/create-post.html')

    def post(self, request, *args, **kwargs):
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        user = request.user

        if not user.is_authenticated:
            return redirect('login')

        Post.objects.create(user=user, caption=caption, image=image)
        return redirect('blog:home')