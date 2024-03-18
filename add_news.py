from django.utils import timezone
import random
from news.models import Article

def add_news():
    for _ in range(20):
        title = f'Заголовок {_ + 1}'
        content = f'Текст новости номер {_ + 1}. Это просто тестовая новость'
        pub_date = timezone.now() - timezone.timedelta(days=random.randint(1, 365))
        Article.objects.create(title=title, content=content, pub_date=pub_date)

if __name__ == "__main__"
    add_news()