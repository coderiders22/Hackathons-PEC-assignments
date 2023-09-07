#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:      CSE(Data Science)
# SID :        22106028
#
# Question 4: Write a program for insertion and deletion of elements in a list.
#              On selection of deletion option, a submenu should be displayed
#              to ask if the element is to be deleted by value or by position or
#              a slice of elements has to be deleted and accordingly the output
#              is generated.
#
#
# Created:     01-09-2023
#------------------------------------------------------------------------------

l1=[]
n1=int(input(""))
for i in range(0,n1):
    a=int(input(" "))
    l1.append(a)
opt=int(input("1.delete \n 2.Insert"))
if opt==2:
    a=int(input(" index value"))
    b=input("value ")
    l1.insert(a,b)
else:
    op=int(input(" 1.delete by value \n 2. delete by index \n 3.delete range"))
    if(op==1):
        k=input("enter you want to delete")
        l1.remove(k)
    elif op==2:
        k=int(input("enter index"))
        del l1[k]
    else:
        st=int(input("strating index"))
        ed=int(input("ending value"))
        for i in range(st,ed+1):
            del l1[i]


print(l1)