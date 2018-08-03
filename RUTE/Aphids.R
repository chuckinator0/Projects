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

# This program simulates the growth of an aphid population using a stage-structured model.

##
## DATA
##
## Import any data from files.
## Give values to any fixed parameters.
##

# define the model size and the number of days
stages <- 6	
days <- 20     

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
N <- array(0,dim=days+1)				# "N[j]" is the total population at time "j-1"
U <- matrix(0,nrow=stages,ncol=days+1)		# "U[i,j]" is the proportion of stage "i" at time "j-1"
R <- array(0,dim=days)					# "R[j]" is the ratio of "N" at time "j" to "N" at time "j-1"

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


## FIND THE LONG-TERM GROWTH RATE AND AGE DISTRIBUTION

# Compute eigenvalues and eigenvectors using "eigen"
result <- eigen(M)

# "lambda1" is the largest eigenvalue
lambda1 <- Re(result$values[1])	# "Re(x)" ignores any imaginary part of "x" (should be 0)

# "proportions" is the normalized eigenvector for the largest eigenvalue
proportions <- Re(result$vectors[,1]/sum(result$vectors[,1]))

# "r" is the continuous growth rate, which we need for any differential equation model
r <- log(lambda1)				# "log" is natural logarithm


## RUN THE SIMULATION

# Compute "V"
for (t in 1:days)			# "t" is the new time value
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


##
## OUTPUT
##
## Create any needed graphs.
## Display key results.
##

# determine the y-axis limit
ymax <- min(max(R),3)

# plot the data for daily growth rate
plot(1:days, R, pch=15, xlim=(c(0,days)), ylim=(c(0,ymax)), col="blue3", xlab="days", ylab="growth rate: N(t)/N(t-1)")

# connect the points in the growth rate graph
lines(1:days, R, pch=15, col="blue3", lty=2)

# plot the long-term growth rate as an asymptote
abline(h=lambda1, lty=3)

# print the output quantities

M			# matrix for the model
lambda1		# dominant eigenvalue
proportions		# proportions of stages for stable distribution
r			# growth rate for continuous model


