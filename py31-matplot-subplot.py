#subplot:
#Mina Hemmati

#Plotting two types of bar charts for the course scores
#of two individuals named Reza and Zahra.

import matplotlib.pyplot as plt
import numpy as np

source=["Physics","Chemistry","Mathematics","Literature","English","Religious","sport"]
rezascores=[13,19,15,17,14,14,19]
zahrascores=[19,17,15,18,18.5,17,18]


x=np.arange(len(source))
w=0.35

fig,ax=plt.subplots(1,2)


ax[0].bar(x-w/2 ,rezascores , width=w , label="Reza")
ax[0].bar(x+w/2 ,zahrascores , width=w , label="Zahra")

ax[0].set_ylabel("score")

ax[0].set_xticks(x)
ax[0].set_xticklabels(source, rotation=45, ha="right")

ax[0].legend(loc="lower center", bbox_to_anchor=(0.5, 1.05),
             fontsize=8, ncol=1)

# ncol=1 places the legend items vertically (one below another)
# fontsize=8 makes the legend text smaller
# bbox_to_anchor=(0.5, 1.05) moves the legend above the plot

ax[1].bar(source, rezascores, width=w ,  label='Reza')
ax[1].bar(source, zahrascores, width=w , bottom=rezascores,label='Zahra')
ax[1].set_xticks(x)
ax[1].set_ylabel("score")
ax[1].set_xticklabels(source, rotation=45, ha="right")

ax[1].legend(loc="lower center", bbox_to_anchor=(0.5, 1.05),
             fontsize=8, ncol=1)




fig.suptitle("scors")
plt.show()
