def VPS(N):
  stack=[]

  for i in N:
    if i=='(':
      stack.append(i)
    else:
      if not stack:
        return False
      stack.pop()
  return len(stack)==0

T= int(input())

for i in range(T):
  N=input()

  if VPS(N)==True:
    print("YES")
  else:
    print("NO")