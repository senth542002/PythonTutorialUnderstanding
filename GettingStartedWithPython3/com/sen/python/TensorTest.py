'''
Created on 29-Dec-2017

@author: senthilkumar
'''
from com.sen.python.PythonFunctions import Summation
from test.test_xml_etree import summarize

if __name__ == '__main__':
    pass

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow')
sess = tf.Session()
print(sess.run(hello))

def plus(a,b):
    summ = a+b;
    return (summ, a)

print(plus(2, 3))

sumInstance = Summation('Summation')
print(sumInstance.sum(2, 3))
print(sumInstance.hello() * 2)

summation , a = plus(2, 3)

print(summation)
