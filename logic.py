'''
program parts

-------x----
create mat 

--------x----

move left-wrte code
move right-reverse mat then left again
move top, transpose and left and transpose
move down transpose right transpose

moving part -------------------done

checking 

see if nempty blocks-> game not over
if no empty blocks------> see if any adjacent elements same, if same, game not over
else-----> game over

----------------
---------------

check if game not over.....
select random row and column, see if element empty, if empty add 2 to element
else, pick again

------------
game done
------------

'''
import random 

def start_game():
    mat=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    '''
    
    print("------ rules ----")
    print("w ---->top")
    print("a---->left")
    print("d--->right")
    print("s---->downn")
    '''
    
    
    mat=generate_new_mat(mat)
    return mat

def generate_new_mat(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    
	#check if element is empty
	
    while(mat[r][c]!=0):
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=random.choice([2, 4])
    return mat
    



def remove_blank(mat):
    for i in range(4):
        for j in range(2,-1,-1):
            if(mat[i][j]==0):
                 mat[i][j]=mat[i][j+1]
                 mat[i][j+1]=0
    return mat
         
#2244
		
def compress(mat):
     for i in range(4):
          for j in range(3):
               if(mat[i][j]==mat[i][j+1]):
                    mat[i][j]=mat[i][j]*2
                    mat[i][j+1]=0
                    mat=remove_blank(mat)
        
     return mat
                    
def reverse_list(lst):
    for i in range(2):
        lst[i], lst[-1-i] = lst[-1-i], lst[i]
    return lst

# Reversing the elements of each row
def reverse(mat):
     for i in range(4):
          mat[i] = reverse_list(mat[i])
     return mat
     
def transpose(mat):
     mat = list(map(lambda x: list(x), zip(*mat)))
     return mat


def move_left(mat):
     mat=remove_blank(mat)
     mat=compress(mat)
     return mat
     
def move_right(mat):

     mat=reverse(mat)
     mat=move_left(mat)
     mat=reverse(mat)
     return mat

def move_up(mat):
     mat=transpose(mat)
     mat=move_left(mat)
     mat=transpose(mat)
     return mat

def move_down(mat):
     mat=transpose(mat)
     mat=move_right(mat)
     mat=transpose(mat)
     return mat

def direct(direction,mat):
     if(direction=='w' or direction=='W'):
          mat=move_up(mat)
     elif(direction=='a' or direction=='A'):
          mat=move_left(mat)
     elif(direction=='s' or direction=='S'):
          mat=move_down(mat)
     elif(direction=='d' or direction=='D'):
          mat=move_right(mat)
     mat=generate_new_mat(mat)
     return mat


def checking(mat):
     for i in range(3):
            for j in range(3):
               if(mat[i][j]==0 or mat[i+1][j+1]==0):
                    return 1
               elif(mat[i][j]==2048 or mat[i+1][j+1]==2048):
                    return 2
               elif(mat[i][j]==mat[i][j+1]):
                    return 1
               elif(mat[i][j]==mat[i+1][j]):
                    return 1
            if(mat[i][3]==mat[i+1][3]):
                    return 1
            elif(mat[3][i]==mat[3][i+1]):
                 return 1
     for i in range(4):
          if(mat[i][3]==0):
               return 1
          elif(mat[3][i]==0):
               return 1
        
     return 0

def print_mat(mat):
     for rows in mat:
          print(rows)

def get_current_score(mat):
    # calculate the current score
    score = 0
    for i in range(4):
        for j in range(4):
            score += mat[i][j]
    return score
#checking code

'''
mat=start_game()
choice=1
print_mat(mat)

while(1):
     direction=input("enter direction: ")
     mat=direct(direction,mat)
     print_mat(mat)
     choice=checking(mat)
     if(choice==0):
          print("\n\n\n\n\n***************************")
          print("END OF GAME")
          print("**************************")
          break
     elif(choice==2):
          print("you have won")
          break
'''

