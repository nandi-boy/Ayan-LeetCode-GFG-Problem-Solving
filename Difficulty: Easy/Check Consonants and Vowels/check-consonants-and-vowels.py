class Solution:
    def checkString(self, s):
        
        # Initializing vowel count
        # and consonant count to 0
        v = 0
        c = 0
        
        for ch in s:
            if ((ch>='A' and ch<='Z') or (ch>='a'and ch<='z')):
                ch = ch.lower()
                if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
                    v+=1
                else:
                    c+=1
        if v>c:
            print('Yes')
        elif c>v:
            print('No')
        else:
            print('Same')