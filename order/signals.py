from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, OrderItem
from inventory_management.models import Product

@receiver(post_save, sender=Order)
def update_product_inventory(sender, instance, **kwargs):
    """
    Subtract product quantities from inventory when an order is completed and paid.
    """
    # Check if the order is completed and paid
    if instance.status == 'completed' and instance.is_paid:
        order_items = instance.orderitem_set.all()  # Fetch all items in the order

        for item in order_items:
            product = item.product
            if product.quantity >= item.quantity:
                product.quantity -= item.quantity  # Subtract ordered quantity from product stock
                product.save()
            else:
                raise ValueError(f"Insufficient stock for product: {product.name}")
