def solution(s):
    s = s.replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ")
    reversed_s = s[::-1]
    ss = reversed_s.split()
    reversed_ss = ss[::-1]
    
    return reversed_ss