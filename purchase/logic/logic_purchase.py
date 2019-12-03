from ..models import Purchase

def get_purchases():
  queryset = Purchase.objects.all().order_by('-purchase_date')[:10]
  return (queryset)

def create_purchase(form):
  purchase = form.save()
  purchase.save()
  return ()