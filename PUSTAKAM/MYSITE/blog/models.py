from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Homepage(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='genre_pics')
    genre = models.ManyToManyField('Genre', help_text="Select a genre for this book")

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    

class Genre(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
        )
   
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    image = models.ImageField(default='default.jpg', upload_to='book_pics')
    title = models.CharField(max_length=200)
    publication = models.CharField(max_length=200,default='none')
    the_writer = models.ManyToManyField('Writer', help_text="Select a genre for this book")
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    bookreview =  models.TextField(max_length=1000, default='enter your review here')
    the_genre = models.ManyToManyField('Genre', help_text="Select a genre for this book")
    buying_link = models.CharField(max_length=500,default='link')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

   
    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([the_genre.name for the_genre in self.the_genre.all()[:3]])
    display_genre.short_description = 'Genre'
    
    def display_writer(self):
        return ', '.join([the_writer.name for the_writer in self.the_writer.all()[:3]])
    
    def display_language(self):
        return ', '.join([language.name for language in self.language.all()[:3]])
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('bookdetail', args=[str(self.id)])

    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title
        

class Writer(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=200)
    penname = models.CharField(max_length=200,default='None')
    image = models.ImageField(default='default.jpg', upload_to='writer_pics')
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)
    Bio=models.CharField(max_length=2000)
    knowmore=models.CharField(max_length=300,default='none')

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('writerdetail', args=[str(self.id)])
    

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Comment(models.Model):
    book = models.ForeignKey('blog.Book',on_delete=models.CASCADE)
    username =  models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.TextField(max_length=200,default='enter your comment here' )
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text
   




    
