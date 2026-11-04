from django.urls import path
from .import views

urlpatterns =[
    path('cakes/',views.CakeListCreateView.as_view()),
    path('cakes/<int:id>/',views.CakeRetrieveUpdateDestroyView.as_view()),
    path('category/',views.CategoryListCreateView.as_view()),
    path('category/<int:id>/',views.CategoryRetrieveUpdateDestroyView.as_view()),
    path('shape/',views.ShapeListCreateView.as_view()),
    path('shape/<int:id>/',views.ShapeRetrieveUpdateDestroyView.as_view()),
     path('weight/',views.WeightListCreateView.as_view()),
    path('weight/<int:id>/',views.WeightRetrieveUpdateDestroyView.as_view())
    
]