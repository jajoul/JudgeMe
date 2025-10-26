from django.db import models

# Create your models here.
class Post(models.Model):
    caption=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='post_images',blank=True,null=True)
    user=models.ForeignKey('user.CustomUser',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey('user.CustomUser',on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)




class Repost(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

