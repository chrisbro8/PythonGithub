if cout==0:
        addlist=[credit_defer,credit_fail,credit_pass]
        extension=[addlist]        
        if credit_pass>=120:
            if credit_pass==120:
                progress+=1
                p=progress
                print('progress')
            else:
                print('progress(module trailer)')
                trailer+=1
                t=trailer
        elif credit_fail<80 :
            print('Do not progress-module retriever')
            retriever+=1
            r=retriever
        else:
            print('Exclude')
            excluded+=1
            e=excluded