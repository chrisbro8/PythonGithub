rewrite=''
progress=retriever=trailer=excluded=0
storage=[]
part4storage=dict()
testtry=''
studentidstorage=[]
wordstorage=''


def compare(a,b=''):
    for y in range(len(a)):
        if a[y] not in [0,20,40,60,80,100,120]:
            b='false'
        else:
            b='true'
    return b


while rewrite!='q':
    studentid=input('Please enter your student id:')
    credit_pass=input('Please enter your credits at pass: ')
    credit_defer=input('Please enter your credits at defer: ')
    credit_fail=input('Please enter your credits at fail: ')
    testtry=studentid[1::]
    
   
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
    try:
        testtry=int(testtry)
    except:
        print('The inputs are not integers')
        break
    storage=[credit_pass,credit_defer,credit_fail]
    if studentid[0]!='w':
        print('The first letter has to be w')
        break
    elif len(studentid)!=8:
        print('The length of the id has to be 8. ')
        break
    if credit_pass>=100:
        if credit_pass==120:
            wordstorage=': Progress -' +str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)
          
        elif credit_pass==100:
            wordstorage=': Progress(module trailer) -'+str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)
            
        
    elif credit_fail<80:
        wordstorage=': Module retriever - '+str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)
        
    
    elif credit_fail>=80:               
        wordstorage=': Exclude - '+str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)
        
        
    part4storage.update({studentid:wordstorage})  
    rewrite=input("Would you like to test another set of data ? \nEnter 'y' for yes or 'q' to quit and view results:")
    if rewrite=='y' or rewrite=='q':
        pass
    else:
        print('i dont recognised that input perhaps you inputed caplocks')
        break
 
total_input=progress+trailer+retriever+excluded
for i in part4storage:
    print(i,part4storage[i])