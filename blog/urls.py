from django.urls import path

from . import views

urlpatterns = [
    path('category/', view=views.CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', view=views.CategoryRetrieveUpdateDeleteAPIView.as_view()),
]