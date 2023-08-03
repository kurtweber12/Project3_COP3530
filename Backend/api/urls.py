from django.urls import path
from api.views import SearchResultView

urlpatterns = [
    path('search-results/', SearchResultView.as_view(), name="search-result")
]