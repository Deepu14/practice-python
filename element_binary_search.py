def element_search(list1,search_element):
    #list1 = input("Please enter an ordered list of numbers: ")
    #search_element = input("Please enter a search element: ")
    list1 = sorted(list1)
    print(list1)
    mid = round(len(list1)/2)
    if search_element in list1:
        print("element found")
    else:
        print("element not found")
        
element_search([10,20,40,3,5,6,7],5)
element_search([10,20,40,3,5,6,7],15)

def binarysearch(list1,search_element):
    list1 = sorted(list1)
    first = 0
    last = len(list1)-1
    found = False
    while(found == False and first <= last):
        mid = round((first+last)/2)
        if search_element == list1[mid]:
            found = True
        elif search_element < list1[mid]:
            last = mid-1
        else:
            first = mid+1
    return found
    
print(binarysearch([10,20,40,3,5,6,7],5))
print(binarysearch([10,20,40,3,5,6,7],15))
