from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    ctx = {
        "page_title": "Início — Meu Site",
        "meta_description": "Conteúdos sobre [seu nicho]. Dicas, tutoriais e novidades.",
    }
    return render(request, "home.html", ctx)

def sobre(request):
    ctx = {
        "page_title": "Sobre — Meu Site",
        "meta_description": "Quem somos e o que fazemos no [seu nicho].",
    }
    return render(request, "sobre.html", ctx)

def contato(request):
    ctx = {
        "page_title": "Contato — Meu Site",
        "meta_description": "Fale conosco.",
    }
    return render(request, "contato.html", ctx)

# robots.txt como view plana
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
        "Sitemap: https://pistanews.com.br/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
