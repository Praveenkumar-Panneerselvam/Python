# To count the vowels, consonants,numbers,space and special characters 

def alphabets(a):
    vowels="a,e,i,o,u,A,E,I,O,U"
    number="1,2,3,4,5,6,7,8,9,0"
    vowel_count=0
    consonant_count=0
    specialchar_count=0
    space_count=0
    num_count=0
    for i in range(0,len(a)):
        if a[i].isalpha():
            if(a[i] in vowels):
                vowel_count+=1
            else:
                consonant_count+=1
        elif a[i].isdigit():
            num_count+=1
        elif a[i].isspace():
            space_count+=1
        else:
            specialchar_count+=1
    print(vowel_count)
    print(consonant_count)
    print(num_count)
    print(specialchar_count)
    print(space_count)
alphabets(input("Enter:"))
            
    
