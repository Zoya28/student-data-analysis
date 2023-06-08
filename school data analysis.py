import pandas as pd
import matplotlib.pyplot as pl

# show data
def showdata():
    print()
    df = pd.read_csv(r'D:\ds project\student.csv')
    print(df)
    input('press  any key to continue .....')
    
# show data without index
def noindex():
    print()
    df = pd.read_csv(r'D:\ds project\student.csv', index_col=0)
    print(df)
    input('press  any key to continue .....')
    
# show data in ascending order
def ascdata():
    print()
    print('sort data')
    print(''' 
            1. name 
            2. total marks''')
    choice = int(input('enter your choice :'))
    if choice == 1 :
        print('data sorted according to name : ')
        print('--------------------------------------------')
        df = pd.read_csv(r'D:\ds project\student.csv')
        print(df.sort_values(by=['name']))
        
    else:
        print('data sorted according to name : ')
        print('--------------------------------------------')
        df = pd.read_csv(r'D:\ds project\student.csv')
        print(df.sort_values(by=['total']))
    input('press  any key to continue .....')
        
# find average min and maximum
def mam():
    print()
    df = pd.read_csv(r'D:\ds project\student.csv')
    print('========================================================')
    print('average, max and minimum marks subject wise :')
    print('maths maximum :' , df['math'].max())
    print('maths minimum :' , df['math'].min())
    print()
    print('physics maximum :' , df['physics'].max())
    print('physics minimum :' , df['physics'].min())
    print()
    print('chemistry maximum :' , df['chemistry'].max())
    print('chemistry minimum :' , df['chemistry'].min())
    print()
    print('english maximum :' , df['english'].max())
    print('english minimum :' , df['english'].min())
    print()
    print('IP maximum :' , df['IP'].max())
    print('IP minimum :' , df['IP'].min())
    print()
    print('total maximum :' , df['total'].max())
    print('total minimum :' , df['total'].min())
    print()
    print('--------------------------------------------------------')
    print()
    print('overall average subject wise :')
    print(df.mean(numeric_only=True))
    print()
    print('=======================================================')
    
    
    input('press  any key to continue .....')
    
# edit a data
def edit():
    print()
    df = pd.read_csv(r'D:\ds project\student.csv')
    print('''
            1 --> update a single data
            2 --> add new data /row ''')
    choice = int(input('enter your choice :'))
    if choice == 1:
        print(''' 
                1 --> update name 
                2 --> update marks''')
        update = int(input('enter your choice :'))
        if update  == 1:
            row = int(input('enter the row number :')) 
            new = input('enter name :')
            df.name[row]=new
            print('updated ......')
            df.to_csv(r'D:\ds project\student.csv',index=False)
            print(df)

        else:
            row = int(input('enter the row :'))
            coln = input('enter column name (subject) :')
            new = int(input('enter marks to be updated :'))
            if coln == 'math':
                df.math[row]=new
            elif coln == 'physics':
                df.physics[row]=new
            elif coln == 'chemistry':
                df.chemistry[row]=new
            elif coln == 'IP' or 'ip':
                df.IP[row]=new
            elif coln == 'english':
                df.english[row]=new
            else:
                print('wrong input')
                
            print('updated....')
            df.to_csv(r'D:\ds project\student.csv',index=False)
            print(df)
    
    else:
        qty = int(input('number of rows to be added :'))
        for i in range(qty):
            name= input('enter student name : ')
            math = int(input('enter maths marks :'))
            phy = int(input('enter physics marks :'))
            chem = int(input('enter chemistry marks :'))
            eng = int(input('enter english marks :'))
            ip = int(input('enter ip marks :'))
            tot = math+phy+chem+eng+ip
            df.loc[len(df.index)]=[name,math,phy,chem,eng,ip,tot]
            print('updated ......')
            df.to_csv(r'D:\ds project\student.csv',index=False)
        print(df)
    input('press any key to continue.......')
# delete a data
def deldata():
    print()
    df = pd.read_csv(r'D:\ds project\student.csv')
    delrow = int(input('enter the index of row to be deleted :'))
    df1=df.drop(df.index[delrow])
    df = df1
    print('updated....')
    df.to_csv(r'D:\ds project\student.csv', index=False)
    print(df)
    input('press any key to continue.......')
    

# line plot
def lineplot():
    print()
    df = pd.read_csv(r'D:\ds project\student.csv')
    print(''' 
            1 --> plot name vs math
            2 --> plot name vs physics
            3 --> plot name vs  chemistry
            4 --> plot name vs english
            5 --> plot name vs IP
            6 --> plot name vs total
            7 --> plot all data at once
            ''')

    ch = int(input('enter your plotting choice :'))
    if ch == 1:
            df.plot(x='name', y='math', kind='line', title='math marks')
            pl.show()
    elif ch == 2:
            df.plot(x='name', y='physics', kind='line', title='physics marks')
            pl.show()
    elif ch == 3:
            df.plot(x='name', y='chemistry', kind='line', title='chemistry marks')
            pl.show()
    elif ch == 4:
            df.plot(x='name', y='english', kind='line', title='english marks')
            pl.show()
    elif ch == 5:
            df.plot(x='name', y='IP', kind='line', title='IP marks')
            pl.show()
    elif ch == 6:
            df.plot(x='name', y='total', kind='line', title='total marks')
            pl.show()
    elif ch == 7:
            df.plot()
            pl.show()
    else:
            print('wrong choice')
    
    
    input('press any key to continue.......')
# bar plot
def barplot():
    
    print()
    df = pd.read_csv(r'D:\ds project\student.csv')
    print(''' 
        1 --> plot name vs math
        2 --> plot name vs physics
        3 --> plot name vs  chemistry
        4 --> plot name vs english
        5 --> plot name vs IP
        6 --> plot name vs total
        
        ''')
        
    ch = int(input('enter your plotting choice :'))
    if ch == 1:
            df.plot(x='name', y='math', kind='bar', title='math marks')
            pl.show()
    elif ch == 2:
            df.plot(x='name', y='physics', kind='bar', title='physics marks')
            pl.show()
    elif ch == 3:
            df.plot(x='name', y='chemistry', kind='bar', title='chemistry marks')
            pl.show()
    elif ch == 4:
            df.plot(x='name', y='english', kind='bar', title='english marks')
            pl.show()
    elif ch == 5:
            df.plot(x='name', y='IP', kind='bar', title='IP marks')
            pl.show()
    elif ch == 6:
            df.plot(x='name', y='total', kind='bar', title='total marks')
            pl.show()
    else:
            print('wrong chpice')
    
    
    input('press any key to continue.......')


# main function 
def main():
    
# main program
    print('          welcome to my data analysis software')
    print()
    print("           ================================")
    print('                      main menu            ')
    print("           ================================")
    
    ch=0
    while ch !=10:
        
        print('''

            -----------------------------------
            1. show all data
            2. show data without index
            3. show data in ascending order
            4. find average, maximum and minimum
            5. edit a data 
            6. delete a record
            7. line graph
            8. bar graph
            9. exit 
            -----------------------------------''')
        ch = int(input('enter your choice :'))
        if ch == 1:
            showdata()
    
        elif ch == 2 :
            noindex()
    
        elif ch == 3 :
            ascdata()

        elif ch == 4 :
            mam()

        elif ch == 5 :
            edit()

        elif ch == 6:
            deldata()

        elif ch == 7:
            lineplot()

        elif ch == 8 :
            barplot()

        else:
            print('THANK YOU !!!   for using app,  bye bye ')
            break
main()



