from django.db import models
from django.utils import timezone
# author of a post is going to be a user from User model. Hence import User
from django.contrib.auth.models import User


class Posts(models.Model):
    title = models.CharField(max_length=100)
    # TextField is free form text.
    text  = models.TextField()
    # user_date_crated takes a default value by running the default function
    # timezone.now(). Note that parentheses are not included in this
    # declaration. User can assign a value to this field.
    user_date_crated = models.DateTimeField(default=timezone.now)
    # date_updated has argument "auto_now=True", this means that this field
    # will get the date time of whenever any change is done to the record
    date_updated = models.DateTimeField(auto_now=True)
    # sys_date_created is system captured when a new record is created. But
    # it is not a user editable value.
    sys_date_created = models.DateTimeField(auto_now_add=True)
    # posts-user have many-to-one relationship. Hence using foreign key
    # on_delete=models.CASCADE means if a user is deleted, all posts are deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        dunder ~ double underscores
        __str__ controls how the object is printed.

        Without this customized method:
        In [25]: Posts.objects.all()
        Out[25]: <QuerySet [<Posts: Posts object (1)>]>

        With customized __str__:
        In [2]: Posts.objects.all()
        Out[2]: <QuerySet [<Posts: Django data bases>]>

        :return: As shown above
        """
        return self.title
