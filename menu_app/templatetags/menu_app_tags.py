from menu_app.models import MenuItem
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('menu_app/menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None):

    def get_menu(menu_item: str = None, child_items: list = None):
        if not menu_item:
            menu = list(items.filter(parent=None))
        else:
            menu = list(items.filter(parent__name=menu_item))
        menu.append(child_items)
        try:
            return get_menu(items.get(name=menu_item).parent.name, menu)
        except AttributeError:
            return get_menu(child_items=menu)
        except ObjectDoesNotExist:
            return menu
    items = MenuItem.objects.filter(menu__name=menu_name)
    if menu_name == menu_item:
        return {'menu': get_menu()}
    else:
        return {'menu': get_menu(menu_item)}

    
