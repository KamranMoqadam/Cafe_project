from back_end.model.category.category_model import Category
from flask import render_template, request, jsonify
from back_end.model.item.item_model import Menu_Item
from back_end.model.category_item.category_item_model import Category_item


def home():
    categorys = Category.select()
    return render_template('home.html', categorys=categorys)


def get_items():
    items = Menu_Item.select().join(Category_item, on=(Category_item.menu_item_id == Menu_Item.menu_id)).where(
        Category_item.category_id == 1)

    return render_template('items.html', items=items)


