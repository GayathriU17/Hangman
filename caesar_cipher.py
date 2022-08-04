alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift, alphabet):
  letters=[]
  letters= [char for char in text]
  new=[]
  new=['']*len(letters)
  for i in range(len(letters)):
    for j in range(len(alphabet)):
      if(letters[i]==alphabet[j]):
        k=j+shift
        if(k<26):
          new[i]=alphabet[k]
        elif(k>25):
          k=k-25
          new[i]=alphabet[k]
  print(''.join(map(str,new)))


def decrypt(text, shift, alphabet):
  letters=[]
  letters= [char for char in text]
  decrypt_new=['']*len(letters)
  for i in range(len(letters)):
    for j in range(len(alphabet)):
      if(letters[i]==alphabet[j]):
        k=j-shift
        #print (k, i, j)
        if(k>-1):
          decrypt_new[i]=alphabet[k]
        elif(k<0):
          k=26+k
          decrypt_new[i]=alphabet[k]
  print(''.join(map(str,decrypt_new)))


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if(direction=='encode'):
  encrypt(text, shift, alphabet)
elif(direction=='decode'):
  decrypt(text, shift, alphabet)
else:
  print('Invalid Entry')