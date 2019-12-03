from ..models import Shoe
from ..models import ShoeInstance
from django.db.models import Count, F, Value
def get_all_shoeInstances():
  queryset = ShoeInstance.objects.all()[:10]
  return (queryset)

def create_shoeInstance(form):
  shoeInstance = form.save()
  shoeInstance.save()
  return ()