'''
# Conda for TensorFlow
where anaconda
where python
conda --version
conda info

# Know about Environment 
conda info -e

#Create Env
conda create --name temp_conda

#Python
conda create --n temp_conda python=3.7
# with Lib
conda create --n temp_conda python=3.7 numpy keras

#get info of env
conda activate conda_python
pip list
#install tensorflow
pip install tensorflow
conda env remove -n temp_conda

'''

import tensorflow as tf
a = tf.constant(3.0, dtype=tf.float32)
print(a)

b = tf.constant(4.0)
print(b)

total = a*b
print(total)

c = tf.constant([1,2,3,4,5,6,7,8],shape=[2,4])
print(c)
sess = tf.Session()
print(sess.run(a))
print(sess.run(b))
print(sess.run(c))
print(sess.run(total))

#x  = tf.constant([[1,1,1][1,1,1]])
#print(x)
#print(sess.run(tf.reduce_sum(x)))
#print(sess.run(tf.reduce_sum(x,0)))
#tf.reduce_sum(x,1)
#tf.reduce_sum(x,[0,1])

#print(sess.run({'ab':(a,b), 'total':total}))


a = tf.add(1,2, name="Add 1 and 2")
b = tf.multiply(a,3, name="MUL A and 2")
c = tf.add(4,5,name="Add 4 and 5")
d = tf.multiply(c,6)
e = tf.multiply(4,5)
f = tf.div(c,6)
g = tf.add(b,d)
h = tf.multiply(g,f)

with tf.Session() as sess:
    print(sess.run(h))

with tf.Session() as sess:
    writer = tf.summary.FileWriter("output",sess.graph)
    print(sess.run(h))
    writer.close()



