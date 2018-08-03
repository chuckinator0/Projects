##
## General note on program comments:
##
## Comments with "##" are standard to all my programs.
## Comments with "#" are descriptive of the specific program.
## Comments with "#." are lines of program code that can be used by deleting the "#.".
##

##
## General note on program structure:
## 
## It is generally best to look at the program elements in this order:
##  1. INTRODUCTION
##  2. OUTPUT
##  3. DATA
##  4. INITIALIZATION
##  5. MAIN PROGRAM
##  6. FUNCTIONS
##

##
## INTRODUCTION
##

# This program 
# 1) determines the average birth rate for aphids that have previously reproduced
# 2) determines the average birth rate for aphids that have not previously reproduced
# 3) plots the average reproduction versus age with the 95% confidence interval
# 	and the fraction of aphids surviving up to the corresponding day

# m1 is the average fecundity for aphids on the first day of reproduction
# m is the survival-weighted average fecundity for aphids beyond the first day of reproduction

# The program requires one data file.

# fecundity.csv is a file that contains the fecundity data from the clip-cage experiment.
#	The first row contains column headers.
#	The first column contains the ID numbers for the cages.
#	The second column contains the number of offspring on the first day of reproduction.
#	Subsequent columns contain the number of offspring on the corresponding day.
#	No data should be included for the day in which the adult aphid died.


##
## DATA
##
## Import any data from files.
## Give values to any fixed parameters.
##

# read the development file and remove ID numbers
data <- read.csv("fecundity.csv",header=TRUE)
data <- data[,-1]

# choose a color for secondary data and axis
color <- "blue3"						# color for the secondary data and axis


##
## INITIALIZATION
##
## Set up any running variables that need to have a starting value.
## Create any needed data structures.
##

# determine the number of rows (aphids) and columns (days) in the data file
aphids <- length(data[,1])
days <- length(data[1,])

# define the data structures for the transitions and parameters
mu <- rep(0,days)					# average for each day
sigma <- rep(0,days)				# standard deviation for each day
survival <- rep(0,days)				# fraction of aphids still alive
allvalues <- rep(0,0)				# list of all fecundity values other than day 1


##
## MAIN PROGRAM
##
## Perform the computations, using functions as needed.
##

## COMPUTE MEANS AND 95% CONFIDENCE INTERVALS FROM DATA

for (day in 1:days)
	{
	thisday <- data[,day]					# selects the appropriate column
	values <- thisday[which(is.na(thisday)==FALSE)]	# removes the NA entries
	mu[day] <- mean(values)
	sigma[day] <- sd(values)
	survival[day] <- length(values)/aphids
	}
conf95 <- 1.96*sigma/sqrt(aphids)
m1 <- mu[1]

for (day in 2:days)
	{
	thisday <- data[,day]					# selects the appropriate column
	values <- thisday[which(is.na(thisday)==FALSE)]	# removes the NA entries
	allvalues <- c(allvalues,values)
	}
m <- mean(allvalues)						# mean for all but day 1
stdev <- sd(allvalues)					
c95 <- 1.96*stdev/sqrt(length(allvalues))


##
## FUNCTIONS FOR OUTPUT
##
## Define any functions that the output program requires.
##

# "errorbars" is a low-level plotting command that adds error bars to a set of plotted points.
#	The first argument is the set of "x" values.
#	The second argument is the set of "y" values.
#	The third argument is the height of the bar above and below the point.
#	The standard optional arguments col and lwd are accepted.
#	The optional argument "cap" is a multiplier for the cap length.

errorbars <- function(x,y,dy,col="black",lwd=1,cap=1)
	{
	n <- length(x)
	top <- y+dy
	btm <- y-dy
	d <- cap*0.015*(max(x)-min(x))
	for (i in 1:n)
		{
		lines( c(x[i]  ,x[i]  ), c(btm[i],top[i]), col=col, lwd=lwd )
		lines( c(x[i]-d,x[i]+d), c(btm[i],btm[i]), col=col, lwd=lwd )
		lines( c(x[i]-d,x[i]+d), c(top[i],top[i]), col=col, lwd=lwd )
		}
	}

# "secondplot" is a low-level plotting command that adds a second "y" axis.
#	The first argument is the set of "y" values for the second axis.
#	The standard optional argument col is accepted.
#	The optional argument "min0" is "TRUE" if you want the new axis to start at 0.
#	The optional argument "ylab" is the axis title.
#	The function returns the scale factor for plotting the data.

secondplot <- function(y,min0=FALSE,ylab="",col="black")
	{
	yticksleft <- axTicks(2)
	ymaxleft <- max(yticksleft)
	if (min0)
		y <- c(0,y)
	yticksright <- pretty(y,n=length(yticksleft)-1)
	ymaxright <- max(yticksright)
	scale <- ymaxleft/ymaxright
	axis(4, at=scale*yticksright, labels=yticksright, col=col, col.axis=col)
	mtext(ylab, side=4, line=2.8, col=col)
	return(scale)
	}


##
## OUTPUT
##
## Create any needed graphs.
## Display key results.
##

# set up the plot window
par(mar=c(5.1,4.1,4.1,4.1))

# determine the "y" axis limit
ymax <- max(pretty(mu+conf95))

# plot the daily averages as points
plot(1:days, mu, pch=15, 
	xlim=(c(0,days+1)), ylim=(c(0,ymax)), xlab="days as reproducing adult", ylab="fecundity")

# use "errorbars" to add error bars
errorbars(1:days, mu, conf95)

# use "secondplot" to add a second "y" axis and determine the scale
scale <- secondplot(survival,min0=TRUE,ylab="survival",col=color)

# add survival data as both points and lines
points(1:days, scale*survival, pch=16, col="blue3")
lines(1:days, scale*survival, lty=3, col="blue3")

m1
m
c95
