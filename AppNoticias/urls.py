from django import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='padre'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='AppNoticias/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('RegistroNuevaNoticia/', RegistroNuevaNoticia.as_view(), name='nueva'),
    
    path('acercaDelEditor/', views.about, name='acerca_del_editor'),

    path('deporteLista/', DeporteLista.as_view(), name='deportes'),
    path('deporteDetalle/<int:pk>/', DeporteDetalle.as_view(), name='deporte'),
    path('deporteEdicion/<int:pk>/', DeporteUpdate.as_view(), name='editar_deporte'),
    path('deporteBorrado/<int:pk>/', DeporteDelete.as_view(), name='eliminar_deporte'),
    path('deporteDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('politicaLista/', PoliticaLista.as_view(), name='politicas'),
    path('politicaDetalle/<int:pk>/', PoliticaDetalle.as_view(), name='politica'),
    path('politicaEdicion/<int:pk>/', PoliticaUpdate.as_view(), name='editar_politica'),
    path('politicaBorrado/<int:pk>/', PoliticaDelete.as_view(), name='eliminar_politica'),
    path('politicaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    
    path('farandulaLista/', FarandulaLista.as_view(), name='farandulas'),
    path('farandulaDetalle/<int:pk>/', FarandulaDetalle.as_view(), name='farandula'),
    path('farandulaEdicion/<int:pk>/', FarandulaUpdate.as_view(), name='editar_farandula'),
    path('farandulaBorrado/<int:pk>/', FarandulaDelete.as_view(), name='eliminar_farandula'),
    path('farandulaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('tecnologiaLista/', TecnologiaLista.as_view(), name='tecnologias'),
    path('tecnologiaDetalle/<int:pk>/', TecnologiaDetalle.as_view(), name='tecnologia'),
    path('tecnologiaEdicion/<int:pk>/', TecnologiaUpdate.as_view(), name='editar_tecnologia'),
    path('tecnologiaBorrado/<int:pk>/', TecnologiaDelete.as_view(), name='eliminar_tecnologia'),
    path('tecnologiaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('cienciaLista/', CienciaLista.as_view(), name='ciencias'),
    path('cienciaDetalle/<int:pk>/', CienciaDetalle.as_view(), name='ciencia'),
    path('cienciaEdicion/<int:pk>/', CienciaUpdate.as_view(), name='editar_ciencia'),
    path('cienciaBorrado/<int:pk>/', CienciaDelete.as_view(), name='eliminar_ciencia'),
    path('cienciaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

]



