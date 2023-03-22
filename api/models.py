from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """Category Model"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    """Post Model"""

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=1)

    STATUS = (
        (0, 'Draft'),
        (1, 'Published'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_posts')
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    objects = models.Manager() # default manager.
    postobjects = PostObjects() # custom manager.

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
        Comment Model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    reply = models.ForeignKey('Comment', null=True, on_delete=models.CASCADE, related_name='replies')
    Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.content}'