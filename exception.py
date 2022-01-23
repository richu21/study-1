try : 
     x= 1
     if x==1 :
         raise NameError("nothing")
except NameError as n :
    print(n)
    print("name issue")
except Exception as ex:
    print(ex)
    print("general errors")
print("hiii")

# NameError