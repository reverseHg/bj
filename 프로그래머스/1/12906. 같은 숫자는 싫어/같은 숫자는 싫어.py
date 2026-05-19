def solution(arr):
    answer=[] #빈 리스트 생성
    for i in range(len(arr)-1): #배열 크기만큼 반복
        if arr[i]!=arr[i+1]: #현재 수와 다음 수가 같은지 확인
            answer.append(arr[i]) #중복이 아니라면 리스트에 현재 수 추가
    answer.append(arr[-1]) #마지막 수 리스트에 추가
    return answer