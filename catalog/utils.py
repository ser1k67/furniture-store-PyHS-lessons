from django.db.models import Q

from catalog.models import Products


def q_search(q):
    if q.isdigit() and len(q) <= 5:
        return Products.objects.filter(id=int(q))