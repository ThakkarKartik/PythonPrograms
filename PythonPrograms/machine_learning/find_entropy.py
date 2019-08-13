import numpy as np

def entropy(vals):
  sum=0.0
  norm=0.0
  for v in vals:norm+=v
  vals=[v/norm for v in vals]
  for v in vals:sum+=(v*np.log(v))
  return -1.0*sum
 
for i in range(10):
  print(i,entropy([1 for j in range(i)]))
