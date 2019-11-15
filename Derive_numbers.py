#!/usr/bin/env python
# coding: utf-8

# In[2]:


def main():
    num_test = int(input())
    pr_list = []
    if( 1<=num_test <=10):
        for num in range(num_test):
            p_r = input()
            pr_list.append(p_r)
        #print(pr_list)
        for p_r in pr_list:
            p,r = int(p_r.split(' ')[1]),int(p_r.split(' ')[0])
            if(1<=p<=r):
                if(p==r):
                    print(1)
                else:
                    a_len = p
                    print(r-a_len+1)
            
main()


# In[5]:


char_word = 'vikas134'
num = 0
for char in char_word:
    if(char.lower()==char.upper()):
        num = num*10 + int(char)
print(num)


# In[ ]:




