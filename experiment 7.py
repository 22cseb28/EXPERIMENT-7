# items in library
list=['book','journels','epicbook','encyclopedia','book']
list_book=['fan','table','chairs','clock']
#append
list.append('subjectbook')                       
print("append:",list)
#extend
list.extend('dictinary')                              
print("extend:",list)
#insert
list.insert(3,'newspaper')                              
print("insert:",list)
#changing element
list[2]='friction book'                               
print("changing elemnent:",list)
#slicing
list[1:4]                                                   
list[1::]
list[-3]
list[-3:-5]
print("slicing:",list)
#poping
list_book.pop(1)
print("pop:",list_book)
#concatenation
book_list=[list+list_book]
print("cocatenation:",book_list)
#remove
list.remove('journels')                             
print("remove:",list)
#del
del list[1:4]                                             
print("del",list)

