from basic_stt.views import report
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()
# Create your models here.

class subs_market(models.Model):


    list_user = models.ManyToManyField(User, default=None, blank=True)


class marketpost(models.Model):
    title = models.CharField(max_length=30, blank= False)
    describe = models.TextField(max_length=200, blank= False)
    address = models.CharField(max_length=200, blank= False)
    contact = models.CharField(max_length=100, blank=False)
    price = models.CharField(max_length=30, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_outdate = models.PositiveSmallIntegerField(blank=False, default=15)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    report = models.ManyToManyField(User, default=None, blank=True, related_name='marketreport_set')
    post_img1 = models.ImageField(_("Ảnh 1:"), upload_to='postImg/market/', null=True, blank=True)
    post_img2 = models.ImageField(_("Ảnh 2:"), upload_to='postImg/market/', null=True, blank=True)
    post_img3 = models.ImageField(_("Ảnh 3:"), upload_to='postImg/market/', null=True, blank=True)
    post_img4 = models.ImageField(_("Ảnh 4:"), upload_to='postImg/market/', null=True, blank=True)
    post_img5 = models.ImageField(_("Ảnh 5:"), upload_to='postImg/market/', null=True, blank=True)
    

    def __str__(self):
        return self.title
    @property
    def num_report(self):
        return self.report.all().count()
    @property
    def is_expired(self):
        return timezone.now() > (self.date_posted + datetime.timedelta(days=self.date_outdate))
