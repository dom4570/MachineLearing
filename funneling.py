import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# print(visits.head(5))
# print(cart.head(5))
# print(checkout.head(5))
# print(purchase.head(5))

data = (pd.merge(visits,cart, how = 'left'))
# print(data)

len_data = len(data)
# print(len_data)

null_cart_time = (data[data.cart_time.isnull()])
len_null_cart_time = len(null_cart_time)

# print(len_null_cart_time)

not_visited = float(len_null_cart_time) / float(len_data)

print(not_visited)

#LEFTMERGE

cart_checkout = cart.merge(checkout, how = 'left')
# print(cart_checkout)
len_cart_checkout = len(cart_checkout)


null_check_out = (cart_checkout[cart_checkout.checkout_time.isnull()])
# print(null_check_out)

len_null_check_out = len(null_check_out)
print(len_null_check_out)

perecentage_of_no_check_out = float(len_null_check_out) / float(len_cart_checkout)

print(perecentage_of_no_check_out)

all_data = data.merge(cart_checkout, how = 'left').merge(purchase, how = 'left')

print(all_data.head(5))

reached_checkout = all_data[~all_data.checkout_time.isnull()]

checkout_not_purchase = all_data[(all_data.purchase_time.isnull()) & (~all_data.checkout_time.isnull())]

checkout_not_purchase_percent = float(len(checkout_not_purchase)) / float(len(reached_checkout))

print(checkout_not_purchase_percent)

print("{} percent of users who visited the page did not add a t-shirt to their cart".format(round(not_visited*100, 2)))
print("{} percent of users who added a t-shirt to their cart did not checkout".format(round(perecentage_of_no_check_out*100, 2)))
print("{} percent of users who made it to checkout  did not purchase a shirt".format(round( checkout_not_purchase_percent*100, 2)))


all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

final_table = all_data.merge(purchase,how = 'inner')

print(all_data)
print(final_table)
print(all_data.time_to_purchase.mean())
