import math
d_cod={}

def coder(d_sort,len_res1,c,d_cod_u):
    count_half_len=0
    one_let=""
    zero_let=""
    for i in c:
        count_half_len+=d_sort[i]
        one_let+=i
        if count_half_len>=((len_res1/2)-1):
            break
    for i in c:
        if one_let.count(i)==0:
            zero_let+=i
            d_cod[i]+="0"
        else:
            d_cod[i]+="1"
    if len(c)<=2:
        return 1
    elif len(c)==3:
        if len(zero_let)==2:
            coder(d_sort,len_res1/2,zero_let,d_cod_u)
        else:
            coder(d_sort,len_res1/2,one_let,d_cod_u)
    elif len(c)>3:
        coder(d_sort,len_res1/2,one_let,d_cod_u)
        coder(d_sort,len_res1/2,zero_let,d_cod_u)
    return "end"

def coder_haff_1(d_haff,len_res1,c):
    a=""
    min_haff_2="belg"
    min_haff_1="gleb"
    d_haff2={}
    d_haff2["gleb"]="99999999999999"
    p=""
    d_haff1=sorted(d_haff.items(), key=lambda item: item[1],reverse=True)
    for i in range(len(d_haff1)):
        a=d_haff1[i]
        d_haff2[a[0]]=a[1]
        p+=a[0]

        if (int(a[1])<=int(d_haff2[min_haff_1])):
            min_haff_2=min_haff_1
            min_haff_1=a[0]
    for i in range(len(min_haff_1)):
        code_haff_1[min_haff_1[i]]+="0"
    for i in range(len(min_haff_2)):
        code_haff_1[min_haff_2[i]]+="1"
    if(len(min_haff_1)+len(min_haff_2))==len(p):
        return "end"
    else:
        g={}
        for i in c:
            if min_haff_1.count(i)==0 and min_haff_2.count(i)==0:
                g[i]=d_haff2[i]
        g[min_haff_1+min_haff_2]=d_haff2[min_haff_1]+d_haff2[min_haff_2]
        coder_haff_1(g,len_res1,g.keys())



def coder_haff_2(d_haff,len_res1,c):
    a=""
    min_haff_2="belg"
    min_haff_1="gleb"
    d_haff2={}
    d_haff2["gleb"]="99999999999999"
    p=""
    d_haff1=sorted(d_haff.items(), key=lambda item: item[1],reverse=True)
    for i in range(len(d_haff1)):
        a=d_haff1[i]
        d_haff2[a[0]]=a[1]
        p+=a[0]
        if (int(a[1])<=int(d_haff2[min_haff_1])):
            min_haff_2=min_haff_1
            min_haff_1=a[0]
    for i in range(0,len(min_haff_1)-1,2):
        code_haff_2[min_haff_1[i]+min_haff_1[i+1]]+="0"
    for i in range(0,len(min_haff_2)-1,2):
        code_haff_2[min_haff_2[i]+min_haff_2[i+1]]+="1"
    if(len(min_haff_1)/2+len(min_haff_2)/2)==len(p)/2:
        return "end"
    else:
        g={}
        for i in c:
            if min_haff_1.count(i)==0 and min_haff_2.count(i)==0:
                g[i]=d_haff2[i]
        g[min_haff_1+min_haff_2]=d_haff2[min_haff_1]+d_haff2[min_haff_2]
        coder_haff_2(g,len_res1,g.keys())
      
def coder_dva(d_sort,len_res1,c):
    b=c.split()
    c=""
    for i in b:
        c+=i
    count_half_len=0
    one_let=""
    zero_let=""
    for i in range(0,int(len_res1)-1,2):
        i=c[i]+c[i+1]
        count_half_len+=d_sort[i]
        one_let+=i
        one_let+=""
        if count_half_len>=((len_res1/4)-1):
            break
    for i in range(0,int(len_res1)-1,2):
        i=c[i]+c[i+1]
        if one_let.count(i)==0:
            zero_let+=i
            zero_let+=""
            res_cod[i]+="0"
        else:
            res_cod[i]+="1"
            4+6
    if len(c)<=4:
        return 1
    elif len(c)==6:
        if len(zero_let)==4:
            coder_dva(d_sort,len(zero_let),zero_let)
        else:
            coder_dva(d_sort,len(one_let),one_let)
    elif len(c)>6:
        coder_dva(d_sort,len(one_let),one_let)
        coder_dva(d_sort,len(zero_let),zero_let)
    return "end"



