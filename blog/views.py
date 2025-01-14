from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryPutPatchAPIView(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
