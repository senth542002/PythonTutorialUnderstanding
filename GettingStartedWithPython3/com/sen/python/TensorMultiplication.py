'''
Created on 29-Dec-2017

@author: senthilkumar
'''

if __name__ == '__main__':
    pass

import tensorflow as tf

x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

result = tf.multiply(x1, x2)

#one way to invoke interactive session
# sess = tf.Session()
# 
# print(sess.run(result))
# sess.close()

#second way to invoke interactive session
config=tf.ConfigProto(log_device_placement=True)
config=tf.ConfigProto(allow_soft_placement=True)
with tf.Session() as sess:
    output = sess.run(result)
    print(output)