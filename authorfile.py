def group_by_owners(files):
    """This  accepts a  dictionary containing the file owner name for each file name and
    returns a dictionary containing a list of file names for each owne name, in any order."""
    try :
        maindict = {}
        for fle,author in files.items() :
            if author in maindict :
                maindict[author].append(fle)
            else :
                maindict[author] = []
                maindict[author].append(fle)
        if len(maindict) > 0 :
            for ky in maindict.keys() :
                maindict[ky] = ", ".join(maindict[ky])
        return maindict

    except Exception as ex :
        print(ex)

# Input section
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))