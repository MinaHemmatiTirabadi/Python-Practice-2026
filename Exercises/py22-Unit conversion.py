#unit conversion 

class convert_T:
    def __init__(self,T):
        self.t=T
    def F_C(self):
        F=self.t
        C=(F-32)*(5/9)
        return C
    def C_F(self):
        C=self.t
        F=(C*(9/5))+32
        return F
    def F_K(self):
        F=self.t
        K=(F+459.67)*(5/9)
        return K
    def K_F(self):
        K=self.t
        F=(K*(9/5))-459.67
        return F
    def K_C(self):
        K=self.t
        C=K-273.15
        return C
    def C_K(self):
        C=self.t
        K=C+273.15
        return K

class convert_L:
    def __init__(self,L):
        self.l=L
    def m_cm(self):
        m=self.l
        cm=m*100
        return cm
    def m_mm(self):
        m=self.l
        mm=m*1000
        return mm
    def cm_m(self):
        cm=self.l
        m=cm/100
        return m
    def cm_mm(self):
        cm=self.l
        mm=cm*10
        return mm
    def mm_cm(self):
        mm=self.l
        cm=mm/10
        return cm
    def mm_m(self):
        mm=self.l
        m=mm/1000
        return m
    def km_m(self):
        km=self.l
        m=km*1000
        return m
    def m_km(self):
        m=self.l
        km=m/1000
        return km
    
class convert_x:
    pass

class convert_litre:
    def __init__(self,lit):
         self.l=lit
    def l_ml(self):
        litre=self.l
        milliliter=litre*1000
        return milliliter
    def ml_l(self):
        milliliter=self.l
        litre=milliliter/1000
        return litre
    def l_g(self):
        litre=self.l
        gallon=litre*(0.26)
        return gallon
    def g_l(self):
        gallon=self.l
        litre=gallon*(3.7854)
        return litre
    def ml_g(self):
        milliliter=self.l
        gallon=milliliter*(0.00026)
        return gallon
    def g_ml(self):
        gallon=self.l
        milliliter=gallon*3785.4
        return milliliter
     
        
        

def convert_unit():
    k=int(input("you want convert_temprature:1,convert_length:2,"
                "convert_x:3, convert_litre:4 \n======\n"))
    if k==1:
        T=float(input("temprature="))
        m=int(input("enter F->C:1,C->F:2,F->K:3,K->F:4,K->C:5,C->K:6\n======\n"))
        convert=convert_T(T)
        if m==1:
            print(convert.F_C())
        elif m==2:
            print(convert.C_F())
        elif m==3:
            print(convert.F_K())
        elif m==4:
            print(convert.K_F())
        elif m==6:
            print(convert.K_C())
        elif m==7:
            print(convert.C_K())
    elif k==2:
        L=float(input("Length="))
        j=int(input("enter m->cm:1,m->mm:2,cm->m:3,cm->mm:4,mm->cm:5,"
                    "mm->m:6,km->m:7,m->km:8==="))
        convert=convert_L(L)
        if j==1:
            print(convert.m_cm())
        elif j==2:
            print(convert.m_mm())
        elif j==3:
            print(convert.cm_m())
        elif j==4:
            print(convert.cm_mm())
        elif j==5:
            print(convert.mm_cm())
        elif j==6:
            print(convert.mm_m())
        elif j==7:
            print(convert.km_m())
    elif k==3:
            convert=convert_x()
    elif k==4:
        lit=float(input("Volume= "))
        a=int(input("enter l->ml:1,ml->l:2,l->g:3,g->l:4,ml->g:5,"
                    "g->ml:6 ==="))
        convert=convert_litre(lit)
        if a==1:
            print(convert.l_ml())
        elif a==2:
            print(convert.ml_l())
        elif a==3:
            print(convert.l_g())
        elif a==4:
            print(convert.g_l())
        elif a==5:
            print(convert.ml_g())
        elif a==6:
            print(convert.g_ml())
            
        
restart = input("Do want to convert?(y/n)")
if restart == "y" or restart == "Y":
            convert_unit()
            
restart = input("Do want to convert?(y/n)")
if restart == "y" or restart == "Y":
        convert_unit()
        





        








    
    
