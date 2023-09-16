def print_header2():
    ascii_art = '''

___________.___         ___________               ___________            
\__    ___/|   | ____   \__    ___/____    ____   \__    ___/___   ____  
  |    |   |   |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ 
  |    |   |   \  \___    |    |   / __ \\  \___    |    |(  <_> )  ___/ 
  |____|   |___|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >
                    \/                 \/     \/                      \/

  '''
    print(ascii_art);     

def ConstBoard(board):
    
    print("Current State of the Board: \n\n");
    for i in range(0,9):
        if(i>0) and (i%3==0):
            print("\n");
        if(board[i]==0):
            print("_ ",end = " ");
        if(board[i]==-1):
            print("X",end = " ");
        if(board[i]==1):
            print("O",end = " ");
    print("\n\n");

def User1Turn(board):
    
    pos =  input("Enter Xth Position form [1,2...,9]: ");
    pos = int(pos);
    if(board[pos-1]!=0):
       print("Wrong Move");
       exit(0);
    board[pos-1] = -1;
    
def User2Turn(board):
     
    pos =  input("Enter Oth Position form [1,2...,9]: ");
    pos = int(pos);
    if(board[pos-1]!=0):
       print("Wrong Move");
       exit(0);
    board[pos-1] = 1;    

def analyzeboard(board):
    
    cb = [[0,1,2,],[3,4,5],[6,7,8],[0,3,6],[1,4,7],
        [2,5,8], [0,4,8],[2,4,6]]
    
    for i in range(0,8):
        
        if(board[cb[i][0]]!=0 and 
        board[cb[i][0]]== board[cb[i][1]] and
        board[cb[i][0]]== board[cb[i][2]]):
         return board[cb[i][0]];

    return 0;

def minmax(board, player):

    x = analyzeboard(board);    
    if(x!=0):
     return (x*player);
    
    pos = -1; #Declaration 
    value = -2 #Not possibility 
    for  i in range(0,9): #Every particular index checks it's an empty
        if(board[i]==0):
            board[i] = player; #put player 
            score  = -minmax(board, (player)*(-1)); #next player turns Ai then human then Ai so-on
            board[i]  = 0;
            if(score > value):
                value = score; #upgrade the value
                pos = i;
        if(pos == -1):
         return 0;
    return value;

def CompTurn(board):
    
    pos = -1; #Declaration 
    value = -2 #Not possibility 
    for  i in range(0,9): #Every particular index checks it's an empty
        if(board[i]==0):
            board[i] = 1; #put 0 on that current position in board as an AI
            score  = -minmax(board, -1); #minus sign is what! ?? 
            # bcz in minmax return statement minus is return so it's a positive 
            board[i]  = 0;
            if(score > value):
                value = score; #upgrade the value
                pos = i;
    board[pos]= 1;
    

def main():
    
    print("\n");
    print_header2();
    print("\n")
    choice = input("Enter 1 for Single Player, 2 for MultiPlayer: ");
    choice = int(choice);
    board = [0,0,0,0,0,0,0,0,0] #Declaring as 0
    if(choice == 1):
        
        print("Computer: 0 Vs You: X");
        print("\n");
        name = input("Enter the Player Name: ");
        player = input("Enter to play 1(st) pr 2(nd): ");
        print("\n");
        player = int(player);
        
        for i in range(0,9):
            if(analyzeboard(board)!=0):
                break;
            if((i+player)%2==0):
                CompTurn(board); #AI turn 
            else:
                ConstBoard(board);
                User1Turn(board);
    else:
        for i in range(0,9):
            if(analyzeboard(board)!=0):
                break;
            if((i%2==0)):
                ConstBoard(board);
                User1Turn(board);
            else:
                ConstBoard(board);
                User2Turn(board);
    
    x = analyzeboard(board);
    if(x==0):#Draw
        ConstBoard(board);
        print("Draw!");
    if(x==-1):#Myself
        ConstBoard(board);
        print("Player " + name + " (X) Wins!!!!");
    if(x==1): #AI
        ConstBoard(board);
        print("Player AI (0) Wins!!!!");

#Calling the Main Function
main();
  




