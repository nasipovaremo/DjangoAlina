from django.shortcuts import render

from apps.blogs.models import Blog


def index(reguest):
    blogs = Blog.objects,all()

    context = {
        "blogs": blogs,
    }
    return render(reguest,"index.html", context=context)