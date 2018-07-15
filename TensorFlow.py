# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 07:25:15 2018

@author: akansal2
"""

import tensorflow as tf



############################################ Basic Program
a = tf.constant(3.0,tf.float32)
b = tf.constant(4.0)
c =a*b
print(c)
sess = tf.Session()
sess.run([a,b])
sess.run([a*b])
sess.close()


################################################ Using with command

a = tf.constant(3.0)
b = tf.constant(4,tf.float32)
c =a*b

with tf.Session() as sess:
    print(sess.run(c))
    
############################################### Drawing Computational grapgh
a = tf.constant(3.0)
b = tf.constant(4,tf.float32)
c =a*b

File_Writer = tf.summary.FileWriter('C://A_stuff//Learning//Machine Learning//Coursera//Deep Learning//Mul_graph',sess.graph)
with tf.Session() as sess:
    print(sess.run(c))
  
############################################# placeholder

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = a+b
sess = tf.Session()
output =sess.run(c,feed_dict={a:[1,2],b:[4,5]})
print(type(output))



############################################## variables and linear function and Grad desc optimizer

#model parameters
W = tf.Variable(-1.0,tf.float32)
b = tf.Variable(2.0,tf.float32)

#Input and output
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#model
model_output = W*X + b

#loss
square_delta = tf.square(model_output - Y)
loss = tf.reduce_sum(square_delta)


#optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


#session
sess = tf.Session()

#initializing all variables
init = tf.global_variables_initializer()

#running session
sess.run(init)
#print(sess.run(loss,feed_dict={X:[1,2,3],Y:[4,5,6]}))

for i in range(1000):
    sess.run(train,feed_dict={X:[4,2,4,4],Y:[1,-1,-2,-3]})


print(sess.run([W,b]))
sess.close()























