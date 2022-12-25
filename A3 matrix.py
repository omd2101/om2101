def inputs():
    list=[]
    row=int(input("Enter the row number: "))
    col=int(input("Enter the column number : "))
    for i in range(row):
        b=[]
        for j in range(col):
            b.append(int(input("Enter the element : ")))
        list.append(b)
    return list

def addition(m1,m2):
    m3=[]
    for i in range(len(m1)):
        b=[]
        for j in range(len(m1[0])):
            b.append ( m1[i][j] + m2[i][j] )
        m3.append(b)
    print("Addition is : \n",m3)

def substraction(m1,m2):
    m3=[]
    for i in range(len(m1)):
        
        b=[]
        for j in range(len(m1[0])):
            b.append ( m1[i][j] - m2[i][j] )
        m3.append(b)
    print("Substraction is : \n",m3)

def multipication(m1,m2):
    m3=[[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j] += m1[i][k] * m2[k][j]
    print("Multiplication is : ",m3)

def transpose(m1):
    m3=[[0 for j in range(len(m1))] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            m3[j][i] = m1[i][j]
    print("Transpose is : ",m3)

mat1=inputs()
mat2=inputs()
print(mat1)
print(mat2)

addition(mat1,mat2)
substraction(mat1,mat2)
multipication(mat1,mat2)
transpose(mat1)
