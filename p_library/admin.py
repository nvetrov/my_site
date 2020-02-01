from django.contrib import admin

# Register your models here.
from django.contrib import admin
from p_library.models import Book, Author, Publisher


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    # list_display = ('id', 'full_name', 'birth_year', 'country')
    fields = ('full_name', 'birth_year', 'country', )

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name


@admin.register(Publisher)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    @staticmethod
    def author_name(obj):
        return obj.author.name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'Publisher_id', 'copy_count', 'price')
    '''
    Для этого мы перечисляем в свойстве fields класса BookAdmin все поля, которые разрешено редактировать
    В результате мы увидим, что поле copy_count исчезло из панели редактирования и создания. Оно теперь будет принимать
    default-значение, указанное в модели Book. Его редактирование теперь будет доступно только из shell.
    
    class AuthorAdmin(admin.ModelAdmin):
    exclude = ('birth_date',)
    
    '''
