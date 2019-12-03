from ..models import Client

"""
    Class to manage all the logic of the client model.
"""
# Create
def create_client(form):
    client = form.save()
    client.save()
    return ()

# Retrieve
def get_clients():
    queryset = Client.objects.all()
    return (queryset)

def get_client(id: int):
    client = Client.objects.get(pk = id)
    return client

# Update
#def update_client(client_id: int, new_client):
 #   client = get_client(client_id)

 #  client.save()
    

# Delete
