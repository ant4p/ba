from django.urls import path

from src.views import (
    ShowIndex,
    ShowAnalytics,
    ShowGraphs,
    ShowNets,
    ShowTables,
)

app_name = "src"

urlpatterns = [
    path("", ShowIndex.as_view(), name="index"),
    path("analytics/", ShowAnalytics.as_view(), name="analytics"),
    path("graphs/", ShowGraphs.as_view(), name="graphs"),
    path("nets/", ShowNets.as_view(), name="nets"),
    path("tables/", ShowTables.as_view(), name="tables"),
]