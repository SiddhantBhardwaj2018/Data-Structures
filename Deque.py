
import collections

#Initializing deque
de = collections.deque([1,2,3,3,4,2,4])

#using extend() to add numbers to the right end 
#adds 4,5,6 to the right end

de.extend([4,5,6])

#Printing the modified deque
print(de)

#Using index to print first occurrence of 4
print("The number 4 first occurs at position: ")
print(de.index(4,2,5))

#insert(i,a)
# using insert() to insert the value 3 at 5th position
de.insert(4,3)

#Rotate the deque
#rotates by 3 to left
de.rotate(-3)

#printing modified deque
print("The deque after inserting 3 at 5th position is: ")
print(de)


#using count()  to count occurrences of 3
print("The count of 3 in deque is: " + str(de.count(3)))

#using remove() to remove the first occurrence of 3
de.remove(3)

#printing modified deque
print("The deque after deleting the first occurrence of 3")
print(de)