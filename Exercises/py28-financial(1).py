#What is the present value (i.e., initial investment) of an investment that,
#after 10 years of saving $100 per month,
#would total $15,692.93? Assume the interest rate is 5% (annually).
#rate , nper , pmt , pv , fv


import numpy_financial as np
print(np.fv(0.05/12,10*12,-100,-15692.93))
