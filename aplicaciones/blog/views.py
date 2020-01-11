from django.shortcuts import render
from .models import Post,Categoria # REFERENCIAR LOS MODELOS
from django.shortcuts import get_object_or_404# sirve para validar los post
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

#def home(request):
    #queryset=request.GET.get("buscar") # creacion de busqueda en la barra de busqueda
    #print(queryset)
    #posts=Post.objects.filter(estado=True)# es para referenciar  el post en el index oen la plantilla

    if queryset:
        posts=Post.objects.filter(
        Q(titulo__icontains=queryset) |
        Q(descripcion__icontains= queryset)   #es para validar en la barra de busqueda del blog

        ).distinct()
    paginator=Paginator(posts,3)# se instancia la clase paginator y recibe 2 parametros la lista y el total a mostrarpor cada pagina
    page=request.GET.get('page')    #la pagina actual en el template
    posts= paginator.get_page(page), # el valor a seguir en el template




    return render(request,'index.html',{'posts':posts})



def generales(request):
    queryset=request.GET.get("buscar")
    posts=Post.objects.filter(
    estado=True,
    categoria=Categoria.objects.get(nombre__iexact='generales')

    )
    if queryset:
        posts=Post.objects.filter(
        Q(titulo__icontains=queryset) |
        Q(descripcion__icontains=queryset),
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='generales'),  # se referencia por categoria los post
        ).distinct()
        paginator=Paginator(posts,1)# se instancia la clase paginator y recibe 2 parametros la lista y el total a mostrarpor cada pagina
        page=request.GET.get('page')    #la pagina actual en el template
        posts= paginator.get_page(page)# el valor a seguir en el template


    return render(request,'generales.html',{'posts':posts})



def programacion(request):
    queryset=request.GET.get("buscar")
    posts=Post.objects.filter(
    estado=True,
    categoria=Categoria.objects.get(nombre__iexact= 'programacion')

    )
    if queryset:
        posts=Post.objects.filter(
        Q(titulo__icontains=queryset)|
        Q(descripcion__icontains=queryset),
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='programacion'),
        ).distinct()
        paginator=Paginator(posts,1)# se instancia la clase paginator y recibe 2 parametros la lista y el total a mostrarpor cada pagina
        page=request.GET.get('page')    #la pagina actual en el template
        posts= paginator.get_page(page)# el valor a seguir en el template


    return render(request,'programacion.html',{'posts':posts})



def tutoriales(request):
    queryset=request.GET.get("buscar")
    posts=Post.objects.filter(
    estado=True,
    categoria=Categoria.objects.get(nombre__iexact='tutoriales'),
    )
    if queryset:
        post=Post.objects.filter(
        Q(titulo__icontain=queryset)|
        Q(descripcion__icontain=queryset),
        estado=True,
        categoria=Categoria.objects.get(nombre_iexact='tutoriales'),# el iexact sirve para validar los nombre sin importar mayusculas o min
        ).distinct()
        paginator=Paginator(posts,1)# se instancia la clase paginator y recibe 2 parametros la lista y el total a mostrarpor cada pagina
        page=request.GET.get('page')    #la pagina actual en el template
        posts= paginator.get_page(page)# el valor a seguir en el template



    return render(request,'tutoriales.html',{'posts':posts})




def tecnologia(request):
    queryset=request.GET.get("buscar")
    posts=Post.objects.filter(
    estado=True,
    categoria=Categoria.objects.get(nombre__iexact='tecnologia'),
    )
    if queryset:
        posts=Post.objects.filter(
        Q(titulo__icontain=queryset)|
        Q(descripcion__icontain=queryset),
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='tecnologia'),
        ).distinct()
        paginator=Paginator(posts,1)# se instancia la clase paginator y recibe 2 parametros la lista y el total a mostrarpor cada pagina
        page=request.GET.get('page')    #la pagina actual en el template
        posts= paginator.get_page(page)# el valor a seguir en el template



    return render(request,'tecnologia.html',{'posts':posts})


def videojuegos(request):
    queryset=request.GET.get("buscar")
    posts=Post.objects.filter(
    estado=True,
    categoria=Categoria.objects.get(nombre__iexact='videojuegos'),
    )
    if queryset:
        posts=Post.objects.filter(
        Q(titulo__icontain=queryset)|
        Q(descripcion__icontain=queryset),
        estado=True,
        categoria=Categoria.objects.get(nombre_iexact='videojuegos'),
        ).distinct()
        paginator=Paginator(posts,1)# se instancia la clase paginator y recibe 2 parametros la lista y el total a mostrarpor cada pagina
        page=request.GET.get('page')    #la pagina actual en el template
        posts= paginator.get_page(page)# el valor a seguir en el template



    return render(request,'videojuegos.html',{'posts':posts})

def inicio(request):
    return render(request,'inicio.html')

def detallePost(request,slug):
   post=get_object_or_404(Post,slug=slug) # sirve para validar los post si existen  o no
   return render(request,'post.html',{'detalle_Post':post})
