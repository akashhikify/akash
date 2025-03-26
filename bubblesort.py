def bubblesort(a):
    n=len(a)-1
    while n>=1:
        i=0
        while i<n:
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
            i=i+1
        n=n-1    
a=[1,2,4,6,78,89]
bubblesort(a)
print(a)
             