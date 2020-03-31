import random
import string


def get_random_name(length=25):
    y = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    return y


def item_path(instance, filename):
    category = instance.item.category.name
    product = instance.item.name
    y = get_random_name()
    name, extension = filename.split('.')
    return 'categories/{}/{}/{}.{}'.format(category, product, y, extension)


def category_path(instance, filename):
    category = instance.name
    y = get_random_name()
    name, extension = filename.split('.')
    return 'categories/{}/{}.{}'.format(category, y, extension)
