function Tableau = MakeTableau(A,b,c,beta)
% This program takes an LP problem in Standard Form (min c dot x subject to Ax=b) with mxn matrix A, nx1 cost vector c, mx1 constraint vector b, and 1xm set of indicies beta,and creates a Tableau with which one can perform Full Tableau Implementation.
b = b(:);
c =c(:);

[m,n]=size(A);
c_beta = c(beta);
A_beta = A(:,beta);
if rank(A_beta) < m ; error('The set of indicies, beta, does not produce a basic feasible solution'); end
x_beta=A_beta\b;
non_negative=(sum((x_beta)<0)==0);
if ~non_negative; error('The set of indicies, beta, does not produce a basic feasible solution');end
Tableau = zeros(m+1,n+1); % Tableau is an m+1xn+1 matrix
Tableau(1,1) = dot(-1*c_beta,inv(A_beta)*b);
Tableau(1,2:n+1) = c' - c_beta'*inv(A_beta)*A;
Tableau(2:m+1,1) = inv(A_beta)*b;
Tableau(2:m+1,2:n+1) = inv(A_beta)*A;