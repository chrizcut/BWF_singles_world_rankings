from django.urls import path
from .views import (
    FemaleSinglePlayerAPIView,
    MaleSinglePlayerAPIView,
    FemaleSinglePlayerDetail,
    MaleSinglePlayerDetail,
)

urlpatterns = [
    path("womens_singles/", FemaleSinglePlayerAPIView.as_view()),
    path("mens_singles/", MaleSinglePlayerAPIView.as_view()),
    path("womens_singles/<int:pk>/", FemaleSinglePlayerDetail.as_view()),
    path("mens_singles/<int:pk>/", MaleSinglePlayerDetail.as_view()),
]
