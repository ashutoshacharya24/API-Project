from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    published_date = models.DateField()
    author = models.CharField(max_length=30)


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    text = models.CharField(max_length=30)
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)


