function [IsBasicFeasibleSolution,x,Abeta_inv]=BasicFeasibleSolutionFromBeta(A,b,beta);
% This function takes a polyhedron in standard form P={x| Ax=b, x>=0} and
% checks if the indices beta=[beta_1,... ,beta_m] yields linearly independent
% columns and then computes a basic feasible solution x if exists
% Usage: [IsBasicFeasibleSolution,x,Abeta_inv]=BasicFeasibleSolutionFromBeta(A,b,beta);
b=b(:); beta=beta(:);
[m,n]=size(A); 
if length(b)~=m;error('The sizes of A and b do not match');end
if n<=m; error('The matrix A does not define a polyhedron in standard form'); end;
if rank(A)<m; error('The matrix is not full rank --> quitting'); end
if length(beta)~=m; error('must specify an index set beta of length m');end

A_beta=A(:,beta);
rk=rank(A_beta);
if rk<m; 
    IsBasicFeasibleSolution=false; 
else
    x_beta=A_beta\b;
    non_negative=(sum((x_beta)<0)==0);
     if ~non_negative
        IsBasicFeasibleSolution=false;
     else
         IsBasicFeasibleSolution=true;
     end
end

if (nargout>1) && (rk==m)
    x=zeros(n,1);
    x(beta)=x_beta;
else
    x=[];
end


if (nargout>2) && (IsBasicFeasibleSolution)
    Abeta_inv=inv(A_beta);
else
    Abeta_inv=[];
end