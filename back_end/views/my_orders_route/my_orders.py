import functools

from back_end.model.order.oredr_model import orders
from back_end.model.item.item_model import Menu_Item
from flask import render_template, redirect, url_for,session
from back_end.model.users.users_model import Users
def my_orders(user_id):
    try:
        user = Users.get(Users.user_id == session['user_id'])
        my_order = Menu_Item.select(Menu_Item, orders).join(orders, on=(orders.item_id == Menu_Item.menu_id)).where(
            orders.user_id == user_id)
        order_dict = {}
        for i in my_order:
            sample = {}
            sample.update(i.__dict__['orders'].__dict__['__data__'])
            sample.update(i.__dict__['__data__'])
            sample.update({'bigger':False})
            if i.__dict__['orders'].number in order_dict:
                order_dict[i.__dict__['orders'].number].append(sample)
            else:
                order_dict[i.__dict__['orders'].number] = [sample]
        for i, j in order_dict.items():
            ti = j[0]['ready_time']
            big = j[0]
            for x in j:

                if x['ready_time'] > ti:
                    big = x
            big.update({'bigger':True})

        print(order_dict)
        return render_template('my-orders.html', orders=order_dict,user=user)
    except KeyError:
        return render_template('signIn.html')
