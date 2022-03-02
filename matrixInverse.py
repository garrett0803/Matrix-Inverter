size=int(input('enter size of square matrix: '))
mat=[]
mattemp=[]

for x in range(size):
    for i in range(size):
        j=int(input("enter number in ROW {} in LOCATION {}".format(x+1,i+1)+' '))
        mattemp.append(j)

    mat.append(mattemp)
    mattemp=[]




def matrixInverse(mat):
    if(len(mat)==4):
        i=0
        while(i<4):
            if(i==1 or i==2):
            #print(mat[i])
                mat[i]=-1*mat[i]
            #print(mat[i])
            if(i==3):
                temp=mat[0]
                mat[0]=mat[3]
                mat[3]=temp

            i=i+1  


    #TODO need to turn a certain matrix into a identity matrix and do the same operations to a identity matrix
    a=0
    #while(a<len(mat)):


  
            




matrixInverse(mat)
y=0

while(y<len(mat)):
    
       
    print(mat[1], end=",")
    #print(y)
    y=y+1







#TODO need to turn a certain matrix into a identity matrix and do the same operations to a identity matrix

#def rowEch(mat):
    #get row 1, col 1==1





