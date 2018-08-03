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

# This program uses nonlinear and linear optimization to compute the parameters
#    in the Holling type 2 function "R(x)=qx/(a+x)" and the linear function "R(x)=sx".
# The function "RSSa(a)" uses linear regression to fit "R=qZ", where "Z=x/(a+x)", 
#   with output consisting of the residual sum of squares for the best "q".
# The built-in "optimize" function is used to find the value of "a" that 
#   minimizes "RSSa".
# The data for "x" and "R" can be imported from a file or entered directly.
# The output consists of 
#    the best "a" and "q" for the Holling 2 model and the best "s" for the linear model;
#    the average residual sums of squares for both models;
#    the AIC values for both models; 
#    a plot of the data; 
#    the best fit curve for Holling type 2; and
#    the best fit straight line (optional).

##
## DATA
##
## Import any data from files.
## Give values to any fixed parameters.
##

# Set the maximum "x" value for the graph.
maxx <- 300

# Speedius data
#.x <- c(0,5,7,9,11,13,16,20,22,24,27,31,35,37,42,48,55,61,67,78,85,101,114,120,129,137,142,145,148)
#.R <- c(0,3,0,1,2,4,6,5,2,7,8,8,7,7,9,19,14,16,17,18,26,26,27,28,35,34,33,32,29)

# Steadius data
x <- c(0,4,7,13,15,18,21,25,29,34,38,43,47,51,58,63,69,75,80,88,96,107,116,125,130,134,138,141,145,148)
R <- c(0,3,3,7,8,9,8,13,9,11,10,17,18,17,19,19,22,21,24,21,20,27,26,29,27,29,26,29,30,28)

# Set "plotline" to "TRUE" or "FALSE" to show or suppress the linear fit on the graph.
plotline <- TRUE

##
## INITIALIZATION
##
## Set up any running variables that need to have a starting value.
## Create any needed data structures.
##

# This program requires no initialization.

##
## FUNCTIONS
##
## Define any functions that the main program requires.
## Calculations that need to repeated at different points of a program should be
##   coded as functions.
##

# The function "RSSa" is needed to compute the residual sum of squares for any value of "a"
#   tested by the "optimize" function.
# The lists of "x" and "R" values comes from the main program.
# The function "RSSa" is based on the model form "R=qZ" that applies when the value of "a" is known.

RSSa <- function(a) 
      {
	Z <- x/(a+x)
	sumZ2 <- sum(Z^2)
	sumZR <- sum(Z*R)
	sumR2 <- sum(R^2)
	q <- sumZR/sumZ2
	result <- sumR2-q*sumZR
	return(result)
	}

##
## MAIN PROGRAM
##
## Perform the computations, using functions as needed.
##

# "optimize" is a built-in R function.
# The following line finds the minimum value of the function "RSSa",
#   with the values of the input variable confined to the interval [0,150].
# The function "RSSa" must be user-defined above.

result <- optimize(f=RSSa, lower=0, upper=maxx, maximum=FALSE)

# Save the optimizing value of the input variable as "a". 

a <- result$minimum

# Find the optimal "q", "RSS", and average of "RSS", given the correct "a".

Z <- x/(a+x)
sumZ2 <- sum(Z^2)
sumZR <- sum(Z*R)
sumR2 <- sum(R^2)
q <- sumZR/sumZ2
RSS <- sumR2-q*sumZR
avgRSS <- RSS/length(x)
AIC <- log(avgRSS)+4/length(x)

# Find the optimal "m", "RSS", average of "RSS", and AIC for the linear model.

sumx2 <- sum(x^2)
sumxR <- sum(x*R)
m <- sumxR/sumx2
RSSline <- sumR2-m*sumxR
avgRSSline <- RSSline/length(x)
AICline <- log(avgRSSline)+2/length(x)

##
## OUTPUT
##
## Create any needed graphs.
## Display key results.
##

# Calculate data points for the model using a set of "x" values and the calculated parameters.

xmodel <- 0:maxx
Rmodel <- q*xmodel/(a+xmodel)

# Plot "R" vs "x" as a curve, using appropriate settings and labels.
# The settings can be changed to improve the graph appearance.

plot(xmodel,Rmodel, type="l", ylim=c(0,q+3), xlab="prey density (x)", ylab="consumption (R)", xaxs="i", yaxs="i")

# Add the data points to the plot.

points(x,R)

# Add the asymptote to the plot.

abline(h=q, lty=3)

# Add the linear model to the plot.

if (plotline) 
	abline(0,m, lty=2)

# Display the calculated values for "m", "a", "q", average "RSS", and "AIC".

m
a
q
c(avgRSS,avgRSSline)
c(AIC,AICline)


