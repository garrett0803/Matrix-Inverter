size=int(input('enter size of square matrix: '))
mat=[]
mattemp=[]

for x in range(size):
    for i in range(size):
        j=int(input("enter number in ROW {} in LOCATION {}".format(x+1,i+1)+' '))
        mattemp.append(j)

    mat.append(mattemp)
    mattemp=[]
# used to find the det of a square matrix 
## takes in each minor and multiples it by the sum of the smaller matrix
def matrixDet(mat):
    reduceDet=[]
    detnew=[]
    detmulti=[]
    x=0
    row=1
    while(x<len(mat)):
        dettemp=mat[0]
        detmulti=dettemp[x]
        print(detmulti)
        while(row<len(mat)):
            col=1
            dettemp=mat[row]
            while(col<len(mat)):
                detnew.append(dettemp[col])
                col=col+1
            row=row+1
        x=x+1
        reduceDet.append(detmulti*((detnew[0]*detnew[3])-(detnew[1]*detnew[2])))

        print(reduceDet)
          
    


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
matrixDet(mat)
while(y<len(mat)):
    
       
    print(mat[y], end="\n")
    #print(y)
    y=y+1







#TODO need to turn a certain matrix into a identity matrix and do the same operations to a identity matrix

#def rowEch(mat):
    #get row 1, col 1==1





