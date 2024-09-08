#********************************************* String Slicing *********************************************************************

b="hello,world"                                         #0 1 2 3 4 5 6 7 8 9 10 
print(b[2:5])           #2 is start index 5 is end index h e l l o , w o r l d
                                                        #0 1 2 3 4 5  (last index value(5) not included but start index included)
                                                        # result will be llo 
# from start to end

b = "Hello,World!"

print(b[7:])

                                          
#reverse string slicing

b = "Hello,World!"
print(b[-5:-2])             #index numbers are assigned in reverse direction



#********************************************* Modify String *********************************************************************

# 1. Upper : upper() converts to uppercase
c="world of stars"
print(c.upper())

# 2. Lower : lower() converts to lowercase
d="WORLD OF STARS"
print(d.lower())

# 3. Strip(whitespace removal) : strip() removes whitespace from beginning or ending
e="    EL. HALUFF!     "
print(e.strip())

# 4. Replace : replace() replace one string with another
f="Hellow , World"
print(f.replace("o","J"))  # replaces alphabet ' o ' with ' j ' 

# 5. Split : split() replace one string with another

a = "Hello j World!"
print(a.split("j")) # splits the string into further smaller strings here it finds j and replaces it with comma removing j while also spliting into two smaller strings 

#********************************************* Concatenate String *********************************************************************

i="Hello"
j="World"
k=i+j
print(k)

# to add space add " "
i="Hello"
j="World"
k=i+" "+j
print(k)

#********************************************* Format String *********************************************************************

age = 36
txt = f"My name is Barry, I am {age}"  # normally string and int variable cannot be added so we use fstring
print(txt)