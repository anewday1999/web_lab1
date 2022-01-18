from django.template.defaultfilters import default
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django import forms
from django.contrib.auth.models import AbstractUser
from PIL import Image
import datetime
from datetime import date

class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('Username:'),
        max_length=30,
        unique=True,
        help_text=mark_safe(_(
            '<small style="color:teal">Maximun is 30 characters. include number, characters and @ . + - _</small>'
        )),
        validators=[username_validator], 
        error_messages={
            'unique': mark_safe(_(
            '<small style="color:#e60000">Username is already existed.</small>'
        )),
        },
    )
    first_name = None
    last_name = None
    full_name = models.CharField(_('Fullname :'), max_length=255)
    email = models.EmailField(_('email address'), unique=True, max_length=150)

    address = models.CharField(_("Address:"), max_length=500, blank=True)
    school = models.CharField(_("School:"), max_length=500, blank=True)
    specialize = models.CharField(_("Special:"), max_length=500)
    yearofschool = models.PositiveSmallIntegerField(_("Years of school:"), null = True, blank = True)

    class Sexs(models.TextChoices):
        Male = 'Male'
        Female = 'Female'

    sexs = models.CharField(
        _("Sexs:"),
        max_length=6,
        choices=Sexs.choices,
        default=Sexs.Male
    )

    years_of_birth = models.PositiveSmallIntegerField(_("Years old"), null= True, blank=True)

    more = models.TextField(_("More:"), blank=True)
 
    avatar = models.ImageField(_("Avatar:"),default='default95486216548123654894126.png', upload_to='avatar')

    paid_until = models.DateField(null=True, blank=True)

    is_sub_findtutor = models.BooleanField(null= True, blank= True, default=False)
    is_sub_market = models.BooleanField(null= True, blank= True, default=False)
    is_sub_employee = models.BooleanField(null= True, blank= True, default=False)
    is_sub_homework = models.BooleanField(null= True, blank= True, default=False)

    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100, default='', blank=True) 

    def __str__(self):
        return self.username

    def set_paid_until(self, date_or_timestamp):
        if isinstance(date_or_timestamp, int):
            paid_until = date.fromtimestamp(date_or_timestamp)
        elif isinstance(date_or_timestamp, str):
            paid_until = date.fromtimestamp(int(date_or_timestamp))
        else:
            paid_until = date_or_timestamp
        self.paid_until = paid_until
        self.save()

    def has_paid(self):
        current_date = datetime.date.today()
        if self.paid_until is None:
            return False
        return current_date < self.paid_until


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)

        # When image height is greater than its width
        if img.height > img.width:
            # make square by cutting off equal amounts top and bottom
            left = 0
            right = img.width
            top = (img.height - img.width)/2
            bottom = (img.height + img.width)/2
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width >300:
                output_size = (300, 300)
                img.thumbnail(output_size)
            img.save(self.avatar.path)

        # When image width is greater than its height
        elif img.width > img.height:
            # make square by cutting off equal amounts left and right
            left = (img.width - img.height)/2
            right = (img.width + img.height)/2
            top = 0
            bottom = img.height
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width >300:
                output_size = (300, 300)
                img.thumbnail(output_size)
            img.save(self.avatar.path)
        elif img.width == img.height:
            if img.height > 300 or img.width >300:
                output_size = (300, 300)
                img.thumbnail(output_size)
            img.save(self.avatar.path)
    