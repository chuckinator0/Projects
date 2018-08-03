# This program 
# 1) determines the average consumption rate for coccinellids by larval age
# 2) determines the average consumption rate for adult coccinellids
# 3) plots the average consumption rate versus age with the 95% confidence interval
# 	and the number of larvae in the sample on each day

# The program requires one data file.

# predation.csv is a file that contains the predation data.
#	The first row contains column headers.
#	The first column contains the ID numbers for the cages.
#	Rows 2 and 3 are the before and after counts of aphids for the larva in the first cage.
#	After all larvae data, there is a blank row.
#	The following rows are before and after counts for adults.
#	Use the numbers -1 to indicate pupation and -2 to indicate death.

# DATA

data <- read.csv("predation-1.csv",header=TRUE)
color <- "blue3"		# color for the secondary data and axis
maxdays <- 0		# cutoff for presentation of data--0 if all data is to be displayed
droplast <- FALSE  	# drops last fecundity value from the plot
adultsurvival <- TRUE	# if TRUE, adult survival affects the right axis scale
adjustment <- 0.95	# locates the "adults" label; should be 0.95 to 1

# INITIALIZATION

data <- data[,-1]
if (maxdays>0)
	data <- data[,1:maxdays]
rows <- length(data[,1])
days <- length(data[1,])

blankrow <- which(is.na(data[,1]))

larvaecages <- (blankrow-1)/2
adultcages <- (rows-blankrow)/2
larvae <- matrix(-1,nrow=larvaecages,ncol=days)
adults <- matrix(-1,nrow=adultcages,ncol=days)

mu <- rep(0,days)					# average for larvae for each day
sigma <- rep(0,days)				# standard deviation for larvae for each day
individuals <- rep(0,days)			# fraction of larvae still alive and not pupated
allvalues <- rep(0,0)				# list of all adult predation values

cutpoints <- 0
if (droplast==TRUE)
	cutpoints <- 1

# PREPARE DATA FILES

for (cage in 1:larvaecages)
	for (day in 1:days)
		if (is.na(data[2*cage,day])==FALSE)
			if (data[2*cage,day]>0)
				larvae[cage,day] <- data[2*cage-1,day]-data[2*cage,day]
for (cage in 1:adultcages)
	for (day in 1:days)
		if (is.na(data[blankrow+2*cage,day])==FALSE)
			if (data[blankrow+2*cage,day]>0)
				adults[cage,day] <- data[blankrow+2*cage-1,day]-data[blankrow+2*cage,day]
	
# COMPUTE MEANS AND 95% CONFIDENCE INTERVALS FROM DATA

for (day in 1:days)
	{
	thisday <- larvae[,day]					# selects the appropriate column
	values <- thisday[which(thisday>-1)]		# uses only positive entries
	mu[day] <- mean(values)
	sigma[day] <- sd(values)
	individuals[day] <- length(values)
	}
conf95 <- 1.96*sigma/sqrt(larvaecages)

for (day in 1:days)
	{
	thisday <- adults[,day]					# selects the appropriate column
	values <- thisday[which(thisday>-1)]		# removes the NA entries
	allvalues <- c(allvalues,values)
	}
q <- mean(allvalues)						# mean for all adults
stdev <- sd(allvalues)
c95 <- 1.96*stdev/sqrt(length(allvalues))

# FUNCTIONS 

# errorbars is a low-level plotting command that adds error bars to a set of plotted points.
#	The first argument is the set of x values.
#	The second argument is the set of y values.
#	The third argument is the height of the bar above and below the point.
#	The standard optional arguments col and lwd are accepted.
#	The optional argument 'cap' is a multiplier for the cap length.
#	The optional argument 'width' is the cap width; width=0 for automatic width

errorbars <- function(x,y,dy,col="black",lwd=1,cap=1,width=0)
	{
	n <- length(x)
	top <- y+dy
	btm <- y-dy
	if (width>0)
		d <- width
	else
		d <- cap*0.015*(max(x)-min(x))
	for (i in 1:n)
		{
		lines( c(x[i]  ,x[i]  ), c(btm[i],top[i]), col=col, lwd=lwd )
		lines( c(x[i]-d,x[i]+d), c(btm[i],btm[i]), col=col, lwd=lwd )
		lines( c(x[i]-d,x[i]+d), c(top[i],top[i]), col=col, lwd=lwd )
		}
	return(d)
	}

# secondplot is a low-level plotting command that adds a second y axis.
#	The first argument is the set of y values for the second axis.
#	The standard optional argument col is accepted.
#	The optional argument 'min0' is TRUE if you want the new axis to start at 0.
#	The optional argument 'ylab' is the axis title.
#	The function returns the scale factor for plotting the data.

secondplot <- function(y,min0=FALSE,ylab="",col="black")
	{
	yticksleft <- axTicks(2)
	ymaxleft <- max(yticksleft)
	if (min0==TRUE)
		y <- c(0,y)
	yticksright <- pretty(y,n=length(yticksleft)-1)
	ymaxright <- max(yticksright)
	scale <- ymaxleft/ymaxright
	axis(4, at=scale*yticksright, labels=yticksright, col=col, col.axis=col)
	mtext(ylab, side=4, line=2.8, col=col)
	return(scale)
	}

# OUTPUT

par(mar=c(5.1,4.1,4.1,4.1)) 			
	# creates space on the right side of the plot for the axis label

ymax <- max( max(pretty(mu+conf95)), max(pretty(q+c95)) )
plot(1:(days-cutpoints), mu[1:(days-cutpoints)], pch=15, 
		xlim=(c(0,days+3)), ylim=(c(0,ymax)), 
		xaxt="n", xlab="age of larvae (days)", ylab="predation")
d <- errorbars(1:(days-cutpoints), mu[1:(days-cutpoints)], conf95[1:(days-cutpoints)])
xticks <- axTicks(1)
marks <- which(xticks<=days)
axis(1, at=xticks[marks], labels=xticks[marks])
if (adultsurvival==FALSE)
	scale <- secondplot(individuals,min0=TRUE,ylab="individuals",col=color)
if (adultsurvival==TRUE)
	scale <- secondplot(c(individuals,length(allvalues)),min0=TRUE,ylab="individuals",col=color)
points(1:days, scale*individuals, pch=16, col=color)
lines(1:days, scale*individuals, lty=3, col=color)
abline(v=days+1,lwd=2)
points(days+2.3, q, pch=15)
d <- errorbars(days+2.3, q, c95, width=d)
points(days+2.3, scale*length(allvalues), pch=16, col=color)
mtext("adults", side=1, line=3, adj=adjustment)

q
c95


