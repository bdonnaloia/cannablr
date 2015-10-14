from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.conf import settings
from PIL import Image
from django_resized import ResizedImageField
import datetime




class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    storename=models.CharField(null=True, blank=True, max_length=20)
    streetaddress=models.CharField(null=True, blank=True, max_length=30)
    city = models.CharField(null=True, blank=True, max_length=20)
    state = models.CharField(null=True, blank=True, max_length=20)
    zipcode = models.IntegerField(_('zipcode'),
                                       max_length=5, null=True, blank=True)
    nearbyzips1=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips2=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips3=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips4=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips5=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips6=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips7=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips8=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips9=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips10=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips11=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips12=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips12=models.IntegerField(null=True, blank=True, max_length=10)
    nearbyzips13=models.IntegerField(null=True, blank=True, max_length=10)
    phone=models.CharField(null=True, blank=True, max_length=16)
    websiteurl=models.CharField(null=True, blank=True, max_length=38)
    deliveryoption=models.BooleanField(default=False)
    storebio=models.CharField(null=True, blank=True, max_length=100)
    storespecials=models.CharField(null=True, blank=True, max_length=65)
    reviewavg=models.FloatField(null=True, blank=True, max_length=5)
    coverpic = ResizedImageField(max_width=350, upload_to="site_media/media/covers/", null=True, blank=True)


class Entry(models.Model):
    headline= models.CharField(max_length=200,)
    body_text = models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='entryauthors')
    pub_date=models.DateTimeField(auto_now_add=True)
    zipcode =models.IntegerField(null=True, max_length=10)
    entrytype = models.IntegerField(null=True, max_length=3)
    price1 = models.CharField(max_length=20)
    price2 = models.CharField(max_length=20)
    price3 = models.CharField(null=True, blank=True, max_length=20)
    price4 = models.CharField(null=True, blank=True, max_length=20)
    price5 = models.CharField(null=True, blank=True, max_length=20)
    item_picture = ResizedImageField(max_width=400, upload_to="site_media/media/items/")

    def __str__(self):
        return u'%s %s %s %s %s %s %s' % (self.headline, self.body_text, self.author, self.pub_date, self.zipcode, self.price1, self.price2)

class UserReview(models.Model):
    name= models.ForeignKey(User, related_name='usersbeingreviewed', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviewauthors')
    pub_date=models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(max_length=5)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return u'%s %s %s %s %s' % (self.name, self.author, self.pub_date, self.stars, self.comment)

