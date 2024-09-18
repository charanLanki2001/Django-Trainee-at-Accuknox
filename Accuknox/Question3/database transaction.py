from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection

# Define a model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define a signal handler for post_save
@receiver(post_save, sender=MyModel)
def signal_handler(sender, instance, **kwargs):
    
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO my_other_table  VALUES ('Signal ran')")
        print("Signal handler ran")

# Simulate saving a model 
def save_with_transaction():
    print("Transaction started")
    
    with transaction.atomic():  #  new transaction
        obj = MyModel.objects.create(name='Test Object')
        print("Object created")
        
       
        # transaction.set_rollback(True)

        print("Transaction committed")

save_with_transaction()
