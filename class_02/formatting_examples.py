print('{:d}'.format(42))
print('{:f}'.format(42))
# print('{:s}'.format(42))   # If it is a number, do not force it to string. It's unnecessary
print('{:s}'.format('42'))
print('{:b}'.format(42))
print('{:%}'.format(0.42))

print('{0:05.2f}'.format(2))
print('{:05.2f}'.format(2))
print('{0:05.2f}'.format(2))

print('{:05d}'.format(122))
print('{:5d}'.format(122))
print('{0:5d}'.format(122))
print('{0:05d}'.format(122))
print('{0:05.2f}'.format(122))