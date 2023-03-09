from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import NotasNoticias, Comentario
from .forms import FormularioRegistroUsuario, FormularioEdicion, FormularioCambioPassword, FormularioNuevaNoticia, ActualizacionNoticia, FormularioComentario


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'AppNoticias/padre.html'

class LoginPagina(LoginView):
    template_name = 'AppNoticias/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('padre')

    def get_success_url(self):
        return reverse_lazy('padre')

class RegistroPagina(FormView):
    template_name = 'AppNoticias/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('padre')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('padre')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'AppNoticias/edicionPerfil.html'
    success_url = reverse_lazy('padre')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppNoticias/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'AppNoticias/passwordExitoso.html', {})

class RegistroNuevaNoticia(LoginRequiredMixin, CreateView):
    model = NotasNoticias
    form_class = FormularioNuevaNoticia
    success_url = reverse_lazy('padre')
    template_name = 'AppNoticias/registroNuevaNoticia.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RegistroNuevaNoticia, self).form_valid(form)

# ACERCA DEL EDITOR
def about(request):
    return render(request, 'AppNoticias/acercaDelEditor.html', {})

#DEPORTE
class DeporteLista(LoginRequiredMixin, ListView):
    context_object_name = 'deportes'
    queryset = NotasNoticias.objects.filter(noticia__startswith='deporte')
    template_name = 'AppNoticias/deporteLista.html'
    login_url = '/login/'

class DeporteDetalle(LoginRequiredMixin, DetailView):
    model = NotasNoticias
    context_object_name = 'deporte'
    template_name = 'AppNoticias/deporteDetalle.html'

class DeporteUpdate(LoginRequiredMixin, UpdateView):
    model = NotasNoticias
    form_class = ActualizacionNoticia
    success_url = reverse_lazy('deportes')
    context_object_name = 'deporte'
    template_name = 'AppNoticias/deporteEdicion.html'

class DeporteDelete(LoginRequiredMixin, DeleteView):
    model = NotasNoticias
    success_url = reverse_lazy('deportes')
    context_object_name = 'deporte'
    template_name = 'AppNoticias/deporteBorrado.html'

#POLITICA
class PoliticaLista(LoginRequiredMixin, ListView):
    context_object_name = 'politicas'
    queryset = NotasNoticias.objects.filter(noticia__startswith='politica')
    template_name = 'AppNoticias/politicaLista.html'
    login_url = '/login/'

class PoliticaDetalle(LoginRequiredMixin, DetailView):
    model = NotasNoticias
    context_object_name = 'politica'
    template_name = 'AppNoticias/politicaDetalle.html'

class PoliticaUpdate(LoginRequiredMixin, UpdateView):
    model = NotasNoticias
    form_class = ActualizacionNoticia
    success_url = reverse_lazy('politicas')
    context_object_name = 'politica'
    template_name = 'AppNoticias/politicaEdicion.html'

class PoliticaDelete(LoginRequiredMixin, DeleteView):
    model = NotasNoticias
    success_url = reverse_lazy('politicas')
    context_object_name = 'politica'
    template_name = 'AppNoticias/politicaBorrado.html'

#FARANDULA
class FarandulaLista(LoginRequiredMixin, ListView):
    context_object_name = 'farandulas'
    queryset = NotasNoticias.objects.filter(noticia__startswith='farandula')
    template_name = 'AppNoticias/farandulaLista.html'
    login_url = '/login/'

class FarandulaDetalle(LoginRequiredMixin, DetailView):
    model = NotasNoticias
    context_object_name = 'farandula'
    template_name = 'AppNoticias/farandulaDetalle.html'

class FarandulaUpdate(LoginRequiredMixin, UpdateView):
    model = NotasNoticias
    form_class = ActualizacionNoticia
    success_url = reverse_lazy('farandulas')
    context_object_name = 'farandula'
    template_name = 'AppNoticias/farandulaEdicion.html'

class FarandulaDelete(LoginRequiredMixin, DeleteView):
    model = NotasNoticias
    success_url = reverse_lazy('farandulas')
    context_object_name = 'farandula'
    template_name = 'AppNoticias/farandulaBorrado.html'

#TECNOLOGIA
class TecnologiaLista(LoginRequiredMixin, ListView):
    context_object_name = 'tecnologias'
    queryset = NotasNoticias.objects.filter(noticia__startswith='tecnologia')
    template_name = 'AppNoticias/tecnologiaLista.html'
    login_url = '/login/'

class TecnologiaDetalle(LoginRequiredMixin, DetailView):
    model = NotasNoticias
    context_object_name = 'tecnologia'
    template_name = 'AppNoticias/tecnologiaDetalle.html'

class TecnologiaUpdate(LoginRequiredMixin, UpdateView):
    model = NotasNoticias
    form_class = ActualizacionNoticia
    success_url = reverse_lazy('tecnologias')
    context_object_name = 'tecnologia'
    template_name = 'AppNoticias/tecnologiaEdicion.html'

class TecnologiaDelete(LoginRequiredMixin, DeleteView):
    model = NotasNoticias
    success_url = reverse_lazy('tecnologias')
    context_object_name = 'tecnologia'
    template_name = 'AppNoticias/tecnologiaBorrado.html'

#CIENCIA
class CienciaLista(LoginRequiredMixin, ListView):
    context_object_name = 'ciencias'
    queryset = NotasNoticias.objects.filter(noticia__startswith='ciencia')
    template_name = 'AppNoticias/cienciaLista.html'
    login_url = '/login/'

class CienciaDetalle(LoginRequiredMixin, DetailView):
    model = NotasNoticias
    context_object_name = 'ciencia'
    template_name = 'AppNoticias/cienciaDetalle.html'

class CienciaUpdate(LoginRequiredMixin, UpdateView):
    model = NotasNoticias
    form_class = ActualizacionNoticia
    success_url = reverse_lazy('ciencias')
    context_object_name = 'ciencia'
    template_name = 'AppNoticias/cienciaEdicion.html'

class CienciaDelete(LoginRequiredMixin, DeleteView):
    model = NotasNoticias
    success_url = reverse_lazy('ciencias')
    context_object_name = 'ciencia'
    template_name = 'AppNoticias/cienciaBorrado.html'

# COMENTARIOS
class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppNoticias/comentario.html'
    success_url = reverse_lazy('padre')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)
