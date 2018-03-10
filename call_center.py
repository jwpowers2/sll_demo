#!/usr/bin/python
# FIFO stack, classes Call, CallCenter
import uuid
import time
from linked_list import LinkedList


class Call(object):

    def __init__(self, name, phone, reason):

	self.name = name
	self.phone_number = phone
	self.reason = reason
        self.uid = uuid.uuid4()
	self.time_of_call = time.time()	

    def display(self):

        print "{} {} reason: {} time: {} uid: {}".format(self.name, self.phone_number, self.reason, self.time_of_call, self.uid)


class CallCenter(object):

    def __init__(self):

	self.calls = LinkedList()
	self.queue_size = 0

    def add(self, call):

	self.calls.addNode(call)
        return self

    def find(self, name):

	print(self.calls.findNode(name))

    def remove(self,name):

        self.calls.removeNode(name)

    def info(self):
        self.calls.printNode()

call1 = Call('ET', '222-2222', 'call home')
call2 = Call('The Daleks', '5555555', 'kill the Doctor!')
call3 = Call('Blob', '222-2222', 'cheetos')
call4 = Call('Wayne Newton', '5555555', 'plugs')

callcenter = CallCenter()
callcenter.add(call1).add(call2).add(call3).add(call4)
callcenter.info()
callcenter.find('Blob')
callcenter.remove('ET')
callcenter.info()
#callcenter.info()
#callcenter.add(call2)
#callcenter.remove()
#callcenter.info()
#callcenter.sort_by_time()
