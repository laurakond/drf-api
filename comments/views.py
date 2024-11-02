from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'post'
    ]


    def perform_create(self, Serializer):
        Serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly] # only the comment owner to be able to edit  or delete it
    serializer_class = CommentDetailSerializer # not to have to send  the post id every time to edit a comment
    queryset = Comment.objects.all()