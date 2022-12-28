'''
[문제 설명]

0 이상의 정수 n이 주어질 때, n의 이진 표현에서 인접한 두 1 사이의 가장 긴 거리를 출력하는 함수, solution을 완성해주세요.
예를 들어, n이 주어질 때의 결과는 다음과 같습니다.

n : 5
n의 이진 표현 : 101
결과 : 2

n : 11
n의 이진 표현 : 1011
결과 : 2

 
[입력 형식]
n은 0 이상 109 이하의 정수입니다.
 

[출력 형식]
n의 이진 표현에서 인접한 두 1 사이의 가장 긴 거리를 int 형식으로 출력합니다.
'''

def solution(n):
    bn = bin(n)[2:]
    cnt = 1
    result = 1

    for i in bn:
        if '1' == i:
            if result < cnt:
                result = cnt
            cnt = 1
        else:
            cnt += 1
    return result
  
# find 함수 이용 
'''
def solution(n):
    b = format(n, 'b')
    a = b.find('1')
    c = b.rfind('1')
    d = c-a-1
    return(d)
'''
