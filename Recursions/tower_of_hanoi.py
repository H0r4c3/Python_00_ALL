'''
https://towardsdatascience.com/tower-of-hanoi-a-recursive-approach-12592d1a7b20

How does Recursion works ?
Let f(n) be a recursive function .

Three rules :

Show f(1) works => Base case.
Assume f(n-1) works .
Show f(1) works using f(n-1).
'''

moves = list()

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    global moves
    
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        moves.append((from_rod, to_rod))
        print(moves)
        return moves
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    moves.append((from_rod, to_rod))
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         

n = int(input("Enter the number of disks: "))
TowerOfHanoi(n, 'A', 'C', 'B')