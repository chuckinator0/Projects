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

##
## DATA
##
## Import any data from files.
## Give values to any fixed parameters.
##

f <- 2.87    # average number of offspring per adult per day
a <- .5   # fraction of adults that survive each day
p <- .67   # fraction of larvae that pupate each day
s <- .083  # fraction of larvae that survive without pupating each day
L0 <- 0   # initial number of larvae
P0 <- 0   # initial number of pupae
A0 <- 1   # initial number of adults
T <- 20   # total number of days

##
## INITIALIZATION
##
## Set up any running variables that need to have a starting value.
## Create any needed data structures.
##

V <- matrix(0,nrow=3,ncol=T+1)	# V[i,j] is stage i at time j-1
V[1,1] <- 0
V[2,1] <- 0
V[3,1] <- 1
M <- matrix(0,nrow=3,ncol=3)
M[1,1] <- s
M[2,1] <- p
M[3,2] <- 1
M[3,3] <- a
M[1,3] <- f
U <- matrix(0,nrow=3,ncol=T+1)	# U[i,j] is proportion of i at t=j-1

##
## FUNCTIONS
##
## Define any functions that the main program requires.
## Calculations that need to repeated at different points of a program should be
##   coded as functions.
##

##
## MAIN PROGRAM
##
## Perform the computations, using functions as needed.
##

for (t in 1:T){	# new time value
	n <- t	# column of the old population values
	k <- t+1	# column of the new population values
	V[,k] <- M %*% V[,n]  # calculate new population values
	}
N <- colSums(V)		# total population at times 0, 1, etc
R <- N[2:(T+1)]/N[1:T]	# N1/N0, N2/N1, etc
for (j in 1:(T+1)) U[,j] <- V[,j]/N[j]

result <- eigen(M)
lambda1 <- Re(result$values[1])
ratios <- Re(result$vectors[,1]/result$vectors[3,1])

##
## OUTPUT
##
## Create any needed graphs.
## Display key results.
##

par(mfrow=c(1,2))

# plot 1

plot(1:T, R[1:T], pch=15, xlim=(c(0,T)), ylim=(c(0,max(R))), xlab="time", ylab="growth rate: N(t)/N(t-1)")
abline(h=lambda1, lty=3)

# plot 2

plot(0:T, U[1,], pch=16, col="green3", ylim=(c(0,1)), xlab="time", ylab="proportions")
points(0:T, U[2,], pch=17, col="purple3")
points(0:T, U[3,], pch=18, col="red3")
abline(h=ratios[1]/sum(ratios), lty=3, col="green3")
abline(h=ratios[2]/sum(ratios), lty=3, col="purple3")
abline(h=ratios[3]/sum(ratios), lty=3, col="red3")
legend(0.77*T,1,legend=c("Larvae","Pupae","Adults"),pch=c(15,16,17),col=c("green3","purple3","red3"))
#	[* The legend location may need to be adjusted. *]

lambda1
ratios

