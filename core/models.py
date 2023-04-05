from django.db import models
from django.conf import settings

# The basic functionality of a model, including the ability to save and retrieve data.
class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

# This class is needed to create a many-to-many relationship between the Post and Tag models.
class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# This class is needed to create a one-to-many relationship between the Post and Comment models.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    # A nested class that specifies the default ordering of the objects.
    class Meta:
        ordering = ('-created',)

    # A method that returns a string representation of the object.
    def __str__(self):
        return 'Comment by {}'.format(self.name)


# This class is needed to create a one-to-many relationship between the Post and Like models.
class BlogPost(Post):
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title