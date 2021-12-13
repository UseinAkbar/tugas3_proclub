# Half Pyramid
pattern = ''
for i in range(5):
    for j in range(i+1):
        pattern += '* '
    if(i == 4):
        break
    pattern += '\n'
print(pattern)

# Half Inverted Pyramid
# pattern = ''
# for i in range(5,0,-1):
#     for j in range(i):
#         pattern += '* '
#     if(i == 1):
#         break
#     pattern += '\n'
# print(pattern)

# Half Pyramid Pattern Mirrored
# pattern = ''
# for i in range(5):
#     for j in range(4-i):
#         pattern += ' '
#     for k in range(i+1):
#         pattern += '*'
#     if(i == 4):
#         break
#     pattern += '\n'
# print(pattern)

# Full Pyramid Pattern
# pattern = ''
# for i in range(5):
#     for j in range(4-i):
#         pattern += ' '
#     for k in range(i+1):
#         pattern += '* '
#     if(i == 4):
#         break
#     pattern += '\n'
# print(pattern)

# Full Pyramid Pattern Mirrored
# pattern = ''
# for i in range(5,0,-1):
#     for j in range(5-i):
#         pattern += ' '
#     for k in range(i):
#         pattern += '* '
#     if(i == 1):
#         break
#     pattern += '\n'
# print(pattern)