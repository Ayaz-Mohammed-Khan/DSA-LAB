import stack
inp=input("Enter the postfix expression:").split(" ")
inp=list(inp)
n=len(inp)
nstack=stack.Stack(n)
newstack=stack.Stack(n)
for i in inp:
    nstack.push(i)
a=nstack.show()
print(a)
for i in a:
    try:
        if (type(int(i))==int) :
            newstack.push(int(i))
    except ValueError:
     if i in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
        newstack.push(i)   
     if i=="+":
         x=newstack.pop()
         y=newstack.pop()
         try:
            z=newstack.push(y+"+"+x)
         except TypeError:
            z=newstack.push(int(y+x)) 
         
     if i=="-":
         x=newstack.pop()
         y=newstack.pop()
         try:
            z=newstack.push(y+"-"+x)
         except TypeError:
            z=newstack.push(int(y-x))
     if i=="*":
         x=newstack.pop()
         y=newstack.pop()
         try:
            z=newstack.push(y+"*"+x)
         except TypeError:
            z=newstack.push(int(y*x))
     if i=="/":
         x=newstack.pop()
         y=newstack.pop()
         try:
            z=newstack.push(y+"/"+x)
         except TypeError:
            z=newstack.push(int(y/x))
     if i=="&":
         x=newstack.pop()
         y=newstack.pop()
         try:
            z=newstack.push(y+"&"+x)
         except TypeError:
            z=newstack.push(int(y)&int(x))
     if i=="^":
         x=newstack.pop()
         y=newstack.pop()
         try:
            z=newstack.push(y+"^"+x)
         except TypeError:
            z=newstack.push(int(y)^int(x))
     if i=="&&":
         x=newstack.pop()
         y=newstack.pop()
         try:
            z=newstack.push(y+"&&"+x)
         except TypeError:
            z=newstack.push((y and x))
     if i=="||":
         x=newstack.pop()
         y=newstack.pop()
         try:
            z=newstack.push(y+"||"+x)
         except TypeError:
             z=newstack.push((y or x))
final=newstack.show()[0]
print("Infix expression is:",final)
        


