from ..models import Supplier

def get_suppliers():
  queryset = Supplier.objects.all()[:10]
  return (queryset)

def create_supplier(form):
  supplier = form.save()
  supplier.save()
  return ()