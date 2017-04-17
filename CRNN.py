'''
출발 명령어와 도착 명령어를 받기 위한 모델을 학습시킬
CRNN
'''

import tensorflow as tf
import LoadData as LD

#testPgn = LD.pgn_reader('./test/test.pgn')
testPgn = LD.pgn_reader('./test/test.pgn')
pgnIndex, pgnInput, pgnOutput, pgnResult = testPgn.get_data()


#hyper parameters
learning_rate=0.00000001
training_epochs = 1 #15
batch_size =100


X = tf.placeholder(tf.float32, [None,8,8,9]) #체스에서 8X8X9 이미지를 받기 위해 64
#X_img = tf.reshape(X,[-1,8,8,9]) #img 8x8x9 (9feature)

Y= tf.placeholder(tf.float32,[None, 64])

#Layer1 ImgIn shape=(?, 8, 8, 9) ?는 N개의 이미지가 들어온다고 볼 수 있다.
W1 = tf.Variable(tf.random_normal([2, 2, 9,32],stddev=0.01)) # 32개의 필터를 사용

L1 = tf.nn.conv2d(X , W1, strides=[1,1,1,1], padding='VALID')
#8x8의 2x2 filter에 stride=1 일때 result는 7x7xfeatur map의 크기인 7x7x32 =1568
L1 = tf.nn.relu(L1)

#Conv 28x28에서 strides = [1,1,1,1] , padding = 'SAME' 일경우 결과 28x28
#               strides = [1,2,2,1] , padding = 'VALID'일경우 14x14

AffineL1 = tf.reshape(L1 , [-1, 7*7*32])
W2 = tf.get_variable("W1", shape = [7*7*32, 64], initializer = tf.contrib.layers.xavier_initializer())
b = tf.Variable(tf.random_normal([64]))
hypothesis = tf.matmul(AffineL1,W2)+b



#define cost/Loss & optimizer

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels= Y))
optimizer = tf.train.AdamOptimizer(learning_rate= learning_rate).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

#train my model
print("Learning start. It tackes sometime.")

for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = 20 #int(mist.train.num_examples / batch_size) 현재 한번만 학습하므로

    for i in range(total_batch):
        batch_xs, batch_ys =pgnInput,pgnOutput[0]#batch로 들거가야할 입력값 X 와 출력값 Y를 담는다
        feed_dict = {X: batch_xs,Y: batch_ys }
        c, _, = sess.run([cost,optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch
        print('Epoch:', '%04d' % (epoch + 1), 'cost = ', '{:9}'.format(avg_cost))
   # print('Epoch:', '%04d' %(epoch+1), 'cost = ', '{:9}'.format(avg_cost))
print('Learning Finished!')

#Test model and check accuracy
correct_prediction = tf.equal(tf.argmax(hypothesis, 1) , tf.argmax(Y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#print('Accuracy : ', sess.run(accuracy, feed_dict={X: minist.test.images, Y:mnist.test.labels}))