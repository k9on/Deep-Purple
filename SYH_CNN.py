import tensorflow as tf
import LoadData as LD
import numpy as np

# 학습데이터 확보

ld = LD.pgn_reader('./test/test.pgn')

index, input, output, r = ld.get_data()
print(input)
print(output)

trainX = input
trainY = output
# sampleX= [[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4],
#           [0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0,9,8,7]]
# sampleY = [[1,2,3,4], [5,6,7,8]]

sampleX = [[1,2],[3,4],[5,6]]
sampleY = [[1],[2],[3]]
#print(output[0][3])

# 그래프 생성

X = tf.placeholder(tf.float32, name='x-input')
Y = tf.placeholder(tf.float32, name='y-input')

w1 = tf.Variable(tf.random_uniform([2, 100], -1.0, 1.0), name='weight1')
w2 = tf.Variable(tf.random_uniform([100, 200], -1.0, 1.0), name='weight2')
w3 = tf.Variable(tf.random_uniform([200, 1], -1.0, 1.0), name='weight3')
# w4 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0), name='weight4')
# w5 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0), name='weight5')
# w6 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0), name='weight6')
# w7 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0), name='weight7')
# w8 = tf.Variable(tf.random_uniform([10, 4], -1.0, 1.0), name='weight8')

b1 = tf.Variable(tf.zeros([100]), name="Bias1")
b2 = tf.Variable(tf.zeros([200]), name="Bias2")
b3 = tf.Variable(tf.zeros([1]), name="Bias3")
# b4 = tf.Variable(tf.zeros([10]), name="Bias4")
# b5 = tf.Variable(tf.zeros([10]), name="Bias5")
# b6 = tf.Variable(tf.zeros([10]), name="Bias6")
# b7 = tf.Variable(tf.zeros([10]), name="Bias7")
# b8 = tf.Variable(tf.zeros([4]), name="Bias8")

L2 = tf.nn.relu(tf.matmul(X, w1) + b1)
L3 = tf.nn.relu(tf.matmul(L2, w2) + b2)
L4 = tf.nn.relu(tf.matmul(L3, w3) + b3)
# L5 = tf.nn.relu(tf.matmul(L4, w4) + b4)
# L6 = tf.nn.relu(tf.matmul(L5, w5) + b5)
# L7 = tf.nn.relu(tf.matmul(L6, w6) + b6)
# L8 = tf.nn.relu(tf.matmul(L7, w7) + b7)
#


a = tf.Variable(0.01)

# 결과값 지정
# hypothesis = tf.nn.relu(tf.matmul(L8, w8) + b8)
hypothesis = L4
# 학습데이터 - 결과값 = 코스트

cost = tf.reduce_mean(tf.square(hypothesis - Y))
# 코스트 함수의 Gradient Descent 방법 지정
optimizer = tf.train.GradientDescentOptimizer(a)

# Train 함수
train = optimizer.minimize(cost)
# 세션 생성
init = tf.initialize_all_variables()


# 학습
with tf.Session() as sess:
    sess.run(init)

    for step in range(20000):
        sess.run(train, feed_dict={X: sampleX, Y: sampleY})
        if step % 200 == 0:
            print (step, sess.run(cost, feed_dict={X: sampleX, Y: sampleY}))

    correct_prediction = tf.equal(tf.floor(hypothesis+0.5), Y)
    print("------------------------------------------")
    #print(sess.run(w1),sess.run(w2))
    print(sess.run(hypothesis, feed_dict={X:sampleX}))
    print(sampleY)

    # accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    # print(sess.run([hypothesis, tf.floor(hypothesis+0.5), correct_prediction], feed_dict={X: x_data, Y: y_data}))
    # print("accuracy", accuracy.eval({X: x_data, Y: y_data}))
# 학습결과 ( cost, acculate )