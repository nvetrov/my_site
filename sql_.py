from django.db.models import Count, F, Value
from django.db.models.functions import Length, Upper

from p_library.models import Author, Book
from django.db.models import Avg, Max, Min


pushkin = Author.objects.get(full_name="Пушкин Александр Сергеевич")
pushkin_books = Book.objects.filter(author=pushkin)
--------------------------------------------------------------------

no_horsman_pushkin_books = Book.objects.all().filter(author=pushkin).exclude(title__icontains="всадник")

for book in no_horsman_pushkin_books:
    print(book.title)

---------------------------------------------------
from p_library.models import Author, Book
max price

>> from django.db.models import Avg
>>> Book.objects.all().aggregate(Max('price'))
----------------------------------------------------------------------
minBook = Book.objects.all().aggregate(Min('price'))
Book.objects.all().filter(price = minBook['price__min']).count()
queryset = Author.objects.all()
str(queryset.query)
-------------------------------------------------------------

Table.objects.exclude(title__in=myListOfTitles)  # SQL: not in (....) == exclude
 ----------------------------------------------------


from p_library.models import Author, Book
from django.db.models import Avg, Max, Min, Sum, F, QuerySet, Count

# Book.objects.aggregate(Max('price'))
# Book.objects.filter(type="normal").values('color').annotate(amount=Sum('id', field="width * height"))
Book.objects.filter(copy_count__gt=1).values('price').annotate(amount=Sum('price','copy_count', field="price * copy_count"))

Book.objects.values_list('id', 'price') # на выходе LIST
Book.objects.values('id', 'price')  # на выходе  список из значений: ключ знамечение -> словарь.
--Сколько стоит самая дорогая книга?
-- ToDO Book.objects.aggregate(Max('price'))
select max(price) as max_price
from p_library_book;
'''

# --Todo: Сколько в библиотеке копий самой дешёвой книги?
# select title, SUM(copy_count) as amout_price
# from p_library_book
# GROUP BY title
# ORDER BY amout_price
# limit 1;

# Todo -- Сколько стоят все библиотечные книги авторов, у которых больше одной книги?

# select sum(A.total) as "библиотечные книги авторов"
# from (
# select round(sum(b.price * b.copy_count),2) as total
# from p_library_book as b
# inner join p_library_author a on b.author_id = a.id
# GROUP BY b.author_id
# HAVING  COUNT(*) > 1
# ) as A;

--13863.630000000001

# Todo --Сколько стоят все библиотечные книги иностранных писателей?
# select  round(sum(b.price * b.copy_count), 2) as Total
# from p_library_book as b
# inner join p_library_author a on b.author_id = a.id
# where a.country  not in  ('RU');
# --5879.990000000001


# Todo -Сколько стоят все экземпляры Пушкина в библиотеке?  ПРАВИЛЬНЫЙ ОТВЕТ.
# select  a.full_name,  sum(b.price * b.copy_count) as price
# from p_library_book as b
# inner join p_library_author a on b.author_id = a.id
# where a.full_name = 'Пушкин Александр Сергеевич'
# GROUP BY  a.full_name; --12666.99
# -- GROUP BY  b.title;

# -- select b.title, sum(b.price) as price
# -- from p_library_book as b
# -- where b.author_id = 2
# -- GROUP BY  b.title;
# --4844.030000000001

# --Сколько стоят все книги, автор которых Douglas Adams? Не учитывайте стоимость копий.
# select  a.full_name,  round(sum(b.price),2) as price_with_out_copy
# from p_library_book as b
# inner join p_library_author a on b.author_id = a.id
# where a.full_name = 'Douglas Adams'
# GROUP BY  a.full_name;

from p_library.models import Author, Book, Publisher
from django.db.models import Avg, Max, Min, Sum, F, QuerySet, Count

Book.objects.all().annotate(amount_price=Sum("copy_count")).group_by("id").order_by("amount_price")

# books = Book.objects.all().annotate(amount_price=Sum("copy_count")).order_by("amount_price")
# books = QuerySet(query=books, model=Book)

books = Book.objects.all().annotate(amount_price=Sum("copy_count")).order_by("amount_price")
books = books.query
books.group_by["id"]
books = QuerySet(query=books, model=Book)

Book.objects.filter(author=Author.objects.filter(full_name='Пушкин Александр Сергеевич')).annotate(price=Sum(F("price") * F("copy_count")))
Book.objects.annotate(total_id=Sum('author__id'))
