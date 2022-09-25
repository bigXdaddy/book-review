from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from .models import Book,Writer,Genre,Language,Homepage,Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    context = {
        'genres':Homepage.objects.all()
    }
    return render(request, 'home.html',context)


def booklist(request):
    context = {
        'books': Book.objects.all()
        }
    
    return render(request, 'booklist.html', context)

def writerlist(request):
    context = {
        'writers': Writer.objects.all()
    }
    return render(request, 'writerlist.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})



def bookdetail(request, id):
    
     book= Book.objects.get(id=id)

     return render(request, 'bookdetail.html',{'book': book})


def writerdetail(request, id):
    
    writer = Writer.objects.get(id=id)
                 
    return render(request, 'writerdetail.html',{'writer': writer})


@login_required
def comments(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username= request.user
            comment.book = book
            comment.save()
            return redirect('bookdetail', id=book.id)
            
        
    else:
          form = CommentForm()

    return render(request, 'comments.html', {'form': form})


def Genres(request, id):
    genres = Genre.objects.get(id=id)
    return render(request, 'genrebooklist.html',{'genre': genres})

def search(request):
    text_search = request.GET.get("in")
    booklist= Book.objects.filter(title__icontains= text_search)
    writerlist=Writer.objects.filter(name__icontains=text_search)
    return render(request,'search.html',{'booklist':booklist ,'writerlist':writerlist})


def contact(request):
     return render(request, 'contact.html', {'title': 'Gallery'})







        




