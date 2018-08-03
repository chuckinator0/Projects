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

# This program simulates the growth of an aphid population 
#   using a stage-structured model and compares it to data
#   from the large cage experiment.

# largecage.csv is a file that contains the data from the large cage experiment.
#	The first row contains column headers.
#	The first column contains the ID numbers for the cages.
#	The second column contains the number of aphids present on the first day of the experiment.
#		The second column should contain all 1s.
#	Subsequent columns contain the population count of aphids on the corresponding day.
#	No data should be included after coccinellids are introduced.


##
## DATA
##
## Import any data from files.
## Give values to any fixed parameters.
##

# read the large cage data from largecage.csv
# "large[i,j]" is the population of cage i on day j, with the first day as "day 1"
large <- read.csv("largecage.csv",header=TRUE)
large <- large[,-1]		
cages <- length(large[,1])
days <- length(large[1,])-1

# define the model size
stages <- 6	

# define the initial population of stage "i"
V0 <- c(0,0,0,0,0,1)

# define the average reproduction of new adults
m1 <- 4.695652

# define the average reproduction of adults after the first day of reproduction
m <- 3.865435

# define the probability of development from stage "j" to stage "i=j+1" 
p <- c(0.4210526,0.7142857,0.5384615,0.3793103,0.4545455)

# define the probability of survival in stage "i" without development 	
s <- c(0.5526316,0.2380952,0.4230769,0.5172414,0.5000000,0.9032258)

# define the probability of the transition from oldest nymph to reproducing adult
a <- 0.03448276


##
## INITIALIZATION
##
## Set up any running variables that need to have a starting value.
## Create any needed data structures.
##

# define the data structures for the model, populations, total population, proportions, and daily growth rates
M <- matrix(0,nrow=stages,ncol=stages)		# The model is "V[,j+1] = M %*% V[,j]"
V <- matrix(0,nrow=stages,ncol=days+1)		# "V[i,j]" is the population of stage "i" at time "j-1"
N <- rep(0,days+1)					# "N[j]" is the total population at time "j-1"
U <- matrix(0,nrow=stages,ncol=days+1)		# "U[i,j]" is the proportion of stage "i" at time "j-1"
R <- rep(0,days)						# "R[j]" is the ratio of "N" at time "j" to "N" at time "j-1"

# enter the initial populations into "V"
V[,1] <- V0

# enter the "p" values into "M" 
for (j in 1:stages-1)
	M[j+1,j] <- p[j]

# enter the "s" values into "M" 
for (j in 1:stages)
	M[j,j] <- s[j]

# enter "a" into "M"
M[6,4] <- a

# compute the fecundities (see Caswell book) and enter them into "M"
survival <- sqrt(sum(M[,1]))
M[1,stages] <- survival*(1+M[stages,stages])*m/2
M[1,stages-1] <- survival*M[stages,stages-1]*m1

# define the data structures for the large cage growth rates
mu <- rep(0,days)					# ratio for each day save the first
sigma <- rep(0,days)				# standard deviation for each day save the first


##
## FUNCTIONS
##
## Define any functions that the main program requires.
## Calculations that need to repeated at different points of a program should be
##   coded as functions.
##

# "eigen(M)" is a built-in function that determines the eigenvalues and eigenvectors of a matrix "M"
#    "eigen(M)$values[1] is the largest eigenvalue
#    "eigen(M)$vectors[,1]" is an eigenvector for the largest eigenvalue


##
## MAIN PROGRAM
##
## Perform the computations, using functions as needed.
##


## FIND THE LONG-TERM GROWTH RATE

# Compute eigenvalues and eigenvectors using "eigen"
result <- eigen(M)

# "lambda1" is the largest eigenvalue
lambda1 <- Re(result$values[1])	# "Re(x)" ignores any imaginary part of "x" (should be 0)


## RUN THE SIMULATION

# Compute "V"
for (t in 1:days)		# "t" is the new time value
	{	
	n <- t			# "n" is the column number for the old population values
	V[,n+1] <- M %*% V[,n]  # "V[,n+1]" is the column of new population values
	}

# Compute "N" 			# "N[j]" is the total population at time "j-1"
N <- colSums(V)

# Compute "U"			# "U[,j]" is the column of proportions at time "j-1"
for (j in 1:(days+1)) 
	U[,j] <- V[,j]/N[j]

# Compute "R" 			# "R[j]" is the ratio of "N" at time "j" to "N" at time "j-1"
R <- N[2:(days+1)]/N[1:days]	


## COMPUTE GROWTH RATES AND 95% CONFIDENCE INTERVALS FROM LARGE CAGE DATA

ratios <- large[,2:(days+1)]/large[,1:days]		# N2/N1, etc
for (day in 1:days)
	{
	mu[day] <- mean(ratios[,day])
	sigma[day] <- sd(ratios[,day])
	}
conf95 <- 1.96*sigma/sqrt(cages)


##
## FUNCTIONS FOR OUTPUT
##

# errorbars is a low-level plotting command that adds error bars to a set of plotted points.
#	The first argument is the set of x values.
#	The second argument is the set of y values.
#	The third argument is the height of the bar above and below the point.
#	The standard optional arguments col and lwd are accepted.
#	The optional argument 'cap' is a multiplier for the cap length.

errorbars <- function(x,y,dy,col="black",lwd=1,cap=1)
	{
	n <- length(x)
	top <- y+dy
	btm <- y-dy
	d <- cap*0.01*(max(x)-min(x))
	for (i in 1:n)
		{
		lines( c(x[i]  ,x[i]  ), c(btm[i],top[i]), col=col, lwd=lwd )
		lines( c(x[i]-d,x[i]+d), c(btm[i],btm[i]), col=col, lwd=lwd )
		lines( c(x[i]-d,x[i]+d), c(top[i],top[i]), col=col, lwd=lwd )
		}
	}


##
## OUTPUT
##
## Create any needed graphs.
## Display key results.
##

# determine the y-axis limit
ymax <- max(max(R),max(mu+conf95))

# plot the data for daily growth rate from the simulation
plot(1:days, R, pch=15, xlim=(c(0,days)), ylim=(c(0,ymax)), col="blue3", xlab="days", ylab="growth rate: N(t)/N(t-1)")

# connect the points in the simulated growth rate graph
lines(1:days, R, pch=15, col="blue3", lty=2)

# plot the long-term growth rate as an asymptote
abline(h=lambda1, lty=3)

# add the data for daily growth rate from the large cage experiment
points(1:days, mu, pch=16)
errorbars(1:days, mu, conf95)



