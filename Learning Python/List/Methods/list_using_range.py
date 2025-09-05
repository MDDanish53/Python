'''
list can be created using range function as -

1. range(start_no, end_no+1, step_count)
here, start_no = value where the list starts
      end_no+1 = value where the list stops (+1 as the last value is excluded)
      step_count = interval of values
2. convert this range into a list as - 
list(range(start_no, end_no+1, step_count))
'''

def_list = range(1, 11, 1)
org_list = list(def_list)
print(org_list)