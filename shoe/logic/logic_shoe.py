from ..models import Shoe

def get_shoes():
  queryset = Shoe.objects.all().order_by('pk')[:10]
  return (queryset)

def create_shoe(form):
  shoe = form.save()
  shoe.save()
  return ()