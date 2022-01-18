from django.urls import path
from .views import (
    APIAllPost,
    patch_post,
)

urlpatterns = [
    path('api/v1/marketposts/', APIAllPost.as_view(), name='api-all-marketposts'),
    path('api/v1/patchmarketposts/', patch_post, name='edit_post'),
]