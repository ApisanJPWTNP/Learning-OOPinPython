class monomial:
    def __init__(self,a,k,is_positive):
        self.a = a
        self.k = k
        self.is_positive = is_positive
    def is_monomial(self):
        for deg in self.k:
            if deg < 0 or not isinstance(deg,int):
                return False
            else:
                return True
    def find_max_deg(self):
        return max(self.k)
    def is_constant(self):
        x=0
        for m in self.k:
            if m > 0:
                x+=1
            elif m==0:
                continue
            else:
                continue
        if x==len(self.k):
            return False
    def num_of_variable(self):
        return len(self.k)
    def in_math_term(self):
        if self.k[0]==0:
            if self.is_positive==True:
                print('{}'.format(self.a),end ="")
            else:
                print('-{}'.format(self.a),end ="")
        else:
            if self.k[0]==1:
                if self.is_positive==True:
                    print ('{}x_0'.format(self.a),end ="")
                else:
                    print ('-{}x_0'.format(self.a),end ="")
            else:
                if self.is_positive==True:
                    print ('{}x_0^{}'.format(self.a, self.k[0]),end ="")
                else:
                    print ('-{}x_0^{}'.format(self.a, self.k[0]),end ="")
        n = 1
        while n!=len(self.k)-1:
            if self.k[n]==0:
                print('')
                n+=1
            elif self.k[n]==1:
                print ('x_{}'.format(n), end ="")
                n+=1
            else:
                print ('x_{}^{}'.format(n,self.k[n]), end ="")
                n+=1
        if n==len(self.k)-1:
            if self.k[n]==0:
                return ""
            else:
                return 'x_{}^{}'.format(n,self.k[n])
            
def is_it_similar(k1,k2):
    if len(k1)!=len(k2):
        return False
    else:
        x=0
        for i in range(len(k1)):
            if k1[i]!=k2[i]:
                x+=1
        if x!=0:
            return False
        else:
            return True
        
def add_monomial(a1,k1,is_positive1,a2,k2,is_positive2):
    if is_it_similar(k1,k2)==True:
        if is_positive1==False:
            a1=-a1
        if is_positive2==False:
            a2=-a2
        if a1+a2>=0:
            is_positive=True
        else:
            is_positive=False
        return monomial(abs(a1+a2),k1,is_positive).in_math_term()
    else:
        return ("can't be added")
    
def multiply_monomial(a1,k1,is_positive1,a2,k2,is_positive2):
    c=[]
    for i in range(0,min(len(k1),len(k2))):
        c.append(k1[i]+k2[i])
    if len(k1)>=len(k2):
        d=k1
    else:
        d=k2
    for i in range(min(len(k1),len(k2)),max(len(k1),len(k2))):
        c.append(d[i])
    # print(c) # power
    if is_positive1!=is_positive2:
        is_positive=False
    else:
        is_positive=True
    return monomial(abs(a1*a2),c,is_positive).in_math_term()

def perfect_square(a):
    psl=[]
    for i in range(1,a+1):
        psl.append(i*i)
    for i in range(0,a):
        if (psl[i]%a==0):
            return psl[i]//a
        
def complementary_monomial(a1,k1,is_positive1):
    powerlist=[]
    for i in k1:
        if i%2==0:
            powerlist.append(0)
        else:
            powerlist.append(1)
    # return powerlist
    return monomial(perfect_square(a1),powerlist,is_positive1).in_math_term()
# print(multiply_monomial(1,[1,2,4],True,2,[1,2,4],False))
# print(perfect_square(3))
print(complementary_monomial(12,[1,3,4],False))