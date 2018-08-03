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

# This program determines the parameters for the linear stage-structured aphid population model

# development.csv is a file that contains the development and survival data.
#	The first row contains column headers.
#	The first column contains the ID numbers for the aphids. 
#	The second column contains the stage number for the aphid on the first day of the experiment.
#		The second column should contain all 1s.
#	Subsequent columns contain the stage numbers for the aphid on the corresponding day.
#	"Number of stages + 1" is used to indicate natural death.
#	"Number of stages + 2" is used to indicate accidental death.
#	"0" is used to indicate that the aphid is not born yet.


##
## DATA
##
## Import any data from files.
## Give values to any fixed parameters.
##

# define the number of stages
stages <- 6

# read the development file and remove ID numbers
devel <- read.csv("development.csv",header=TRUE)
devel <- devel[,-1]


##
## INITIALIZATION
##
## Set up any running variables that need to have a starting value.
## Create any needed data structures.
##

# determine the number of rows in the data file
rows <- length(devel[,1])

# define the data structures for the transitions and parameters
transitions <- matrix(0,nrow=stages+1,ncol=stages)
s <- array(0,dim=stages)
p <- array(0,dim=stages-1)


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

# count the transitions
for (row in 1:rows)
	{
	lastcol <- max(which(devel[row,]<stages+2))
	for (col in 2:lastcol)
		{
		i <- devel[row,col]			# new stage
		j <- devel[row,col-1]			# old stage
		if (j > 0)
			transitions[i,j] <- transitions[i,j]+1
		}
	}

# compute the parameters
for (j in 1:stages)
	{
	total <- sum(transitions[,j])
	s[j] <- transitions[j,j]/total
	if (j < stages)
		p[j] <- transitions[j+1,j]/total
	if (j == 4)
		a <- transitions[6,4]/total
	}


##
## OUTPUT
##
## Create any needed graphs.
## Display key results.
##

p
s
a



