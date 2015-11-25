from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.resources import ALL
from sakila_view.models import Actor


class ActorResource(ModelResource):

    class Meta:
        queryset = Actor.objects.all()
        resource_name = 'actors'
        allowed_methods = ['get', 'post']
        filtering = {
                        'first_name':ALL,
                        'last_name':ALL
                    }
