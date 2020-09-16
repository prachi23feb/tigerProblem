row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))
mat=[]
for i in range(row):
    a =[]
    for j in range(column):
         a.append(input())
    mat.append(a)
count=-1
for i in range(row-1):
    for j in range(column-1):
        if mat[i][j] == 's':
            if(mat[i][j]==mat[i-1][j-1] or mat[i][j]==mat[i][j-1] or mat[i][j]==mat[i+1][j-1] or mat[i][j]==mat[i-1][j]  or mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i-1][j+1] or mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j+1]):
                count+=1
            else:
                mat[i][j]='x'
                continue
        else:
            continue

print(count)
