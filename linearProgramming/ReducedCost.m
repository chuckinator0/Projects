function c_bar=ReducedCost(A,b,c,beta)
% Usage c_bar=ReducedCost(A,b,c,beta);
c=c(:);[m,n]=size(A); 
if n~=length(c); error('The sizes of A and c do not match'); end
[IsBasicFeasibleSolution,x,Abeta_inv]=BasicFeasibleSolutionFromBeta(A,b,beta);
c_bar=zeros(size(c));
not_beta=setdiff(1:n,beta);
c_beta=c(beta);
for j=not_beta;
    c_bar(j)=c(j)-c_beta'*Abeta_inv*A(:,j);
end