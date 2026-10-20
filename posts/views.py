from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Post
from .forms import PostForm

# --- Vistas de Posts ---

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'posts/lista_posts.html', {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detalle_post.html', {'post': post})

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'posts/form_post.html', {'form': form, 'titulo_pagina': 'Crear Post'})

@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/form_post.html', {'form': form, 'titulo_pagina': 'Editar Post'})

@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'posts/confirmar_eliminar.html', {'post': post})

# --- Vistas de Usuarios ---

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_posts')
    else:
        form = UserCreationForm()
    return render(request, 'posts/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_posts')
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('lista_posts')

@login_required
def perfil_usuario(request):
    posts_usuario = Post.objects.filter(autor=request.user).order_by('-fecha_creacion')
    return render(request, 'posts/perfil.html', {'posts_usuario': posts_usuario})