import random
def num(x,y):
    return (y-1)*size[0]+(x-1)
class mine:
    def size(self):
        y,x=int(input('행: ')),int(input('열: '))
        return (x,y,x*y)
    def level(self):
        lv=9
        while not 0<=lv<=2:
            try:
                lv=float(input('난이도: '))
            except:
                pass
            if not 0<=lv<=2:
                print('\n0~2사이의 수를 입력하세요\n')
        return (lv+1)/5
    def maker(self,size,level):
        sheet=[]
        lv=round(level*size[2])
        list=[]
        for i in range(lv):
            list.append('*')
        for i in range(size[2]-lv):
            list.append('.')
        for i in range(size[2]):
            sheet.append(random.choice(list))
            list.remove(sheet[-1])
        return sheet
    def map(self,size,sheet):
        list=[]
        for j in range(1,size[1]+1):
            for i in range(1,size[0]+1):
                save=[]
                if sheet[num(i,j)]=='*':
                    list.append(sheet[num(i,j)])
                else:
                    if j>1:
                        save.append(sheet[num(i,j-1)])
                        if i>1:
                            save.append(sheet[num(i-1,j-1)])
                        if i<size[0]:
                            save.append(sheet[num(i+1,j-1)])
                    if i>1:
                        save.append(sheet[num(i-1,j)])
                    if i<size[0]:
                        save.append(sheet[num(i+1,j)])
                    if j<size[1]:
                        save.append(sheet[num(i,j+1)])
                        if i>1:
                            save.append(sheet[num(i-1,j+1)])
                        if i<size[0]:
                            save.append(sheet[num(i+1,j+1)])
                    list.append(save.count('*'))
        return list
    def sheet(self,size):
        list=[]
        for i in range(size[2]):
            list.append('▯')
        return list
    def printer(self,size,list):
        sheet='\n'
        counter=0
        for i in list:
            sheet+=str(i)
            counter+=1
            if counter%size[0]==0:
                sheet+='\n'
        return sheet
    def choice(self,size):
        choice=9
        grid_x,grid_y=0,0
        while not choice==1 and not choice==2:
            try:
                choice=int(input('어떤 행동을 하시겠습니까?: '))
            except:
                pass
            if not choice==1 and not choice==2:
                print('\n조사,,,1 깃발,,,2 \n')
        else:
            while not 0<grid_y<=size[1]:
                try:
                    grid_y=int(input('행: '))
                except:
                    pass
                if not 0<grid_y<=size[1]:
                    print(f'\n1~{size[1]}사이의 수를 입력하세요\n')
            while not 0<grid_x<=size[0]:
                try:
                    grid_x=int(input('열: '))
                except:
                    pass
                if not 0<grid_x<=size[0]:
                    print(f'\n1~{size[0]}사이의 수를 입력하세요\n')
        return (choice,grid_x,grid_y)
    def judge(self,size,sheet,choice):
        if choice[0]==1 and not sheet[num(choice[1],choice[2])]=='▮':
            if answer[num(choice[1],choice[2])]=='*':
                del sheet[num(choice[1],choice[2])]
                sheet.insert(num(choice[1],choice[2]),'*')
                return 9
            elif answer[num(choice[1],choice[2])]>0:
                del sheet[num(choice[1],choice[2])]
                sheet.insert(num(choice[1],choice[2]),answer[num(choice[1],choice[2])])
                return 1
            elif sheet[num(choice[1],choice[2])]=='▯':
                del sheet[num(choice[1],choice[2])]
                sheet.insert(num(choice[1],choice[2]),0)
                if choice[2]>1:
                    self.judge(size,sheet,(1,choice[1],choice[2]-1))
                    if choice[1]>1:
                        self.judge(size,sheet,(1,choice[1]-1,choice[2]-1))
                    if choice[1]<size[0]:
                        self.judge(size,sheet,(1,choice[1]+1,choice[2]-1))
                if choice[1]>1:
                    self.judge(size,sheet,(1,choice[1]-1,choice[2]))
                if choice[1]<size[0]:
                    self.judge(size,sheet,(1,choice[1]+1,choice[2]))
                if choice[2]<size[1]:
                    self.judge(size,sheet,(1,choice[1],choice[2]+1))
                    if choice[1]>1:
                        self.judge(size,sheet,(1,choice[1]-1,choice[2]+1))
                    if choice[1]<size[0]:
                        self.judge(size,sheet,(1,choice[1]+1,choice[2]+1))
            return 1
        elif choice[0]==2:
            if sheet[num(choice[1],choice[2])]=='▯':  
                del sheet[num(choice[1],choice[2])]
                sheet.insert(num(choice[1],choice[2]),'▮')
            elif sheet[num(choice[1],choice[2])]=='▮':
                del sheet[num(choice[1],choice[2])]
                sheet.insert(num(choice[1],choice[2]),'▯')
            else:
                print('\n조사된 칸에는 깃발을 꽂을 수 없습니다.')
            return 1
        else:
            print('\n깃발을 꽂은 칸은 조사를 할 수 없습니다.')
    def judge2(self,size,sheet,choice):
        counter,total=0,0
        if choice[2]>1:
            if sheet[num(choice[1],choice[2]-1)]=='▮':
                  counter+=1
            if choice[1]>1:
                if sheet[num(choice[1]-1,choice[2]-1)]=='▮':
                    counter+=1
            if choice[1]<size[0]:
                if sheet[num(choice[1]+1,choice[2]-1)]=='▮':
                    counter+=1
        if choice[1]>1:
            if sheet[num(choice[1]-1,choice[2])]=='▮':
                counter+=1
        if choice[1]<size[0]:
            if sheet[num(choice[1]+1,choice[2])]=='▮':
                counter+=1
        if choice[2]<size[1]:
            if sheet[num(choice[1],choice[2]+1)]=='▮':
                counter+=1
            if choice[1]>1:
                if sheet[num(choice[1]-1,choice[2]+1)]=='▮':
                    counter+=1
            if choice[1]<size[0]:
                if sheet[num(choice[1]+1,choice[2]+1)]=='▮':
                    counter+=1
        if counter==sheet[num(choice[1],choice[2])]:
            if choice[2]>1:
                if sheet[num(choice[1],choice[2]-1)]=='▯':
                    total+=self.judge(size,sheet,(1,choice[1],choice[2]-1))
                else:
                    total+=1
                if choice[1]>1:
                    if sheet[num(choice[1]-1,choice[2]-1)]=='▯':
                        total+=self.judge(size,sheet,(1,choice[1]-1,choice[2]-1))
                    else:
                        total+=1
                if choice[1]<size[0]:
                    if sheet[num(choice[1]+1,choice[2]-1)]=='▯':
                        total+=self.judge(size,sheet,(1,choice[1]+1,choice[2]-1))
                    else:
                        total+=1
            if choice[1]>1:
                if sheet[num(choice[1]-1,choice[2])]=='▯':
                    total+=self.judge(size,sheet,(1,choice[1]-1,choice[2]))
                else:
                    total+=1
            if choice[1]<size[0]:
                if sheet[num(choice[1]+1,choice[2])]=='▯':
                    total+=self.judge(size,sheet,(1,choice[1]+1,choice[2]))
                else:
                    total+=1
            if choice[2]<size[1]:
                if sheet[num(choice[1],choice[2]+1)]=='▯':
                    total+=self.judge(size,sheet,(1,choice[1],choice[2]+1))
                else:
                    total+=1
                if choice[1]>1:
                    if sheet[num(choice[1]-1,choice[2]+1)]=='▯':
                        total+=self.judge(size,sheet,(1,choice[1]-1,choice[2]+1))
                    else:
                        total+=1
                if choice[1]<size[0]:
                    if sheet[num(choice[1]+1,choice[2]+1)]=='▯':
                        total+=self.judge(size,sheet,(1,choice[1]+1,choice[2]+1))
                    else:
                        total+=1
        else:
            print('\n칸의 숫자와 깃발의 개수가 일치하지 않아 주위를 조사할 수 없습니다.')
        if total>9:
            return 9
        else:
            return 1
               
