
import pandas as pd

import numpy as np

import matplotlib as mpl

import random

###INPUT###INPUT###INPUT###
Andrey = [0,2,6,5,4,1,3]
Sachka = [0,1,5,4,2,3,6]
Tony = [0,1,2,5,6,4,3]
Danesly = [6,1,2,3,4,5,0]
Ser_gay = [0,6,5,1,2,3,4]
###INPUT###INPUT###INPUT###

Random_dict = {'maps': ['Ancient', 'Nuke', 'Overpass', 'Mirage', 'Dust II', 'Vertigo', 'Inferno'],
               'names': [Andrey, Sachka, Tony, Danesly, Ser_gay],
               'names_n': ['Andrey', 'Sachka', 'Tony', 'Danesly', 'Ser_gay']}

Random_df = pd.DataFrame(Random_dict['names'], index = Random_dict['names_n'], columns = Random_dict['maps']).transpose()


Sum_list = []
for x in Random_dict['maps']:
    Sum_list.append(Random_df.loc[x].sum())
Sum_list_df = pd.DataFrame(Sum_list, index = Random_dict['maps'], columns = ['Sum'])

Random_sum_df = pd.merge(Random_df, Sum_list_df, left_index=True, right_index=True)
print(Random_sum_df)
point = random.randrange(sum(Random_sum_df['Sum']))

import matplotlib.pyplot as plt
print(Sum_list)
# set up the figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,10)
ax.set_ylim(0,10)

# draw lines
xmin = 0
xmax = 10
y = 5
height = 2

plt.hlines(y, xmin, 100)
plt.vlines(xmin, y - height / 2., y + height / 2.)
plt.vlines(xmin + Sum_list[0]/10.5, y - height / 2., y + height / 2.)
plt.vlines(xmin + sum(Sum_list[0:2])/10.5, y - height / 2., y + height / 2.)
plt.vlines(xmin + sum(Sum_list[0:3])/10.5, y - height / 2., y + height / 2.)
plt.vlines(xmin + sum(Sum_list[0:4])/10.5, y - height / 2., y + height / 2.)
plt.vlines(xmin + sum(Sum_list[0:5])/10.5, y - height / 2., y + height / 2.)
plt.vlines(xmin + sum(Sum_list[0:6])/10.5, y - height / 2., y + height / 2.)
plt.vlines(xmin + sum(Sum_list[0:7])/10.5, y - height / 2., y + height / 2.)
plt.vlines(xmax, y - height / 2., y + height / 2.)

# draw a point on the line
px = point/10.5
plt.plot(px,y, 'ro', ms = 3, mfc = 'r')

# add an arrow


# add numbers
plt.text(xmin - 0.1, y+1, 'Ancient', horizontalalignment='right', c = 'r', style = 'oblique', rotation = 'vertical', size = 'x-large')
plt.text(xmin - 0.1 + sum(Sum_list[0:1])/10.5, y+1, 'Nuke', horizontalalignment='right', c = 'orange', style = 'oblique', rotation = 'vertical', size = 'x-large')
plt.text(xmin - 0.1 + sum(Sum_list[0:2])/10.5, y+1, 'Overpass', horizontalalignment='right', c = 'gold', style = 'oblique', rotation = 'vertical', size = 'x-large')
plt.text(xmin - 0.1 + sum(Sum_list[0:3])/10.5, y+1, 'Mirage', horizontalalignment='right', c = 'green', style = 'oblique', rotation = 'vertical', size = 'x-large')
plt.text(xmin - 0.1 + sum(Sum_list[0:4])/10.5, y+1, 'Dust II', horizontalalignment='right', c = 'navy', style = 'oblique', rotation = 'vertical', size = 'x-large')
plt.text(xmin - 0.1 + sum(Sum_list[0:5])/10.5, y+1, 'Vertigo', horizontalalignment='right', c = 'purple', style = 'oblique', rotation = 'vertical', size = 'x-large')
plt.text(xmin - 0.1 + sum(Sum_list[0:6])/10.5, y+1, 'Inferno', horizontalalignment='right', c = 'plum', style = 'oblique', rotation = 'vertical', size = 'x-large')
plt.text(xmax + 0.1, y, '105', horizontalalignment='left')

#plt.annotate('Good game', (px,y), xytext = (px - 1, y + 1),
#             arrowprops=dict(facecolor='black', shrink=0.1),
#          horizontalalignment='right')

plt.show()