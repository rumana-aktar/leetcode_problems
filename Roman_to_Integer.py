import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def romanToInt(str):

    i = 0;     val = 0
    d={};      d['I']=1; 
    d['V']=5;  d['X']=10; d['L']=50;  d['C']=100; d['D']=500;  d['M']=1000;
    d['IV']=4; d['IX']=9; d['XL']=40; d['XC']=90; d['CD']=400; d['CM']=900;


    while i < len(str):
        if str[i:i+2] in d:
            val += d[str[i:i+2]]
            i += 2
        elif str[i] in d:
            val += d[str[i]]  
            i += 1
    return val     

print(romanToInt('LVIII'))         
print(romanToInt('LMVIII'))         
