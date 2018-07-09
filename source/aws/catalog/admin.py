from django.contrib import admin

# imports the models.py and then calls admin.site.register to register each of them
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)