while True:
    print('\n지뢰찾기 시작\n')
    a=mine()
    size=a.size()
    level=a.level()
    answer=a.map(size,a.maker(size,level))
    print('\n지뢰는 %s개' %answer.count('*'))
    sheet=a.sheet(size)
    print(a.printer(size,sheet))
    chosen=a.choice(size)
    while not answer[num(chosen[1],chosen[2])]==0:
        answer=a.map(size,a.maker(size,level))
    game=a.judge(size,sheet,chosen)
    if sheet.count('▯')+sheet.count('▮')==answer.count('*'):
        game=0
        print(a.printer(size,answer))
        print('축하합니다! 지뢰를 성공적으로 모두 찾으셨습니다\n')
    elif game==9:
        print(a.printer(size,sheet))
        print('gameover\n')
    elif game==1 or game==None:
        while not game==0 and not game==9:
            if sheet.count('▯')+sheet.count('▮')==answer.count('*'):
                game=0
                print(a.printer(size,answer))
                print('축하합니다! 지뢰를 성공적으로 모두 찾으셨습니다\n')
            else:
                print(a.printer(size,sheet))
                chosen=a.choice(size)
                if type(sheet[num(chosen[1],chosen[2])])==int:
                    game=a.judge2(size,sheet,chosen)
                else:
                    game=a.judge(size,sheet,chosen)
        if game==9:
            print(a.printer(size,sheet))
            print('gameover\n')
    replay=9
    while not replay==0 and not replay==1:
        try:
            replay=int(input('다시 플레이?: '))
        except:
            pass
        if not replay==0 and not replay==1:
            print('\n0...종료 1...다시 플레이\n')
    if replay==0:
        exit()
    else:
        continue
