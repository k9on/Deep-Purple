import tensorflow as tf
import LoadData as LD
import numpy as np

def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))

def model(X, w,w2,w4,w_o,p_keep_conv, p_keep_hidden):
    l1a = tf.nn.relu(tf.nn.conv2d(X, w,  # l1a shape=(?, 28, 28, 32)
                                  # stride = [ 스킵할 데이터 수, 행의 스킵수, 열의 스킵수, 필터의 스킵수 ]
                                  # 기본적으로 스킵 데이터수 =1, 필터의 스킵 수 = 1
                                  # 로 하여 모든 데이터에 학습하고, 필터를 스킵하여 필터의 기능을 최대한 유지
                                  # padding = same 은 stride가 1일 경우에 input과 output의 크기를 동일하게
                                  # 하도록 padding의 값을 자동 설정하는 것을 의미한다.
                                  strides=[1, 1, 1, 1], padding='SAME'))
    # pooling을 통해 sampling을 진행
    # pooling 사이즈 = 2x2x1 : 1개의 필터 씩, 2 x 2 크기로 풀링
    l1 = tf.nn.max_pool(l1a, ksize=[1, 2, 2, 1],  # l1 shape=(?, 14, 14, 32)
                        # stride의 행과 열이 2씩임으로 output의 크기가 절반씩 줄어들고 필터의 수는 동일
                        strides=[1, 2, 2, 1], padding='SAME')
    # 매개변수로 정의한 keep_conv만큼 노드 부분 활성화
    l1 = tf.nn.dropout(l1, p_keep_conv)

    l2a = tf.nn.relu(tf.nn.conv2d(l1, w2,  # l2a shape=(?, 14, 14, 64)
                                  strides=[1, 1, 1, 1], padding='SAME'))
    l2 = tf.nn.max_pool(l2a, ksize=[1, 2, 2, 1],  # l2 shape=(?, 7, 7, 64)
                        strides=[1, 2, 2, 1], padding='SAME')
    l2 = tf.nn.dropout(l2, p_keep_conv)

    l3a = tf.nn.relu(tf.nn.conv2d(l2, w3,  # l3a shape=(?, 7, 7, 128)
                                  strides=[1, 1, 1, 1], padding='SAME'))
    l3 = tf.nn.max_pool(l3a, ksize=[1, 2, 2, 1],  # l3 shape=(?, 4, 4, 128)
                        strides=[1, 2, 2, 1], padding='SAME')
    # CNN과 FCNN의 인터페이스를 맞춰주기 위해 3차원 배열을 1차원 배열로 변환하여
    # Tensorflow의 계산을 용이하게 하도록함
    # reshape[ -1 = 데이터의 수를 정확하게 모름 , 1차원 배열의 수 = FCNN Layer의 노드당 w수 , 행 * 열 * 필터
    l3 = tf.reshape(l3, [-1, w4.get_shape().as_list()[0]])  # reshape to (?, 2048)
    l3 = tf.nn.dropout(l3, p_keep_conv)
    # FCNN의 계산을 진행
    l4 = tf.nn.relu(tf.matmul(l3, w4))
    # FCNN의 부분학습을 위해 Dropout
    l4 = tf.nn.dropout(l4, p_keep_hidden)

    pyx = tf.matmul(l4, w_o)
    # 최종적인 hypothesis만을 리턴
    return pyx


# 학습데이터 확보

ld = LD.pgn_reader('./test/test.pgn')

index, input, output, r = ld.get_data()

print(len(index))

print(index, input, output, r)

# 그래프 생성

# 결과값 지정

# 학습데이터 - 결과값 = 코스트

# 코스트 함수의 Gradient Descent 방법 지정

# Train 함수

# 세션 생성

# 학습

# 학습결과 ( cost, acculate )