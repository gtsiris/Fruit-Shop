# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import shop

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    if not fruitShops:  # Check if there are available fruit shops
        print("Not available fruit shop to serve you")
        return None
    elif not orderList:  # Check if the order is empty
        print("You don't want to buy fruits")
        return None
    else:
        # Initialize the best option as the first available fruit shop
        cheapestShop, minimumCost = fruitShops[0], fruitShops[0].getPriceOfOrder(orderList)
        for fruitShop in fruitShops:  # For each available fruit shop
            cost = fruitShop.getPriceOfOrder(orderList)  # Calculate the cost of the order
            if cost < minimumCost:  # Check if it is smaller than the current minimum cost
                cheapestShop, minimumCost = fruitShop, cost  # Update both the cheapest shop and the minimum cost
        return cheapestShop  # Return the best option for this order

if __name__ == '__main__':
  "This code runs when you invoke the script from the command line"
  orders = [('apples',1.0), ('oranges',3.0)]
  dir1 = {'apples': 2.0, 'oranges':1.0}
  shop1 =  shop.FruitShop('shop1',dir1)
  dir2 = {'apples': 1.0, 'oranges': 5.0}
  shop2 = shop.FruitShop('shop2',dir2)
  shops = [shop1, shop2]
  print "For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName()
  orders = [('apples',3.0)]
  print "For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName()
