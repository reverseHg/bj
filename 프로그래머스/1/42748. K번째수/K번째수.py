def solution(array, commands):
    answer=[]
    for a in commands:
      i,j,k=a
      arr=array[i-1:j]
      answer.append(sorted(arr)[k-1])
    return answer