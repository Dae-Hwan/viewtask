import json

from django.http import JsonResponse
from django.views import View
from owner.models import Owner, Dog

class OwnerView(View):
    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs = owner.dog_set.all()
            dog_list = []
            for dog in dogs:
                dog_list.append(
                        {
                            'dog_name': dog.name,
                            'dog_age': dog.age
                        }
                )

            results.append(
                    {
                        'owner_name': owner.name,
                        'owner_email': owner.email,
                        'owner_age': owner.age,
                        'dog_list': dog_list
                        }

            )
            

        return JsonResponse({'results': results}, status = 200)

    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
                name = data['owner_name'],
                email = data['owner_email'],
                age = data['owner_age']
        )

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status = 201)


class DogView(View):
    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                    {
                        'owner_name': dog.owner.name,
                        'dog_name': dog.name,
                        'dog_age': dog.age
                        }
            )               

        return JsonResponse({'results': results}, status = 200)

    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name = data['owner_name']) 

        Dog.objects.create(
                    owner = owner,
                    name = data['dog_name'],
                    age = data['dog_age']
        )

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status = 201)
        















