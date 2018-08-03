function [beta,x]=FindBasicFeasibleSolution(A,b)
b =b(:);
[m,n] = size(A);
Combos = nchoosek(1:n , m);
y=0;
for i = 1: size(Combos, 1);
    beta = Combos(i,:);
    Abeta = A(:,beta);
    if rank(Abeta) == m;
    y=1;
    break
    end
end
if y == 1;
x = Abeta\b;
if x >= 0;
else x = NaN;
end    
else 
	x = NaN;   
end
	