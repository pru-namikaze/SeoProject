import math
def val(i,rel):
    #importance value of each link in result page
    r = 1-(i-1)/100;
    r = r/math.log2(i+1)
    #print(r)

    #final value of each link in result page

    final_val = 0.7*r + 0.3 * rel
    #print(final_val)
    f = open('semantic_data.txt','a+')
    f.write("\n"+str(i)+"\t Importance_val="+str(r)+"\t final_val="+str(final_val)+"\n")
    f.close()
    return final_val