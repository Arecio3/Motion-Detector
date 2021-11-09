# grab dataframe thats being generated in other file
from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

# Convert Start and End to date time strings
df['Start_String']=df['Start'].dt.strftime("%D %H:%M:%S")
df['End_String']=df['End'].dt.strftime("%D %H:%M:%S")
# to be able to use dataframe
cds=ColumnDataSource(df)

# creating chart figure container
p=figure(x_axis_type='datetime',height=300,width=1000,title='Motion Detection Graph')
# takes horizontal grid line
p.yaxis.minor_tick_line_color=None
# makes there only be 1 small line

# hover obj (@Col)
hover=HoverTool(tooltips=[("Entry Time","@Start_String"),("Exit Time","@End_String")])
p.add_tools(hover)
# left border = start time
# right border = end time
# top = fixed
# bottom = fixed
q=p.quad(left='Start',right='End',bottom=0,top=1, color='red',source=cds)
output_file('index.html')
show(p)