import json

from flask import render_template, Flask, request, jsonify, redirect, url_for, session, g
from back_end.model.item.item_model import Menu_Item


def shop_card():
    cards = request.get_json()
    card_list = {}
    for i in cards:
        card_list[Menu_Item.get(Menu_Item.menu_id == str(i).split('-')[1])] = int(cards[i])
    print(card_list)
    return render_template('shop-card.html', cards=card_list)
