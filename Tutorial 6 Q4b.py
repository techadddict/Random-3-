#Write a function ShiftEl(A,el), where A is a list of integer numbers and el
#is an integer number. The function should do the following.
#i) Append the number el to the end of A
#ii) Use the SwapLst function to iteratively swap el with the element to the (immediate) left
#of it until either el is the leftmost element of A or el is smaller than or equal
#to the element immediately to the left of it.



def main():
    A=[8,5,7,15,9]
    b=SwapLst(A,1,3)
    print(b)

    

def SwapLst(A,i,j):
    
    temp =A[i]
    A[i]=A[j]
    A[j]=temp
    return A


main()
