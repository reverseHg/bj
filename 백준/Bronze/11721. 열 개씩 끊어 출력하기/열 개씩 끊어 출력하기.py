a=input()
while True:
  if len(a)>=10:
    print(a[:10])
    a=a[10:]
    continue
  else:
    print(a)
    break

