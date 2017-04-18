import tensorflow as tf
import LoadData as LD
import numpy as np

def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))

def model(X, w, w5, w_o, p_keep_conv, p_keep_hidden):
    l1 = tf.nn.relu(tf.nn.conv2d(X, w,strides=[1, 1, 1, 1], padding='SAME')) # 8 8 31
    l1 = tf.reshape(l1, [-1, w5.get_shape().as_list()[0]])
    l5 = tf.nn.relu(tf.matmul(l1, w5))
    pyx = tf.matmul(l5, w_o)
    return pyx

def play():
    ld = LD.pgn_reader('./test/test4.pgn')

    index, pboard, board, rboard, result = ld.get_data()
    print(index)
    print("---------------")
    print(board)
    print(rboard)
    print("---------------")
    print(np.shape(board))
    input1 = np.reshape(board,[-1,8,8,13])
    input2 = np.reshape(rboard,[-1,8,8,13])
    # input1 = board # np.reshape(board,[-1,8,8,13])
    # input2 = rboard # np.reshape(rboard,[-1,8,8,13])
    print(index[0])
    print(pboard[0])
    print("--------------------------------")
    print(input1[0])
    print("--------------------------------")
    print(input2[0])
    trainX = input1
    trainY = input2
    trX = trainX
    trY = trainY
    teX = trainX
    teY = trainY

    X = tf.placeholder("float", [None, 8, 8, 13])
    Y = tf.placeholder("float", [None, 8, 8, 13])

    w = init_weights([4, 4, 13, 20])      # 4x4x13 conv 81 outputs
    # w2 = init_weights([2, 2, 81, 81])     # 2x2x81 conv, 81 outputs
    # w3 = init_weights([2, 2, 81, 81])    # 2x2x81 conv, 81 outputs
    # w4 = init_weights([2, 2, 81, 81])    # 2x2x81 conv, 81 outputs
    w5 = init_weights([8*8*20, 100])    # 81 필터에 8*8 이미지
    w_o = init_weights([100, 1])         # FC 625 inputs, 4 outputs (labels)

    p_keep_conv = tf.placeholder("float")
    p_keep_hidden = tf.placeholder("float")

    py_x = model(X, w, w5, w_o, p_keep_conv, p_keep_hidden)
    py_y = model(Y, w, w5, w_o, p_keep_conv, p_keep_hidden)
    cost_ = py_x  - 10 - py_y
    cost_a = tf.square(cost_)

    cost = tf.reduce_mean(tf.square(cost_))

    a = 0.001
    train_op = tf.train.GradientDescentOptimizer(a).minimize(cost)

    saver = tf.train.Saver()

    modelname = "./mymodel/model.ckpt"

    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver.restore(sess, modelname)
        print(sess.run(w))
        for i in range(10000):
            #print(a)
            sess.run(train_op, feed_dict={X: trX, Y: trY, p_keep_conv: 0.8, p_keep_hidden: 0.5})
            print (i,sess.run(cost, feed_dict={X: trX, Y: trY, p_keep_conv: 0.8, p_keep_hidden: 0.5}))
            if i%200 == 0:
                print("Saved!!!!")
                save_path = saver.save(sess, modelname)
        print(sess.run(py_x, feed_dict={X:trX,p_keep_conv: 1., p_keep_hidden: 1.}))
        print(sess.run(py_y, feed_dict={Y: trY, p_keep_conv: 1., p_keep_hidden: 1.}))
        print(len(trX))
        #save_path = saver.save(sess, modelname)
        print(sess.run(py_y, feed_dict={Y: trX[1:3], p_keep_conv: 1., p_keep_hidden: 1.}))

        return sess.run(py_x, feed_dict={X:trX,p_keep_conv: 1., p_keep_hidden: 1.})

# play()