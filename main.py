nested_list=[[3,4,5,[99,3,2]],[2,3,5,9,[33,[11,[22,102,111]]]],[77,88,99]]
output=[]

def flaten_list(nested_list):
  for element in nested_list:
    if type(element) is list:
      for item in element:
        #print(item)
        if type(item) is list:
          flaten_list(item)
        else:
          output.append(item)
    else:
      output.append(element)

  return(output)

if __name__=="__main__":
  print(flaten_list(nested_list))
