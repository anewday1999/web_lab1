from vote.models import VoteItem

VoteItem(url="http://www.yandex.ru", rating=6).save()
VoteItem(url="http://www.google.com", rating=5).save()
VoteItem(url="http://www.habrahabr.ru", rating=6).save()