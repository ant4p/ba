from django.urls import path

from src.views import (
    ShowIndex,
    ShowAnalytics,
    ShowGraphs,
    ShowNets,
    ShowTables,
    ShowTablesSvod,
    ShowGraphsEnergyEbl,
    ShowGraphsEnergyIee,
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
    path("tables_svod/", ShowTablesSvod.as_view(), name="tables_svod"),
    path("graphs_ebl/", ShowGraphsEnergyEbl.as_view(), name="graphs_ebl"),
    path("graphs_iee/", ShowGraphsEnergyIee.as_view(), name="graphs_iee"),
    path("plan_fact/", ShowPlanFact.as_view(), name="plan_fact"),
    path("fact_plan/", ShowFactPlan.as_view(), name="fact_plan"),
]