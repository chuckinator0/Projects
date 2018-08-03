function B=EliminateColumnElements(A,pivotrow,pivotcolumn)
% Usage: B=EliminateColumnElements(A,pivotrow,pivotcolumn);
% This function performs row operations to eliminate the elements in the
% pivot column using the specified pivot row


B=A; % here we copy the contents of A into B 
[m,n]=size(A); % this computes the number of rows and the number of columns of the matrix A
if A(pivotrow,pivotcolumn)==0; error(' the pivot element must be non-zero');end 

for i=1:m
    if i~=pivotrow;
        c=-B(i,pivotcolumn)/B(pivotrow,pivotcolumn);
        B=AddRow(B,c,i,pivotrow);
    end
end;