import datetime
import uuid

from flask import request, session, jsonify
from back_end.model.users.users_model import Users
from back_end.model.item.item_model import Menu_Item
from back_end.model.order.oredr_model import orders


def checkout():
    items = request.get_json()
    order_list = []

    try:
        uid = str(uuid.uuid4()).split('-')[0]
        for i in items:
            item: Menu_Item = Menu_Item.get(Menu_Item.menu_id == str(i).split('-')[1])
            serv = datetime.timedelta(hours=int(str(item.serving_time).split(':')[0]),
                                      minutes=int(str(item.serving_time).split(':')[1]))
            cook = datetime.timedelta(hours=int(str(item.cooking_time).split(':')[0]),
                                      minutes=int(str(item.cooking_time).split(':')[1]))
            dict_item = {'user_id': Users.get(Users.user_id == session['user_id']),
                         'item_id': item,
                         'status': 'cooking',
                         'number': uid,
                         'takeaway': True,
                         'count':items[i],
                         'ready_time': datetime.datetime.now() + cook + serv,
                         }
            order_list.append(dict_item)

        orders.save_orders(order_list)
        return 'success'
    except KeyError:
        return jsonify({'message': 'you must login'}), 403
