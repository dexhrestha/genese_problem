def gcd(a, b):
    #if b is not 0 compute gcd again
    if b:
        return gcd(b, a % b)
    #if b is 0 gcd is a
    else:
        return a
    
def lcm(a,b):
    return int((a*b)/gcd(a,b))

def compute(start,end,ans=1):
    
    for i in range(start,end+1):
        ans = lcm(ans,i)
    return ans

print(compute(10,20,2520))