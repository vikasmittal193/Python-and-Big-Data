'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''

s = ['aaab','abbcd','abcdrffqhwugqgfeg','AA']
t  = ['vvvv','bbcca','','ab']

def checksimilar(s,t):
    dict_s,dict_t={},{}
    result_array = []
    n = len(s)
    flag=0
    for i in range(n):
        if(len(s[i])==len(t[i])):
            s[i] = s[i].lower()
            t[i] = t[i].lower()
            for j in range(len(s[i])):
                if(s[i][j] in dict_s):
                    count_s = dict_s[s[i][j]]
                    count_s+=1
                    dict_s[s[i][j]] = count_s
                else:
                    dict_s[s[i][j]] = 1
                if(t[i][j] in dict_t):
                    count_t = dict_t[t[i][j]]
                    count_t+=1
                    dict_t[t[i][j]] = count_t
                else:
                    dict_t[t[i][j]] = 1
            list_merge = list(s[i])+list(t[i])
            for ele in list(set(list_merge)):
                if((ele in dict_s) and (ele in dict_t)):
                    diff = dict_s[ele] - dict_t[ele]
                    if(diff>3):
                       flag+=1
                elif((ele in dict_t and dict_t[ele]>3) or (ele in dict_s and dict_s[ele]>3)):
                    flag+=1
            if(flag>0):
                result_array.append('NO')
            else:
                result_array.append('YES') 
        else:
            result_array.append('NO')
        
        dict_s={}
        dict_t={}
        flag=0
    return result_array
result = checksimilar(s,t)
print(result)