f = open('hello_in.txt','r',encoding = "cp1251")
alp="qwertyuiopasdfghjklzxcvbnm"
res = ['']
res = f.read().replace('.',' ').replace(',',' ').replace(';',' ').replace('!',' ').replace('©',' ').replace('?',' ').replace(':',' ').replace('-',' ').replace('(',' ').replace(')',' ').replace('"',' ').replace("'"," ").split(' ')
tk = 0
k = 0
res1 = ''

for i in res:
    res1 += i
res1 = res1.lower()
print(res1)
resu = ['']
counter = 0
max1=0
text=""
min1=99999999999999999999999999
min2=99999999999999999999999999
min3=99999999999999999999999999
min4=99999999999999999999999999
min5=99999999999999999999999999
text1=""
max2=0
max3=0
max4=0
max5=0
d={}
d_double={}
col_sim=0
for i in res1:

    resc =['']
    if i in resu:
        4+6
    else:
        col_sim+=1
        resu+=i
        resc=res1.count(i)
        counter-=(resc/len(res1) * math.log2(resc/len(res1)))
        d[i]=resc
        print(i,resc)
        if max1<resc:
            max1=resc
            max2=max1
            max3=max2
            max4=max3
            max5=max4
            text=i
        if min1>resc:
            min1=resc
            min2=min1
            min3=min2
            min4=min3
            min5=min4
            text1=i

counter2=counter
counter2+=(max1/len(res1) * math.log2(max1/len(res1)))
counter2+=(max2/len(res1) * math.log2(max2/len(res1)))
counter2+=(max3/len(res1) * math.log2(max3/len(res1)))
counter2+=(max4/len(res1) * math.log2(max4/len(res1)))
counter2+=(max5/len(res1) * math.log2(max5/len(res1)))

print('entr-20%(max)',"  ",counter2)

counter3=counter
counter3+=(min1/len(res1) * math.log2(min1/len(res1)))
counter3+=(min2/len(res1) * math.log2(min2/len(res1)))
counter3+=(min3/len(res1) * math.log2(min3/len(res1)))
counter3+=(min4/len(res1) * math.log2(min4/len(res1)))
counter3+=(min5/len(res1) * math.log2(min5/len(res1)))

print('entr-20%(min)',"  ",counter3)

print('entr',"  ",counter)
print('entr_bykva',"  ",counter/len(res1))
counter1 =0
resu = ''
for i in range(0,(len(res1)-1),2):
        resc = ''
        c=res1[i]+res1[i+1]
        if c in resu:
            4+6
        else:
            resu+=c
            resu+=" "
            resc=res1.count(c)
            counter1-=(resc/len(res1) * math.log2(resc/len(res1)))
            d_double[c]=resc
            print(c,resc)

print('entr',"  ",counter1)
print("len",len(res1))
cod_len=len(res1)*5
print("codelen",len(res1)*5)
print("izb",1-(counter/math.log2(26)))
#//2//
f.close()
f = open("hello_out.txt","w")
for index in res1:
    f.write(index)
f.close()
d_sort={}
d_sort1={}
c=""
d_sort=sorted(d.items(), key=lambda item: item[1])
for i in range(col_sim):
    a=d_sort[i]
    d_sort1[a[0]]=a[1]
    c+=a[0]
d_cod={}
add_a=0
c_1=""

for i in c:# alp
    d_cod[i]=""

d_cod_u=""
d_sort={}
d_sort1={}
c=""
count_not_in_c_1=""
d_sort=sorted(d.items(), key=lambda item: item[1],reverse=True)
for i in range(len(d_sort)):
    a=d_sort[i]
    d_sort1[a[0]]=a[1]
    c+=a[0]
add_a=0
c_1=""
print(d_sort1)
coder(d_sort1,len(res1),c,d_cod_u)
print("1 letter cod(sh-f): ",d_cod)
new_cod_len=0
for i in res1:
    new_cod_len+=len(d_cod[i])
print("new cod len: ",new_cod_len)
print("profit: ",cod_len-new_cod_len)
eff=0
for i in c:
    eff+=d_sort1[i]*2
