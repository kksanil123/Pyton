matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

tmatrix = [[], [], [], []]
[tmatrix[i].append(matrix[j][i]) for i in range(0, len(matrix[0])) for j in range(0, len(matrix))]
print(tmatrix)

# tmatrix = [[], [], [], []]
# for i in range(0, len(matrix[0])):
#     for j in range(0, len(matrix)):
#         tmatrix[i].append(matrix[j][i])
#
# print(tmatrix)
