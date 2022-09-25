from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('booklist/',views.booklist,name='booklist'),
    path('about/', views.about,name='blog-about'),
    path('blog/search/',views.search, name='search'),
    path('book/<int:id>', views.bookdetail, name='bookdetail'),
    path('writerlist/',views.writerlist,name='writerlist'),
    path('writer/<int:id>', views.writerdetail, name='writerdetail'),
    path('book/<int:id>/comment/', views.comments, name='comments'),
    path('Genres/<int:id>', views.Genres, name='Genres'),
    path('contact/',views.contact,name='contact')
]
