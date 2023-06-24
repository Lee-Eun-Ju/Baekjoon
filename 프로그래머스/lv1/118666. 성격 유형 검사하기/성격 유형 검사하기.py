
def solution(survey, choices):
    
    answer = {"R":0,"C":0,"J":0,"A":0,
              "T":0,"F":0,"M":0,"N":0}
    
    for i,x in enumerate(survey):        
        if choices[i]<4:
            answer[x[0]] += 4-choices[i]
        elif choices[i]>4:
            answer[x[1]] += choices[i]-4
    
    result = ""
    if answer["R"]>=answer["T"]:
        result = result + "R"
    else :
        result = result + "T"
        
    if answer["C"]>=answer["F"]:
        result = result + "C"
    else :
        result = result+"F"
        
    if answer["J"]>=answer["M"]:
        result = result+"J"
    else :
        result = result+"M"
        
    if answer["A"]>=answer["N"]:
        result = result+"A"
    else :
        result = result+"N"
        
    return result