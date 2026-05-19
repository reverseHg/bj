def solution(s):
    S=s.lower()
    if S.count('p')==S.count('y'):
        answer = True
    else:
        answer=False
    return answer