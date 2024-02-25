candidates={"a":0,"b":0,"c":0}
reg_no=("v2010","v3011","v4013","v2014","v5016","v6019","v7022","v8031","v9088")
invalid=0

def main():
    for i in reg_no:
        reg=str(input("Enter Your Vote Registration Number:-"))
        if reg in reg_no:
            vote=input(f"{reg} you vote for:-").lower()
            if vote in candidates:
                candidates[vote]+=1
            else:
                invalid+=1    

    print(candidates,invalid)
               
main()               
