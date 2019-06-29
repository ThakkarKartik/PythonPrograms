import tensorflow as tf
#x = tf.constant(3.0, dtype=tf.float32)
#y = tf.constant(4.0, dtype=tf.float32)

#x = tf.Variable(3.0, dtype=tf.float32)
#y = tf.Variable(4.0, dtype=tf.float32)

a = tf.multiply(x,x)
b = tf.multiply(a,y)
c = tf.add(b,y)
d = tf.add(c,2)

with tf.Session() as sess:
    sess.run(x.initializer)
    sess.run(y.initializer)
    print(sess.run(d))
sess.close()

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

z = x + y 

sess = tf.Session()
print("\n\n")
print(sess.run(z,feed_dict={x:3,y:4.5}))
print(sess.run(z,feed_dict={x:[1,3],y:[2,4]}))

a = tf.constant([1,2,3,4,5,6],shape=[2,3])
b = tf.constant([7,8,9,10,11,12],shape=[3,2])

product = tf.matmul(a,b)
sum = tf.add(a,tf.transpose(b))

sess = tf.Session()
print("\n\n")
print(sess.run(product))

print("\n\n")
print(sess.run(sum))

