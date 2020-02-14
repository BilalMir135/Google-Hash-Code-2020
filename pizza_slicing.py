import os

def solution(max_slice,categories,_types,f):    
    temp_types_index = []
    _sum = 0
    max_sum = 0
    types_index= []
    for x in range(categories-1,-1,-1):
        _sum = _types[x]    
        temp_types_index.append(x)
        for y in range(categories-1,x+1-1,-1):
            if _sum+_types[y]<=max_slice:
                _sum += _types[y]
                temp_types_index.append(y)
        if max_sum<_sum:
            types_index = temp_types_index.copy()
            max_sum = _sum
        temp_types_index = []
    try:
        with open ('output/'+f,'w') as file:
            file.write(str(len(types_index))+'\n')
            for x in types_index:
                file.write(str(x)+' ')
    except Exception as e:
        print(e)



files = os.listdir('input')
files.sort()

for f in files:
    if f[-3:] == '.in':
        try:
            with open ('input/'+f,'r') as file:
                text=file.read()
        except Exception as e:
                print(e)
                    
        lines = text.split('\n')
        max_slice, categories = lines[0].split()
        _types=[]
        for x in lines[1].split():
            _types.append(int(x))
                
        solution(int(max_slice),int(categories),_types,f.replace('.in','.out'))


