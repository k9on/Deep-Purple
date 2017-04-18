import time

arr = [0]*100000
tmp = 0
i = 0

for i in range(0,99999):
      arr[i] = tmp
      tmp +=1

tmp = 0
Now = int(time.time()*1000)
i = 0

while i < 100000 :
      if arr[i] == 50000:
            i = 0
            tmp +=1
            continue
      if tmp == 100 :
            last = int(time.time() * 1000)
            break
      i +=1
print(last - Now)

#include
#include <stdio.h>
#include <Windows.h>
# int main() {
#
# 	int arr[100000];
# 	int i, tmp = 0;
# 	LONGLONG now, last, freq;
# 	QueryPerformanceFrequency((LARGE_INTEGER*)(&freq));
# 	for (i = 0; i < 100000; i++) {
# 		arr[i] = tmp;
# 		tmp += 1;
# 	}
#
# 	tmp = 0;
# 	QueryPerformanceCounter((LARGE_INTEGER*)&now);
#
# 	for (i = 0; i < 100000; i++) {
#
# 		if (arr[i] == 50000) {
# 			tmp += 1;
# 			i = 0;
# 		}
# 		if (tmp == 100) {
# 			QueryPerformanceCounter((LARGE_INTEGER*)&last);
# 			break;
# 		}
#
# 	}
#
#
# 	printf("찾는 데 걸린 시간 : %f\n", (float)(last - now) / freq * (float)1000.0);
# 	getchar();
#
# 	return 0;
# }
