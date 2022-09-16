class CommonPrifix:
    def longestcommonprifix(self,li):
        if len(li)==0:
            return "List is Empty"
        comPre=li[0]
        for i in range(1,len(li)):
            temp=""
            if len(comPre)==0:                
                break
            for j in range(len(li[i])):
                if j<len(comPre) and comPre[j]==li[i][j]:
                    temp=temp+comPre[j]
                else:
                    break
            comPre=temp
        return comPre
li=["Java","JavaScript","Js"]
object=CommonPrifix()
print(object.longestcommonprifix(li))
