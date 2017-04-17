import tensorflow as tf

num_example =0

#hyper parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100

#dropout (keep_prob) rate 0.7~0.5 on training, but should be 1 for testing
keep_prob = tf.placeholder(tf.float32)

#input place holders
X = tf.placeholder(tf.float32, [None, 832]) # 8 * 8 * 13  grid 64, types 13
X_input = tf.reshape(X, [-1, 8, 8, 13]) # input 보드판
Y = tf.placeholder(tf.float32, [None, 64])


W1 = tf.Variable(tf.random_normal([3, 3, 13, 64], stddev=0.01))
# Conv          ->(?, 8, 8, 64)
L1 = tf.nn.conv2d(X_input, W1, strides=[1, 1, 1, 1], padding='SAME')
L1 = tf.nn.relu(L1)

W2 = tf.get_variable("W1", shape=[8 * 8 * 64, 64],
                     initializer = tf.contrib.layers.xavier_initializer())
b = tf.Variable(tf.random_normal[64])
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
    total_batch = int( num_example/ batch_size)

    for i in range(total_batch):
        b


correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy:', sess.run(accuracy, feed_dict={X: }))