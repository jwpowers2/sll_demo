#!/usr/bin/python
# FIFO stack, classes Call, CallCenter
import uuid
import time
from linked_list import LinkedList


STOCKS = [['GOOGL', 'Alphabet', '1100'],
          ['GE', 'General Electric', '14.5'],
          ['AMZN', 'Amazon', '1500'],
          ['TSLA', 'Tesla', '333'],
          ['TXT', 'Textron', '59'],
          ['F', 'Ford', '10'],
          ['BABA', 'Alibaba', '190'],
          ['F5', 'F5 networks', '50']]

class Stock(object):

    def __init__(self, name, companyname, price):

	self.name = name
	self.companyname = companyname
	self.price = price

class SLL(object):

    def __init__(self):

	self.stocks = LinkedList()
	self.queue_size = 0

    def add(self, stock):

	self.stocks.addNode(stock)
        return self

    def find(self, name):

	print(self.stocks.findNode(name))

    def remove(self,name):

        self.stocks.removeNode(name)

    def info(self):
        self.stocks.printNode()

    def rotate_queue(self):
	self.stocks.rotate_queue()

class StockSLL(object):

    def __init__(self):

        self.stocklist = SLL()

    def spawn(self, arr):

        
	for stock in arr:
	    newstock = Stock(stock[0],stock[1],stock[2])
            self.stocklist.add(newstock)

    def info(self):
        self.stocklist.info()

    def find(self, name):
        self.stocklist.find(name)

    def remove(self, name):
        self.stocklist.remove(name)

    def rotate_queue(self):
	self.stocklist.rotate_queue()

s = StockSLL()
s.spawn(STOCKS)
s.info()
print "****************"
s.rotate_queue()
s.info()
#print "******************"
#s.rotate_queue()
