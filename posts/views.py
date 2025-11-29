from django.shortcuts import render
from . models import Post, Categoria

# Create your views here.
def post_list(request):
    id_categoria = request.GET.get('id')

    if id_categoria:
        posts = Post.objects.filter(categoria_post=id_categoria)
    else:
        posts = Post.objects.all()

    categorias = Categoria.objects.all().order_by('nombre')

    context = {
        'posts': posts,
        'categoria': categorias
    }

    return render(request, 'posts/post_list.html', context)



