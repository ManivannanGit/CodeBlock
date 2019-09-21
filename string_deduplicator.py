def remove_duplicates(s):
    
    #Initialize three Variables
    
    i = 1
    m = 1
    f = 0
    
    while m < len(s):
        i = m
        
        while i < len(s):
            if s[i]==s[m-1]:
                i+=1
            else:break
        
        if i != m:
            f = 1
            s = s[:m-1]+s[i:]
            m-=1
            
        m += 1
        
    if f:
        return remove_duplicates(s)
    return s








#Main Function

def main():
    if __name__ == '__main__':
        sample_string = 'HelLo $$$World!!!'
        print(remove_duplicates(sample_string.lower()))
        
#Driver function

main()
