function B = AddRow(A,c,i,j)
%
% This function adds j-th row times c to the i-th row
B = A;
B(i,:)=A(i,:)+c*A(j,:);