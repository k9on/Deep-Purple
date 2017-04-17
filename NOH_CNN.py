import chess
import tensorflow as tf
import Board2Array as BA
import LoadData as LD
import numpy as np

testPgn = LD.pgn_reader('./test/test.pgn')
pgnIndex, pgnInput, pgnOutput, pgnResult = testPgn.get_data()

print(pgnOutput)

# b = chess.Board()

b = pgnInput



t =[]
a =[]
ret = []

for itr in range(len(pgnInput)):
    t.append(np.eye(8))   #board 한판

    a.append(np.zeros((13,8,8)))  #13*8*8


    i = 0  # 행
    j = 0  # 열
    length = 0

    for row in range(8):
        for col in range(8):
            tmp = b[itr][row * 8 + col]
            t[itr][i][j] = tmp
            j += 1
            length += 1
            if col == 7:
                j = 0
                i += 1


    for step in range(13):
        for row in range(8):
            for col in range(8):
                tmp = t[itr][row][col]
                if np.any(tmp == step):
                    a[itr][step][row][col] = 1
                else:
                    a[itr][step][row][col] = 0

    tmparray = np.transpose(a[itr], (1, 2, 0))


    ret.append(tmparray)



# ba = BA.Board2Array()
#
# b = ba.board2array(b)




#hyper parameters
learning_rate = 0.001
training_epochs = 1
batch_size = 23

#dropout (keep_prob) rate 0.7~0.5 on training, but should be 1 for testing
keep_prob = tf.placeholder(tf.float32)

#input place holders
X = tf.placeholder(tf.float32, [None, 8, 8, 13]) # 8 * 8 * 13  grid 64, types 13
# X_input = tf.reshape(X, [-1, 8, 8, 13]) # input 보드판
Y = tf.placeholder(tf.float32, [None, 64])


W1 = tf.Variable(tf.random_normal([5, 5, 13, 64], stddev=0.01))
# Conv          ->(?, 8, 8, 64)
L1 = tf.nn.conv2d(X, W1, strides=[1, 1, 1, 1], padding='SAME')
L1 = tf.nn.relu(L1)



W2 = tf.get_variable("W1", shape=[8 * 8 * 64, 4],
                     initializer = tf.contrib.layers.xavier_initializer())
L1 = tf.reshape(L1 , [-1, 8 * 8 * 64])
b = tf.Variable(tf.random_normal([4]))
hypothesis = tf.matmul(L1, W2) + b

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits= hypothesis, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# initialize
sess = tf.Session()
sess.run(tf.global_variables_initializer())


# train my model
print('learning stared. It takes sometimes.')
for epoch in range(training_epochs):
    avg_cost =0
    total_batch = batch_size

    for i in range(23):
        batch_xs, batch_ys = ret, pgnOutput  # batch로 들거가야할 입력값 X 와 출력값 Y를 담는다
        feed_dict = {X: batch_xs, Y: batch_ys}
        c, _, = sess.run([cost, optimizer], feed_dict = {X: ret, Y:batch_ys})
        avg_cost += c / total_batch
        print('train:', '%04d' % (i + 1), 'cost = ', c)
        # print('Epoch:', '%04d' %(epoch+1), 'cost = ', '{:9}'.format(avg_cost))
print('Learning Finished!')

correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# print('Accuracy:', sess.run(accuracy, feed_dict={X: feed_dict}))