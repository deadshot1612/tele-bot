from apps.product.models import Category,Product
# Create your views here.


def all_categories():
    categories = Category.objects.all()
    return categories

def get_product_from_category(cat):
    product_list = Product.objects.filter(catagory = cat).all()
    return product_list
