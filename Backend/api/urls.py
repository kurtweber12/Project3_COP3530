from django.urls import path
from api.views import SearchResultView, DropDownView

# our two api endpoints.
urlpatterns = [
    path('search-results/', SearchResultView.as_view(), name="search-result"),
    path('dropdown/', DropDownView.as_view(), name="dropdown")
]