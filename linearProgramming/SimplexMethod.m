function [Status, x, OptimalCost] = SimplexMethod(A,b,c)

[m,n] = size(A);
[beta,y]=FindBasicFeasibleSolution(A,b);
if isnan(y); Status = 3; x = []; OptimalCost = []; fprintf('the polyhedron was empty.')  % All nonempty polyhedrons in standard form have at least one basic feasible solution.
else
    Tableau = MakeTableau(A,b,c,beta);
   
    [Stat1, NewTableau, Newbeta] = SimplexMethodIteration(Tableau,beta);
    while Stat1 == 0;
        Tableau = NewTableau;
        beta = Newbeta;
        [Stat1, NewTableau, Newbeta] = SimplexMethodIteration(Tableau,beta);
    end
    if Stat1 == 2; Status = 2; x = Inf; OptimalCost = -Inf;
    elseif Stat1 == 1; Status = 1;
        x_beta = NewTableau(2:m+1,1);
        x = zeros(n,1);
        x(Newbeta) = x_beta;
        OptimalCost = -NewTableau(1,1);
    end
end