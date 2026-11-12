def addition(x,y):
    return x+y #for solving problems always RETURN
print(addition(10,20))


#conditional STATEMENTS
vowel_count=0
consonant_count=0
str1="project"
for ch in str1:
    if ch in "aeiouAEIOU":
        vowel_count+=1
    else:
        consonant_count+=1
print(vowel_count)
print(consonant_count)



def alphabet_count(str1):
    vowel_count=0
    consonant_count=0
    for ch in str1:
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                vowel_count+=1
            else:
                consonant_count+=1
    return(vowel_count,consonant_count)
res=alphabet_count("python project")
print(res)