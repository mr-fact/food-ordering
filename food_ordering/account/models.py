from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

from account.validators import UnicodePhoneValidator


class UserManager(BaseUserManager):

    @classmethod
    def normalize_phone(cls, phone):
        # TODO
        return phone

    def _create_user(self, phone, email, password, **extra_fields):
        """
        Create and save a user with the given phone, email, and password.
        """
        if not phone:
            raise ValueError("The given phone must be set")
        email = self.normalize_email(email)
        phone = self.normalize_phone(phone)

        user = self.model(phone=phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, email, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone = models.CharField(
        max_length=15,
        unique=True,
        db_index=True,
        validators=[UnicodePhoneValidator(), ]
    )

    USERNAME_FIELD = 'phone'

    objects = UserManager()

    def clean(self):
        self.email = self.__class__.objects.normalize_email(self.email)
        self.phone = self.__class__.objects.normalize_phone(self.phone)

    def save(self, *args, **kwargs):
        if self.password[:9] == '__pass__:':
            self.password = make_password(self.password[9:])
        super().save(*args, **kwargs)


class OrderManager(models.Manager):
    def create(self, user):
        order = Order(
            user=user
        )
        order.save()
        user.packets.filter(order=None).update(order=order)
        return order


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    REGISTERED = 1
    ACCEPTED = 2
    POSTED = 3
    RECEIVED = 4
    CANCELED = 5
    STATUS = (
        (REGISTERED, 'ثبت شده'),
        (ACCEPTED, 'تایید شده'),
        (POSTED, 'ارسال شده'),
        (RECEIVED, 'دریافت شده'),
        (CANCELED, 'کنسل شده'),
    )
    status = models.SmallIntegerField(default=1, choices=STATUS)
    paid = models.BooleanField(default=False)
    # packets
    # TODO save a record of address and user information and datetime

    objects = OrderManager()

    def __str__(self):
        return f'{self.user}'
