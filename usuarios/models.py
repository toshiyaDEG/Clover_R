from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name,password=None):
        if not email:
            raise ValueError("Los usuarios deben tener una dirección de correo")
        if not username:
            raise ValueError("Los usuarios deben tener un nombre de usuario.")
        if not first_name:
            raise ValueError("Los usuarios deben tener nombres registrados")
        if not last_name:
            raise ValueError("Los usuarios deben tener apellidos registrados")
        user = self.model(
                email=self.normalize_email(email),
                username=username,
                first_name=first_name,
                last_name=last_name,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(verbose_name="first_name", max_length=60, null=False, blank=False, default="Nombres")
    last_name = models.CharField(verbose_name="last_name",max_length=60, null=False, blank=False, default="Apellidos")
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    typo = models.CharField(max_length=10, default="student")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.username
        # + ", " + self.email


    def has_perm(self, perm, obj=None):
        return self.is_admin


    def has_module_perms(self, app_label):
        return True