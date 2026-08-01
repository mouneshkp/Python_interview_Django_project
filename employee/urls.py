from django.urls import path
from .views import CompanyListCreateView,CompanyRetriveUpdateDeleteview


urlpatterns = [
    path("companies/", CompanyListCreateView.as_view(), name="company-list"),
    path("companies/<int:pk>/", CompanyRetriveUpdateDeleteview.as_view(), name="comapny-detail")
]