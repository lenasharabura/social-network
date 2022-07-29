from django.urls import path, include
from rest_framework import routers

from post.views import PostViewSet, like_or_unlike

router = routers.DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("posts/<int:post_id>/like/", like_or_unlike, name="like_or_unlike"),
    path("", include(router.urls)),
]

app_name = "post"
