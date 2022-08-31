from django.urls import path
from core.views import SearchPageView, StackListView, RateLimitErrorPage

app_name='core'

urlpatterns = [
    path('search/ans/', SearchPageView.as_view(), name='search_view'),
    path('api/limit-error/', RateLimitErrorPage.as_view(), name='api_limit'),
    path('', StackListView.as_view(), name='stack_list'),
]
