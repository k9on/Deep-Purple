import tensorflow as tf
import LoadData as LD
import numpy as np

ld = LD.pgn_reader('./test/test.pgn')

index, input,output,r = ld.get_data()

print(len(index))

print(index, input,output,r)
# 학습데이터 확보

# 그래프 생성

# 결과값 지정

# 학습데이터 - 결과값 = 코스트

# 코스트 함수의 Gradient Descent 방법 지정

# Train 함수

# 세션 생성

# 학습

# 학습결과 ( cost, acculate )