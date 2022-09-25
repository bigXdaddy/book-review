from django.contrib import admin
from .models import Homepage
from .models import Book
from .models import Writer
from .models import Language
from .models import Genre
from .models import Comment



# Register your models here.


admin.site.register(Homepage)
admin.site.register(Book)
admin.site.register(Writer)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Comment)

