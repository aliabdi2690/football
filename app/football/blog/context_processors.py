from .models import Tag


def add_tags_url(request):
    tags = Tag.objects.all()
    return {'tags':tags}