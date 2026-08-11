#If you only have $1,000 a month to pay off your mortgage,
#how long would it take to pay off an $8,000,000 loan at 28% interest per year?

#rate=0.08/12, pmt=-1000, pv=8000000

import numpy_financial as np
print(np.nper(0.08/12, -1000, 8000000))
