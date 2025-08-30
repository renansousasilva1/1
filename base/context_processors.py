from django.conf import settings

def seo_defaults(request):
    return {
        "site_name": getattr(settings, "SITE_NAME", "Meu Site"),
        "request": request,
    }
