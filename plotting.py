# grab dataframe thats being generated in other file
from motion_detector import df
from bokeh.plotting import figure, show, output_file
# creating chart figure container
p=figure(x_axis_type='datetime',height=300,width=1000,title='Motion Detection Graph')
# left border = start time
# right border = end time
# top = fixed
# bottom = fixed
q=p.quad(left=df['Start'],right=df['End'],bottom=0,top=1, color='red')
output_file('index.html')
show(p)