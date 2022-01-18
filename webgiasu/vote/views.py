from django.shortcuts import render

from django.views.generic import ListView
from vote.models import VoteItem

class VoteListView(ListView):
    model=VoteItem
    template_name="list.html"