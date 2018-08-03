function [Status, NewTableau, Newbeta] = SimplexMethodIteration(Tableau,beta)
% This function is supposed to perform one iteration of the simplex method. Here, Tableau is the full tableau of the original LP problem in the standard form (in particular, it has m + 1 rows and n + 1 columns) and beta is the m-dimensional vector of basic indices.
[m,n] = size(Tableau);
m = m-1;
n = n-1;


c_bar = Tableau(1,2:n+1);
if sum((c_bar >= 0))==n; Status = 1; NewTableau = Tableau; Newbeta = beta; % STOP! we've found the optimal sltn
else
    for j = 1:n;                %pick minimum j s.t. c_bar(j) < 0
        if c_bar(j) < 0;
            j_star = j;
            break
        end
    end
    u = Tableau(2:m+1,j_star+1);    % j is the correct entry of c_bar, but the Tableau has an extra column in front of c_bar in the first row, so we need j_star+1 .
    if u <= 0; Status = 2; Newbeta = beta; NewTableau = Tableau;
        % STOP! optimal cost is -infinity.
    else
        Status = 0;
        xu = Tableau(2:m+1,1)./u;
        xu_star = xu(xu > 0);
        k = min(xu_star);
        v = find(xu == k);
        l = v(1);                         % Pick smallest l=argmin x_betai/ui
        NewTableau = EliminateColumnElements(Tableau,l+1,j_star+1);
        NewTableau(l+1,:) = NewTableau(l+1,:)/NewTableau(l+1,j_star+1);
        Newbeta = beta;
        Newbeta(l) = j_star;                % beta(l) leaves the basis, j enters the basis
    end
end






