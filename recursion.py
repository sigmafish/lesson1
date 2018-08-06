
# Recursion 1: print
def my_print(n):
    if(n!=1):
        my_print(n-1)
    print(n)

# Recursion 2: fractorial
def my_fractorial(n):
    if(n==0):
        return 1
    else:
        return n*my_fractorial(n-1)

# Recursion 3: Tower of Hanoi
def hanoi(n, disk_from, disk_mid, disk_to):
    if(n==0):
##        print("No Disk")
        return;
    hanoi(n-1, disk_from, disk_to, disk_mid)
    print("Disk %d from %s tower -> %s tower"%(n,disk_from,disk_to))
    hanoi(n-1, disk_mid, disk_from, disk_to)
    
##my_print(5)
##print(my_fractorial(5))
hanoi(3,'A','B','C')
