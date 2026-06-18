from django.views.generic import TemplateView


class ShowIndex(TemplateView):
    template_name = "src/index.html"


class ShowAnalytics(TemplateView):
    template_name = "src/analytics.html"


class ShowPotentialES(TemplateView):
    template_name = "src/potential_es.html"


class ShowNets(TemplateView):
    template_name = "src/nets.html"


class ShowTables(TemplateView):
    template_name = "src/tables.html"

class ShowKeys(TemplateView):
    template_name = "src/keys.html"


class ShowIndicators(TemplateView):
    template_name = "src/indicators.html"

class ShowIntensity(TemplateView):
    template_name = "src/intensity.html"

class ShowPlanFact(TemplateView):
    template_name = "src/plan_fact.html"

class ShowFactPlan(TemplateView):
    template_name = "src/fact_plan.html"
