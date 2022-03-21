size=int(input('enter size of square matrix: '))
mat=[]
mattemp=[]
t1=[]
t2=[]
t3=[]

iMat=[t1,t2,t3]


for x in range(size):
    for i in range(size):
        j=int(input("enter number in ROW {} in LOCATION {}".format(x+1,i+1)+' '))
        mattemp.append(j)

    mat.append(mattemp)
    mattemp=[]
# used to find the det of a square matrix 
## takes in each minor and multiples it by the sum of the smaller matrix

def CreateIdentityArr(size):
    x=0
    

    
    #creating a matrix with size 3 with the following values
    # 1 0 0
    # 0 1 0
    # 0 0 1   
    while(x<size):
        y=0
        
        while(y<size):
            if(x==y):
                iMat[x].append(1)

            else:
                iMat[x].append(0)  

            y=y+1      

        x=x+1
        


def matrixDet(mat):
    reduceDet=[]
    detnew=[]
    detmulti=[]
    x=0
    row=1
    #trav arr to reduce and find DET
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

        #print(reduceDet)
          
    


def matrixInverse(mat):
    #for each row reduce col x to 1 and all other rows to 0
    ## create a array with identity mat
    i=0
    if(len(mat)==4):
    
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
    elif(len(mat)==3):
        while(i<len(mat)):
            mat[0]

    #TODO need to turn a certain matrix into a identity matrix and do the same operations to a identity matrix
    a=0
    #while(a<len(mat)):

matrixInverse(mat)

matrixDet(mat)
CreateIdentityArr(size)
y=0

while(y<len(iMat)):
       
    print(iMat[y], end="\n")
    #print(y)
    y=y+1


#TODO need to turn a certain matrix into a identity matrix and do the same operations to a identity matrix

#def rowEch(mat):
    #get row 1, col 1==1





