# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'belle/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'belle/detail.html', context={'post': post})