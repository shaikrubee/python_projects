def read_matrix(rows):
    matrix=[]
    for i in range(rows):
        row=input().split()
        matrix.append(row)
    return matrix

def check_if_sub_matrix_contains_zero(matrix,i,j,k,l):
    for m in range(0,k+1):
        for n in range(0,l+1):
            if(matrix[i+m][j+n]=="0"):
                return True
    return False

def get_max_sub_matrix_area(matrix,rows,columns,i,j):
    max_sub_matrix_area=0
    for k in range(0,rows-i):
        for l in range(0,columns-j):
            if(k!=l):
                continue
            is_sub_matrix_contains_zero=check_if_sub_matrix_contains_zero(matrix,i,j,k,l)
            if not  is_sub_matrix_contains_zero:
                max_sub_matrix_area=max(max_sub_matrix_area,(k+1)*(l+1))
    return max_sub_matrix_area

def get_max_area_of_square(matrix,rows,columns):
    max_area_of_square=0
    for i in range(rows):
        for j in range(columns):
            if (matrix[i][j]=="X"):
                max_sub_matrix_area=get_max_sub_matrix_area(matrix,rows,columns,i,j)
                max_area_of_square=max(max_area_of_square,max_sub_matrix_area)
    return max_area_of_square

def main():
    rows,columns=map(int,input().split(" "))
    matrix=read_matrix(rows)
    max_area_of_square=get_max_area_of_square(matrix,rows,columns)
    print(max_area_of_square)

main()