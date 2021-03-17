from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.utils import timezone


class AccountManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password,
                                date_of_birth=date_of_birth
                                )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    date_of_birth = models.DateField()
    # mobile_number = models.IntegerField()
    last_login = models.DateTimeField(verbose_name='last active', auto_now=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Availability(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Staff(models.Model):
    user = models.OneToOneField(Account, on_delete=models.SET("not_active"))
    availability = models.ManyToManyField(Availability, related_name='availability', blank=True)


class Customer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.SET("not_active"))
    staff = models.ForeignKey(Staff, on_delete=models.SET("not_active"))
