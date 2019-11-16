num_list=[2,6,1,4,9,4,3]

def getbinary(num_list):
    import operator
    sort_list=[]
    bin_list=[]
    for num in num_list:
        bin_list.append(bin(num))
    for i in range(len(bin_list)):
        num_l=[]
        num_l.append(num_list[i])
        num_l.append(bin_list[i].replace('0b','').count('1'))
        sort_list.append(num_l)
    print(sort_list)
    sorted_list = sorted(sort_list, key = operator.itemgetter(1, 0))
    print(sorted_list)
    res_list=[x[0] for x in sorted_list]
    print(res_list)
getbinary(num_list)