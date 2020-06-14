class Sort:
    #选择排序
    def selectionSort(arr):
        n=len(arr)
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[j] < arr[i]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr
    
    #插入排序
    def insertionSort(arr):
        n=len(arr)
        preindex,current=0,0
        for i in range(1,n):
            preindex=i-1
            current=arr[i]
            while preindex>=0 and arr[preindex]>current:
                arr[preindex+1]=arr[preindex]
                preindex-=1
            arr[preindex+1]=current

        return arr
    
    #冒泡排序
    def bubbleSort(arr):
        n=len(arr)
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        
        return arr

        

arr=[9,7,5,3,1,10,6,4,2]
print("选择排序：",Sort.selectionSort(arr))
print("插入排序：",Sort.insertionSort(arr))
print("冒泡排序：",Sort.bubbleSort(arr))
