from django.views.generic import TemplateView


class ShowIndex(TemplateView):
    template_name = "src/index.html"


class ShowAnalytics(TemplateView):
    template_name = "src/analytics.html"


class ShowGraphs(TemplateView):
    template_name = "src/graphs.html"


class ShowNets(TemplateView):
    template_name = "src/nets.html"


class ShowTables(TemplateView):
    template_name = "src/tables.html"


# class ShowIndex(TemplateView):
#     template_name = "src/index.html"
