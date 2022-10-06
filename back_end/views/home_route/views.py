import functools
import json

from back_end.model.category.category_model import Category
from flask import render_template, request, jsonify
from back_end.model.item.item_model import Menu_Item
from back_end.model.category_item.category_item_model import Category_item
from back_end.model.users.users_model import Users
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

def home():
    categorys = Category.select()
    user = None
    try:
     user = Users.get(Users.user_id == session['user_id'])
    except KeyError:
      pass
    return render_template('main.html', categorys=categorys, user=user)


def get_items(cat_id):
    items = Menu_Item.select().join(Category_item, on=(Category_item.menu_item_id == Menu_Item.menu_id)).where(
        Category_item.category_id == cat_id).dicts()
    lst = []
    for q in items:
        lst.append(q)
    return render_template('items.html', items=items)
