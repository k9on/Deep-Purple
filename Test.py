import tensorflow as tf
import numpy as np

# xy = np.loadtxt('07train.txt', unpack=True)
# x_data = np.transpose(xy[0:-1])
# y_data = np.reshape(xy[-1], (4, 1))

x_data = [[1,0],[0,1]]
y_data = [[1,0],[0,1]]

X = tf.placeholder(tf.float32, name='x-input')
Y = tf.placeholder(tf.float32, name='y-input')

w1 = tf.Variable(tf.random_uniform([2, 5], -1.0, 1.0), name='weight1')
w2 = tf.Variable(tf.random_uniform([5, 10], -1.0, 1.0), name='weight2')
w3 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0), name='weight3')
w4 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0), name='weight4')
w5 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0), name='weight5')
w6 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0), name='weight6')
w7 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0), name='weight7')
w8 = tf.Variable(tf.random_uniform([10, 2], -1.0, 1.0), name='weight8')

b1 = tf.Variable(tf.zeros([5]), name="Bias1")
b2 = tf.Variable(tf.zeros([10]), name="Bias2")
b3 = tf.Variable(tf.zeros([10]), name="Bias3")
b4 = tf.Variable(tf.zeros([10]), name="Bias4")
b5 = tf.Variable(tf.zeros([10]), name="Bias5")
b6 = tf.Variable(tf.zeros([10]), name="Bias6")
b7 = tf.Variable(tf.zeros([10]), name="Bias7")
b8 = tf.Variable(tf.zeros([2]), name="Bias8")

L2 = tf.nn.relu(tf.matmul(X, w1) + b1)
L3 = tf.nn.relu(tf.matmul(L2, w2) + b2)
L4 = tf.nn.relu(tf.matmul(L3, w3) + b3)
L5 = tf.nn.relu(tf.matmul(L4, w4) + b4)
L6 = tf.nn.relu(tf.matmul(L5, w5) + b5)
L7 = tf.nn.relu(tf.matmul(L6, w6) + b6)
L8 = tf.nn.relu(tf.matmul(L7, w7) + b7)

hypothesis = tf.sigmoid(tf.matmul(L8, w8) + b8)

with tf.name_scope('cost') as scope:
    cost = tf.reduce_mean(tf.square(hypothesis- Y))
    #cost_summ = tf.summary.scalar("cost", cost)

with tf.name_scope('train') as scope:
    a = tf.Variable(0.1)
    optimizer = tf.train.GradientDescentOptimizer(a)
    train = optimizer.minimize(cost)

# w1_hist = tf.summary.histogram("weights1", w1)
# w2_hist = tf.summary.histogram("weights2", w2)
#
# b1_hist = tf.summary.histogram("biases1", b1)
# b2_hist = tf.summary.histogram("biases2", b2)
#
# y_hist = tf.summary.histogram("y", Y)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)

    # merged = tf.summary.merge_all()
    # writer = tf.summary.FileWriter("/tmp/test_board", sess.graph)

    for step in range(20000):
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            # summary = sess.run(merged, feed_dict={X: x_data, Y: y_data})
            # writer.add_summary(summary, step)
            print (step, sess.run(cost, feed_dict={X: x_data, Y: y_data}))#, sess.run(w1), sess.run(w2))

    print(sess.run(hypothesis, feed_dict= {X:x_data}))
    print(y_data)