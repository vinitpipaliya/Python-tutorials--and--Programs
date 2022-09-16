class RomantoInt:
    def romtoint(self,s):
        roman={'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000} #--> This is dictionary which i defined Roman numberes
        i=0
        number=0
        while(i<len(s)):
            if i+1<len(s) and s[i:i+2] in roman:
                number=number+roman[s[i:i+2]]
                i=i+2
            else:
                number=number+roman[s[i]]
                i=i+1
        return number
object=RomantoInt()
print(object.romtoint("MDCLXVI"))
print(object.romtoint("MXLIIICDLXM"))
