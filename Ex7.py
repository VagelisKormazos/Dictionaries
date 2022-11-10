# 7. Έστω αρχείο κειμένου ASCII το οποίο σε κάθε γραμμή του περιέχει ένα λεξικό της Python (dictionary). Το λεξικό κάθε
# γραμμής περιέχει τα ίδια κλειδιά με τις υπόλοιπες γραμμές. Τα κλειδιά αυτά περιέχουν τιμές οι οποίες μπορούν να είναι
# μόνο αριθμοί ή κείμενο. Γράψτε κώδικα το οποίο διαβάζει το αρχείο αυτό, εμφανίζει στο χρήστη τα διαθέσιμα κλειδιά και
# τον ρωτάει ποιο από τα διαθέσιμα κλειδιά τον ενδιαφέρει. Στην συνέχεια, για αυτό το κλειδί εμφανίζει την δημοφιλέστερη
# τιμή, την μεγαλύτερη και τη μικρότερη.
# Παράδειγμα:
# Έστω ότι το αρχείο σας περιέχει τα ακόλουθα λεξικά
# {"x":3,"y":4,"name":"bob"}
# {"x":13,"y":-4,"name":"malory"}
# {"x":-3,"y":104,"name":"trudy"}
# {"x":1,"y":14,"name":"alice"}
# Ο κώδικάς σας εμφανίζει στο χρήστη: x, y, name
# Ζητάει από το χρήστη το κλειδί. Αν αυτός επιλέξει y, ο κώδικάς σας θα πρέπει να επιστρέψει τις τιμές -4 και 104.

import ast

d=dict()
a=[]
#Open the text add split it to lines.
f=open('example.txt','r')
for x in f:
    #print(x)
    a.append(x)
#Make the lines Dictionaries,find keys and print it.
for y in a:
    b=ast.literal_eval(y)
    d.update(b)
    print(d)

print('There are the keys:')
for key in d:
    print(key)

i=0
#Choose a key
while(i!=2022):
    st = input('Choose a key:')
    for key in d:
        if key==st:
            i=2022
    if i!=2022:
        print('Try Again!')
#Take the valaues of the each line and add it in a List.
L=[]
for y in a:
    b=ast.literal_eval(y)
    d.update(b)
    for key,value in d.items():
        if (key==st):
            L.append(d[key])
print(L)

#Find and print the max,the min and the most popular value.
if type(L[0])!=type(st):
    print("The Maximum Value of this Key is:",max(L))
    print("The Minimum Value of this Key is:",min(L))
else:
    print("The biggest String is:", max(L, key=len))
    print("The smallest String:", min(L, key=len))
from collections import Counter
c = Counter(L)
c.most_common(1)
print("Now you can see the most frequent Value of this Key and how many times exist:",c.most_common(1))