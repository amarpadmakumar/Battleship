'''Input player names'''
player1=str(input("Enter name:"))
player2=str(input("Enter name:"))

'''Print Player 1's board'''
board1=[]
for i in range(10):
   z=['O']*10
   board1.append(z)

def print_board1(board):
   print(player1+':') 
   for i in board:
       print(" ".join(i))

print_board1(board1)

print()

'''Print Player 2's board'''
board2=[]
for i in range(10):
   z=['O']*10
   board2.append(z)

def print_board2(board):
   print(player2+':') 
   for i in board:
       print(" ".join(i))

print_board2(board2)

'''Player 1 placing ships'''
def hide_carrier(): 
   print ('Carrier has 5 holes.')
   accept_row_head=False
   accept_column_head=False
   accept_row_tail=False
   accept_column_tail=False 
   accept_orientation=False


   while accept_orientation==False:
       orientation=str(input("Do you want to hide your Carrier horizontally or vertically? Enter h/v."))
       if orientation=="h" or orientation=="v":
           accept_orientation=True
       else:
           print("You must enter 'h' or 'v' only") 


   while accept_row_head==False:
       row_head=int(input("Enter row of Carrier's head (0-9) :"))
       if row_head in range(10):
           accept_row_head=True
       else:
           print("Row must be in range 0-9") 


   while accept_column_head==False:
       column_head=int(input("Enter column of Carrier's head (0-9) :"))
       if column_head in range(10):
           accept_column_head=True
       else:
           print("Column must be in range 0-9")

   while accept_row_tail==False:
       row_tail=int(input("Enter row of Carrier's tail (0-9) :"))
       if orientation=='v': 
           if row_tail in range(10) and abs(row_tail-row_head)==4:
               accept_row_tail=True
           else:
               poss_row1=row_head-4
               poss_row2=row_head+4
               if row_head-4 in range(10) and row_head+4 in range(10):
                   print("As your Carrier is being hidden vertically, the tail can only be in row %s or row %s." % (poss_row1,poss_row2))
               elif row_head-4 in range(10) and row_head+4 not in range(10):
                   print("As your Carrier is being hidden vertically, the tail can only be in row %s." % poss_row1)
               elif row_head-4 not in range(10) and row_head+4 in range(10):
                   print("As your Carrier is being hidden vertically, the tail can only be in row %s." % poss_row2) 

       elif orientation=='h':
           if row_tail in range(10) and row_tail==row_head:
               accept_row_tail=True
           else:
               print("As your Carrier is being hidden horizontally, the tail can only be in row %s." % row_head) 

   while accept_column_tail==False:
       column_tail=int(input("Enter column of Carrier's tail (0-9) :"))
       if orientation=='h': 
           if column_tail in range(10) and abs(column_tail-column_head)==4:
               accept_column_tail=True
           else:
               poss_col1=column_head-4
               poss_col2=column_head+4
               if column_head-4 in range(10) and column_head+4 in range(10):
                   print("As your Carrier is being hidden horizontally, the tail can only be in column %s or column %s." % (poss_col1,poss_col2))
               elif column_head-4 in range(10) and column_head+4 not in range(10):
                   print("As your Carrier is being hidden horizontally, the tail can only be in column %s." % poss_col1)
               elif column_head-4 not in range(10) and column_head+4 in range(10):
                   print("As your Carrier is being hidden horizontally, the tail can only be in column %s." % poss_col2) 

       elif orientation=='v':
           if column_tail in range(10) and column_tail==column_head:
               accept_column_tail=True
           else:
               print("As your Carrier is being hidden vertically, the tail can only be in column %s." %column_head)

   if orientation=='v':
       if row_head>row_tail: 
           for i in range(row_tail,row_head+1):
               board1[i][column_head]='C'
       elif row_head<row_tail: 
           for i in range(row_head,row_tail+1):
               board1[i][column_head]='C' 



   if orientation=='h':
       if column_head>column_tail: 
           for i in range(column_tail,column_head+1):
               board1[row_head][i]='C'
       elif column_head<column_tail:
           for i in range(column_head,column_tail+1):
               board1[row_head][i]='C'


   print_board1(board1)

hide_carrier()     