print("eff",eff/len(res1))
res_cod=""
for i in res1:
    res_cod+=d_cod[i]
    res_cod+=" "
print("coded text: ",res_cod)
res_spl=res_cod.split(" ")
res_spl[-1]=" "
res_cod_dec=""
for i in res_spl:
    for j in c:#alp
        if d_cod[j]==i:
            res_cod_dec+=j
print("before: ",res1)
print("after: ",res_cod_dec)
print("///////////////////////////////////dvubukv/////////////////////////////////////")
d_sort1={}
c=""
d_sort=sorted(d_double.items(), key=lambda item: item[1],reverse=True)
for i in range(0,len(d_sort)):
    a=d_sort[i]
    d_sort1[a[0]]=a[1]
    c+=(a[0])
res_cod={}

for i in range(0,len(res1)-1,2):    
    res_cod[res1[i]+res1[i+1]]=""
coder_dva(d_sort1,len(res1),c)
print("2 bykv cod(sh-f): ",res_cod)
for i in range(0,len(res1)-1,2):
    new_cod_len+=len(res_cod[c[i]+c[i+1]])
print("new cod len(2 letter c): ",new_cod_len)
print("profit: ",cod_len-new_cod_len)
eff=0
w=res_cod.keys()
for i in w:
    eff+=d_sort1[i]*2
print("eff 2",eff/(len(res1)/2))
res_code=""
for i in range(0,len(res1)-1,2):
    res_code+=res_cod[c[i]+c[i+1]]
    res_code+=" "
print("coded text: ",res_code)
res_spl=res_code.split(" ")
for i in range(0,len(res_spl)-1,2):
    i=res_spl[i]+res_spl[i+1]
    for j in range(0,len(c)-1,2):
        j=c[j]+c[j+1]
        if res_cod[j]==i:
            res_cod_dec+=j
print("before: ",res1)
print("after: ",res_cod_dec)
print("///////////////////////////////////haff/////////////////////////////////////")

code_haff_1={}
for i in c:
    code_haff_1[i]=""
coder_haff_1(d,len(res1),code_haff_1.keys())#
print("1 letter cod(haff): ",code_haff_1)
new_cod_len=0
for i in res1:
    new_cod_len+=len(code_haff_1[i])
print("new cod len: ",new_cod_len)
print("profit: ",cod_len-new_cod_len)
res_cod=""
for i in res1:
    res_cod+=code_haff_1[i]
    res_cod+=" "
print("coded text: ",res_cod)
res_spl=res_cod.split(" ")
res_spl[-1]=" "
res_cod_dec=""
for i in res_spl:
    for j in code_haff_1.keys():#alp
        if code_haff_1[j]==i:
            res_cod_dec+=j
print("before: ",res1)
print("after: ",res_cod_dec)

print("///////////////////////////////////haff-dva/////////////////////////////////////")



d_sort1={}
c=""
d_sort=sorted(d_double.items(), key=lambda item: item[1],reverse=True)
for i in range(0,len(d_sort)):
    a=d_sort[i]
    d_sort1[a[0]]=a[1]
    c+=(a[0])

code_haff_2={}

for i in range(0,len(res1)-1,2):    
    code_haff_2[res1[i]+res1[i+1]]=""

print("#",d_sort1,"#")
coder_haff_2(d_sort1,len(res1),d_sort1.keys())

print("2 bykv cod(haff): ",code_haff_2)
for i in range(0,len(res1)-1,2):
    new_cod_len+=len(code_haff_2[c[i]+c[i+1]])
print("new cod len(2 letter c): ",new_cod_len)
print("profit: ",cod_len-new_cod_len)
res_code=""
for i in range(0,len(res1)-1,2):
    res_code+=code_haff_2[c[i]+c[i+1]]
    res_code+=" "
print("coded text: ",res_code)
res_spl=res_code.split(" ")

for i in range(0,len(res_spl)-1,2):
    i=res_spl[i]+res_spl[i+1]
    for j in range(0,len(c)-1,2):
        j=c[j]+c[j+1]
        if code_haff_2[j]==i:
            res_cod_dec+=j
print("before: ",res1)
print("after: ",res_cod_dec)











