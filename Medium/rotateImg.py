import numpy as np

def rotate(matrix):     # use ref new array and replace matrix with value
   length = len(matrix)
   ans = [[0 for _ in range(length)] for _ in range(length)]

   for c in range(length):
      target = matrix[c]
      for r in range(length):
         ans[r][length-1-c] = target[r]

   for r in range(length):
      for c in range(length):
         matrix[r][c] = ans[r][c]
               
   return matrix

def rotate_2(matrix):      # transpose and reverse
   length = len(matrix)

   for i in range(length):
      for j in range(i+1, length):
         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
   
   for i in range(length):
      for j in range(length//2):
         matrix[i][j], matrix[i][length-1-j] = matrix[i][length-1-j], matrix[i][j]

   return matrix   

def check_output(matrix):
   print(f"----------------- Original -----------------")
   print(np.array(matrix))

   print(f"----------------- Rotated -----------------")
   print(np.array(rotate_2(matrix)))
   
   print('-'*20)

matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix_2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix_3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

check_output(matrix_1)
        