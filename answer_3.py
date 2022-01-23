import os
def find_duplicates():
    path= "G:\\data"   
    count=0
    mainlist = [[] for x in range(10)]

    contents =[]
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f: 
            content=f.read()
            if content in contents :
                index=contents.index(content)
                mainlist[index].append(filename.split(".")[0])
            else:
                contents.append(content)
                index = contents.index(content)
                mainlist[index].append(filename.split(".")[0])

    return mainlist
 
        
if __name__ == '__main__':
    result = find_duplicates()
    for row in result:
        print(" ".join(str(i) for i in row))