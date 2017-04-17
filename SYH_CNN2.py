import tensorflow as tf
import LoadData_1 as LD
import numpy as np

batch_size = 128
test_size = 256

def my_round(x):
    temp = x - round(x)
    if temp >= 0.5:
        return round(x) + 1
    else : return round(x)

def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))

def model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden):
    l1a = tf.nn.relu(tf.nn.conv2d(X, w,strides=[1, 1, 1, 1], padding='SAME')) #  8 8 32
    print(l1a)
    l1 = tf.nn.max_pool(l1a, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME') # 4 4 32
    print(l1)
    l1 = tf.nn.dropout(l1, p_keep_conv)
    #l2a = tf.nn.relu(tf.nn.conv2d(l1, w2,strides=[1, 1, 1, 1], padding='SAME')) # 4 4 64
    #print(l2a)
    #l2 = tf.nn.max_pool(l2a, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME') # 2 2 64
    #l2 = tf.nn.dropout(l2, p_keep_conv)
    #print(l2)
    #l3a = tf.nn.relu(tf.nn.conv2d(l2, w3,strides=[1, 1, 1, 1], padding='SAME')) # 2 2 128
    #print(l3a)
    #l3 = tf.nn.max_pool(l3a, ksize=[1, 1, 1, 1],strides=[1, 1, 1, 1], padding='SAME') # 1 1 128
    #print(l3)
    #l3 = tf.reshape(l3, [-1, w4.get_shape().as_list()[0]])
    #print(l3)
    l3 = tf.reshape(l1, [-1, w4.get_shape().as_list()[0]] )
    l3 = tf.nn.dropout(l3, p_keep_conv)
    l4 = tf.nn.relu(tf.matmul(l3, w4))

    l4 = tf.nn.dropout(l4, p_keep_hidden)
    print(l4)
    pyx = tf.matmul(l4, w_o)
    print(pyx)
    return pyx

ld = LD.pgn_reader('./test/test.pgn')

index, input, output, r = ld.get_data()
input = np.reshape(input,[-1,8,8,13])

print(index[0])
print(input[0])
print(output[0])

trainX = input
trainY = output
trX = trainX
trY = trainY
teX = trainX
teY = trainY

X = tf.placeholder("float", [None, 8, 8, 13])
Y = tf.placeholder("float", [None, 4])

w = init_weights([2, 2, 13, 32])      # 3x3x13 conv, 32 outputs
w2 = init_weights([2, 2, 32, 64])     # 3x3x32 conv, 64 outputs
w3 = init_weights([2, 2, 64, 128])    # 3x3x64 conv, 128 outputs
w4 = init_weights([32*4*4, 625]) # 128의 필터에 4 * 4 이미지
w_o = init_weights([625, 4])         # FC 625 inputs, 4 outputs (labels)

p_keep_conv = tf.placeholder("float")
p_keep_hidden = tf.placeholder("float")

py_x = model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden)

cost = tf.reduce_mean(tf.square(py_x - Y))
train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)
predict_op = py_x

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for i in range(3000):

        sess.run(train_op, feed_dict={X: trX, Y: trY,
                                          p_keep_conv: 0.8, p_keep_hidden: 0.5})

        print (i,sess.run(cost, feed_dict={X: trX, Y: trY,
                                            p_keep_conv: 0.8, p_keep_hidden: 0.5}))
    print(sess.run(py_x, feed_dict={X:trX,p_keep_conv: 1., p_keep_hidden: 1.}))
    print(teY)
print(index)
print(len(teY))