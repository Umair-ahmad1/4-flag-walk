#writing a new method of encryption
#import mergeAlternately
#mport caesar_cipher_encoder
#import caesar_cipher_decoder
x='test string'
def new_encrypt(test_string,rot,key):
    #test string acts as the password, key is like what is needed to unlock it and then when outputting it should sort of undo itself
    y=test_string[::-1]
    print(y)
    #reversed_test_string
    if key!= '':
        word2=key
        word1=test_string
        c = len(word2)-len(word1)
        if c<=0:
            bigger_word=word1
            smaller_word=word2
        else:
            bigger_word=word2
            smaller_word=word1
        joined=[]
        for i in range(2*len(smaller_word)):
            if i%2==0:
                joined.append(word1[i//2])
            else:
                joined.append(word2[i//2])
        if c!=0:
            joined.append(bigger_word[-abs(c):])
        y=''.join(joined)
    next_step=[x for x in y]
    print(next_step)
    new=[]
    for i in range(len(next_step)):
        A=i+rot
        while A >= len(next_step):
            A-=len(next_step)
        new.append(next_step[A])
    print(new)
    alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_string=''.join(new)
    crypted_string=''
    for i in new_string.lower():
            #print(new_string)
            #print(i)
        if i in alphabet:
            base=alphabet.index(i)
            rotated= base + rot
            while rotated >= len(alphabet):
                rotated -= 26
            new_letter=alphabet[rotated]
        else:
            new_letter=i
        crypted_string+=new_letter
    #print(new_string)
    return crypted_string
x=new_encrypt('pa$$w0rd',5,'smellybumhole123')
print(x)
print(len(x))
print(len('pa$$w0rd'))
print(len('smellybumhole123'))