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

# This program simulates the growth of the boxbug population
#   using a stage-structured model.
# This version assumes an initial population of adults only.
#   Some simple changes are needed for the more general case.

##
## DATA
##
## Import any data from files.
## Give values to any fixed parameters.
##

f <- 3.05    # average number of offspring per adult per day
p <- 0.591  # fraction of larvae that pupate each day
a <- 0.4  # fraction of adults that survive each day
s <- 0.3181  #fraction of larvae that come back as larvae
A0 <- 3   # initial number of adults (0 larvae and pupae)
#	[* L0 and P0 need to be defined if not 0. *]
T <- 38   # total number of days

##
## INITIALIZATION
##
## Set up any running variables that need to have a starting value.
## Create any needed data structures.
##

L <- array(0,dim=T+1)	# L[i] is larvae population at time i-1
P <- array(0,dim=T+1)	# P[i] is pupae population at time i-1
A <- array(0,dim=T+1)	# A[i] is adult population at time i-1
A[1] <- A0

#	[* L[1] and P[1] need to be set if not 0. *]
# Stuff to add to do ratios:


RA <- array(0,dim=T)	# RA[j] is A at time j / A at time j-1
RL <- array(0,dim=T)	# RL[j] is L at time j / L at time j-1
RP <- array(0,dim=T)	# RP[j] is P at time j / P at time j-1



##
## FUNCTIONS
##
## Define any functions that the main program requires.
## Calculations that need to repeated at different points of a program should be
##   coded as functions.
##

# No functions are required.

##
## MAIN PROGRAM
##
## Perform the computations, using functions as needed.
##

# Simulation

for (t in 1:T){	# new time value
	n <- t 	# list position of the old population value
	i <- t+1	# list position of the new population value
	L[i] <- s*L[n]+f*A[n] 
	P[i] <- p*L[n]
	A[i] <- a*A[n]+P[n]
	
	j <- t      # list position of the new ratio value

	RA[j] <- A[i]/A[n]
	if (t>1) RL[j] <- L[i]/L[n]	# else old population could be 0
	if (t>2) RP[j] <- P[i]/P[n]	# else old population could be 0
#	[* The above conditions should be removed if P0 and L0 not 0. *]

}

##
## OUTPUT
##
## Create any needed graphs.
## Display key results.
##

par(mfrow=c(1,2))

# plot 1

plot(0:T, L, pch=15, col="green3", xlab="time", ylab="populations")
points(0:T, P, pch=16, col="purple3")
points(0:T, A, pch=17, col="red3")
legend(0,10000,legend=c("Larvae","Pupae","Adults"),pch=c(15,16,17),col=c("green3","purple3","red3"))
#	[* The legend location may need to be adjusted. *]



# plot 2

plot(2:T, RL[2:T], pch=15, xlim=(c(0,T)), col="green3", xlab="time", ylab="growth rates")
points(3:T, RP[3:T], pch=16, col="purple3")
#	[* The x values in the above should both be 1:T if P0 and L0 not 0. *]
points(1:T, RA, pch=17, col="red3")
legend(1,28,legend=c("Larvae","Pupae","Adults"),pch=c(15,16,17),col=c("green3","purple3","red3"))
#	[* The legend location may need to be adjusted. *]

