from django import template
register = template.Library()


@register.simple_tag
def get_nav_items():
    nav_items = {"General": [("Home", "fa-solid fa-house", "food:index"),
                               ("Add Item", "fa-solid fa-plus", "food:addItem"),],
                 }

    return nav_items