from rest_framework import generics, permissions

from .models import Category, Publication
from .serializers import CategorySerializer, PublicationSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PublicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.filter(is_archived=False)
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicationRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()

