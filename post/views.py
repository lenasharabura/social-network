from django.shortcuts import redirect
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from post.models import Post
from post.serializers import PostSerializer


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(
        methods=["GET"],
        detail=False,
        url_path="analytics",
    )
    def get_analytics(self, request):
        queryset = super().get_queryset()
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")
        if date_from:
            queryset = queryset.filter(created_at__gte=date_from)
        if date_to:
            queryset = queryset.filter(created_at__lte=date_to)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def like_or_unlike(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post:post-list')
