#statistics module example:

import statistics as st

Data1=[0,-1,3,4,3,4,0,5,8,9,-4,0,4,5]
Data2=[456.7,547.8,926.6,236.1,543,439]

print("mean Data1 = ", st.mean(Data1))
print("mean Data2 = ", st.mean(Data2))

print("---------------------------------------")

print("geometric_mean Data2 = ", st.geometric_mean(Data2))

print("---------------------------------------")

print("harmonic_mean Data1 = ", st.harmonic_mean(Data1))
print("harmonic_mean Data2 = ", st.harmonic_mean(Data2))

print("---------------------------------------")

print("median Data1 = ", st.median(Data1))
print("median Data2 = ", st.median(Data2))

print("---------------------------------------")

print("variance Data1 = ", st.variance(Data1))
print("variance Data2 = ", st.variance(Data2))
print("pvariance Data1 = ", st.pvariance(Data1))
print("pvariance Data2 = ", st.pvariance(Data2))

print("---------------------------------------")

print("standard deviation Data1 = ", st.stdev(Data1))
print("standard deviation Data2 = ", st.stdev(Data2))
print("pstandard deviation Data1 = ", st.pstdev(Data1))
print("pstandard deviation Data2 = ", st.pstdev(Data2))
