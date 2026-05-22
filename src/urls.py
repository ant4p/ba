from django.urls import path

from src.views import (
    ShowIndex,
    ShowAnalytics,
    ShowGraphs,
    ShowNets,
    ShowTables,
    ShowKeys,
    ShowIndicators,
    ShowIntensity,
    ShowPlanFact,
    ShowFactPlan
)

app_name = "src"

urlpatterns = [
    path("", ShowIndex.as_view(), name="index"),
    path("analytics/", ShowAnalytics.as_view(), name="analytics"),
    path("graphs/", ShowGraphs.as_view(), name="graphs"),
    path("nets/", ShowNets.as_view(), name="nets"),
    path("tables/", ShowTables.as_view(), name="tables"),
    path("keys/", ShowKeys.as_view(), name="keys"),
    path("indicators/", ShowIndicators.as_view(), name="indicators"),
    path("intensity/", ShowIntensity.as_view(), name="intensity"),
    path("plan_fact/", ShowPlanFact.as_view(), name="plan_fact"),
    path("fact_plan/", ShowFactPlan.as_view(), name="fact_plan"),
]