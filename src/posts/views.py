from ast import Delete
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from posts.forms import BookForm, BookFormEdit

from posts.models import BookPost

# def rating_view(request):
    
#     obj = BookRating.objects.filter(score=0).order_by("?").first()
#     context = {'object':obj}
#     return render(request, 'posts/rating.html', context)

# class BookRating(CreateView):
#     model = BookPost
#     obj = BookPost.objects.filter(score=0).order_by("?").first()
#     context = {"object": obj}
#     context_object_name = "context"
#     fields = ["score",]
#     template_name = "posts/rating.html"

class BookRating(UpdateView):
    model = BookPost
    context_object_name = "post"
    fields = ["score",]
    template_name = "posts/rating.html"

    def get_context_data(self, **kwargs):
        obj = BookPost.objects.filter(score=0).order_by("?").first()
        context = super(BookPostUpdate).get_context_data(**kwargs)
        context["score"] = obj.score
        return context

class BookHome(ListView):
    model = BookPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated: #si connecté, on retourne le queryset de tous les articles, même les non publiés
            return queryset

        return queryset.filter(published=True) #sinon, on retourne que les articles publiés

@method_decorator(login_required, name="dispatch") #dispatch étant une fonction django
class BookPostCreate(CreateView): #CreateView qui permet d'accéder à "form" dans html, via les fields renseignés
    model = BookPost
    form_class = BookForm
    template_name = "posts/bookpost_create.html"
    #fields = ['title', 'content',]

@method_decorator(login_required, name="dispatch")
class BookPostUpdate(UpdateView):
    model = BookPost
    form_class = BookFormEdit
    template_name = "posts/bookpost_edit.html"
    #fields = ['title', 'content', 'created_on', 'published']

class BookPostDetail(DetailView):
    model = BookPost
    context_object_name = "post" #par défaut, ça retournerait "object.title" sur l'html bookpost_detail

@method_decorator(login_required, name="dispatch")  
class BookPostDelete(DeleteView):
    model = BookPost
    context_object_name = "post" #d'ailleurs, post retourne forcément le titre du livre (dans models, le def__str__ retourne le titre)
    success_url = reverse_lazy("posts:home") #l'url pour nous rediriger une fois l'article supprimé (en utilisant ce process dans une classe, on ne peut pas utiliser "reverse", on aura un message d'erreur - d'où l'utilisation de reverse_lazy)

