import crypt


t = crypt.crypt('previ$321',crypt.METHOD_MD5)
print(t)
u = crypt.crypt('previ$321',crypt.METHOD_SHA256)
print(u)

print('old')
print('$1$dEuxKjpq$xr9Yxk/bFMANXqCIF0p061')
print('new')
print('$1$dEuxKjpq$xr9Yxk/bFMANXqCIF0p061')