#!/usr/bin/env python
# coding: utf-8

# In[2]:


in_str = input()


# In[3]:


print(in_str)
fnaxtyyzz
gqtrawq


# In[33]:


def main():
    test_cases_num = int(input())
    if(1<=test_cases_num <=10):
        input_list=[]
        for i in range(0,test_cases_num):
            in_str = input()
            input_list.append(in_str)
        for in_str in input_list:
            char_list = list(in_str)
            if(1 <= len(char_list) <= 100000):
                char_dict={}
                for c in char_list:
                    if c not in char_dict:
                        char_dict[c]=1
                    else:
                        cnt = char_dict[c]
                        char_dict[c]=cnt+1
                max_occ_char_list = [key for m in [max(char_dict.values())] for key,val in char_dict.items() if val == m]
                ascii_dict={}
                for c in max_occ_char_list:
                    ascii_dict[c]=ord(c)
                print(min(ascii_dict, key=ascii_dict.get))
            
    
    


# In[34]:


main()


# In[ ]:




