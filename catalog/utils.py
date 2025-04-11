from django.db.models import Q

from catalog.models import Products


def q_search(q):
    if q.isdigit() and len(q) <= 5:
        return Products.objects.filter(id=int(q))
    
    words = [word for word in q.split() if len(word) > 2]

    q_objects = Q()

    for word in words:
        q_objects |= Q(name__icontains=word)
        q_objects |= Q(description__icontains=word)
    
    return Products.objects.filter(q_objects)