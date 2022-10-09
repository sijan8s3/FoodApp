from django import template
import hashlib
import urllib

from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag
def get_nav_items():
    nav_items = {"Dashboard": [("Home", "fa-solid fa-house", "dashboard:Home"),
                               ("Inventory", "fa-solid fa-warehouse", "dashboard:Inventory"),
                               ("Orders", "fa-solid fa-truck-fast", "dashboard:Orders"),
                               ("Offers", "fa-solid fa-tags", "dashboard:Offers")],
                 "My Profile": [("My Profile", "fa-solid fa-user", "dashboard:MyProfile"),
                                ("Edit Profile", "fa-solid fa-user-pen", "dashboard:EditProfile"),
                                ("profile", "fa-solid fa-shield-halved", "two_factor:profile")],
                 "Administration": [("Add User", "fa-solid fa-user-plus", "dashboard:AddUser")],
                 "Logout": [("Logout", "fa-solid fa-right-from-bracket", "dashboard:Logout")]
                 }

    return nav_items


@register.filter(name="add_classes")
def add_classes(value, arg):
    classes = value.field.widget.attrs.get("class", "")

    if classes:
        classes = classes.split(" ")
    else:
        classes = []

    new_classes = arg.split(" ")
    for c in new_classes:
        if c not in classes:
            classes.append(c)

    return value.as_widget(attrs={"class": " ".join(classes)})


@register.simple_tag
def gravatar_url(email):
    email = email.strip()
    return f"https://www.gravatar.com/avatar/{(hashlib.md5(email.lower().encode('utf-8')).hexdigest())}"
