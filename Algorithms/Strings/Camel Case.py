def camelCase(s):
  res = 1
  s = list(s)
  
  for i in range(len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
      res += 1
      
  return res
  
n = int(input())
s = int(input())
print(camelCase(s))
