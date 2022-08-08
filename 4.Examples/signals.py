from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Customer

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Customer(user=user)
        profile.save()

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Perfil creado!')


post_save.connect(customer_profile, sender=User)
