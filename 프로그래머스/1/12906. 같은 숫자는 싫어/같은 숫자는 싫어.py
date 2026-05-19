def solution(arr):
    stack=[]
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            stack.append(arr[i])
    stack.append(arr[-1])
    return stack