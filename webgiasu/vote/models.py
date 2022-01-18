from django.db import models

class VoteItem(models.Model):
    url = models.URLField()
    rating = models.IntegerField(default=0)

    class Meta:
        # это для того чтобы в ListView наши сайты сортировались по рейтингу
        ordering = ["-rating"]

    def __unicode__(self):
        return self.url
