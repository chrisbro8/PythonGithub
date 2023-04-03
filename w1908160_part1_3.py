# I declare that my work contains no examples of misconduct,such plagarism or collusion
#Any code taken from other sources is referenced within my code solution
#w1908160
#23/11/2022
#https://www.w3schools.com/python/python_dictionaries_loop.asp
#https://www.w3schools.com/python/python_file_write.asp

#Wendy purdy lectures
#Software Development seminar
#Edx Introduction to MIT by Eric GRIMSON

rewrite=''
space='  '
progress=retriever=trailer=excluded=0
storage=[]
part2storage=[]



def compare(a,b=''):
    for y in range(len(a)):
        if a[y] not in [0,20,40,60,80,100,120]:
            b='false'
        else:
            b='true'
    return b
def part2():
    print('Part 2:')
    return

wordstorage=[]
while rewrite!='q':
    
    credit_pass=input('Please enter your credits at pass: ')
    credit_defer=input('Please enter your credits at defer: ')
    credit_fail=input('Please enter your credits at fail: ')
   
    try:
        credit_pass=int(credit_pass)
        credit_fail=int(credit_fail)
        credit_defer=int(credit_defer)
        totalcredit=int(credit_pass+credit_fail+credit_defer)
        try:
            a=[credit_pass,credit_defer,credit_fail]
            if compare(a)!='true':
                print('Out of range')
                break
            elif totalcredit!=120:
                print('Total incorrect')
                break
        except:
            pass    
    except:
        print('Integer required')
        break
    storage=[credit_pass,credit_defer,credit_fail]
    part2storage.append(storage)
   
 
    if credit_pass>=100:
        if credit_pass==120:
            progress+=1
            wordstorage.append('Progress')
            print('Progress')
        elif credit_pass==100:
            trailer+=1
            wordstorage.append('Progress(module trailer)')
            print('Progress(module trailer)')
        
    elif credit_fail<80:
        retriever+=1
        wordstorage.append('Module retriever')
        print('Module retriever') 
    
    elif credit_fail>=80:               
        print('Exclude')
        wordstorage.append('Exclude')
        excluded+=1
        
        
        
    rewrite=input("Would you like to test another set of data ? \nEnter 'y' for yes or 'q' to quit and view results:")
    if rewrite=='y' or rewrite=='q':
        pass
    else:
        print('i dont recognised that input perpharps you inputed caplocks')
        break
 
       
 
   
total_input=progress+trailer+retriever+excluded
print('------------------------------------------------------------------------------------')
print('Histogram\nProgress',progress,':','*'*progress,'\nTrailer',trailer ,':','*'* trailer)
print('Retriever ',retriever,':','*'*retriever,'\nExcluded',excluded,':','*'*excluded)
print('\n'+str(total_input) +' outcome in total.\n'+space)
print('------------------------------------------------------------------------------------')
part2()
s=''
x=[]

f=open('file.txt','w')           #https://www.w3schools.com/python/python_file_write.asp
f.write("Part 3a:\n")
f.close()
for i in range(total_input):
    useword=','.join(map(str, part2storage[i]))  #
    print(wordstorage[i]+'-'+useword)
    s=(wordstorage[i]+'-'+useword) #this is s
    x.append(s)
    f = open("file.txt", "a")
    f.write(x[i]+'\n')
    
    
