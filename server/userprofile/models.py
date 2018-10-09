from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.


# class UserCategory(models.Model):
#
#     name = models.CharField(
#         max_length=250,
#         unique=True
#     )
#
#     description = models.TextField()
#
#     class Meta:
#         verbose_name_plural = "Категории"
#
#     def __str__(self):
#         return self.name

class UserCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "категории"       #categories under a parent with same
                                                 #slug

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class UserCompany(models.Model):

    name = models.CharField(
        max_length=250,
        unique=True,
        verbose_name='Компания'
    )

    description = models.TextField(
        blank=False,
        null=False,
        verbose_name='Описание'
    )

    create_date = models.DateTimeField(
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name_plural = "Компании"


    def __str__(self):
        return self.name


class Userprofile(models.Model):

    email = models.EmailField(
        max_length=250,
        verbose_name='Email',
        blank=False,
        null=False,
        unique=True
    )

    first_name = models.CharField(
        max_length=250,
        verbose_name='Имя',
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=250,
        verbose_name='Фамилия',
        blank=True,
        null=True
    )

    son_name = models.CharField(
        max_length=250,
        verbose_name='Отчество',
        blank=True,
        null=True
    )

    password = models.CharField(
        max_length=250
    )

    user_company = models.CharField(
        max_length=250,
        verbose_name='Компания',
        blank=True,
        null=True
    )
    category = models.ForeignKey('UserCategory', null=True, blank=True, on_delete=models.CASCADE)
    # category = models.ForeignKey(UserCategory, on_delete=models.CASCADE)

    create_date = models.DateTimeField(
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        auto_now=True
    )

    url_company = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )

    avatar = models.ImageField(
        blank=True,
        null=True,
        unique=True
    )

    bio = models.TextField(
        blank=True,
        null=True,
        unique=True
    )

    class Meta:
        verbose_name_plural = "Пользователи"


    def __str__(self):
        return self.last_name



    # def CreateUser(self):
    #     user_create = User.objects.create_user(Userprofile.email, Userprofile.email, Userprofile.password)
    #
    #     user_create.save()


