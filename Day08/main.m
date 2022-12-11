clear; close all; clc;
%% take data
fileID = fopen('input_data.txt','r');
formatSpec = '%s';
data = fscanf(fileID,formatSpec);

%% convert data
dim = length(data)^.5;
trees = zeros(dim,dim);
jj = 1;
for row = 1:dim
    for col = 1:dim
        trees(row,col) = data(jj)-'0';
        jj = jj + 1;
    end
end

%% algorithms
view = 1;
trees_seeable = dim*4-4;
for row = 2:dim-1
    for col = 2:dim-1
        % --- part 1 ---
        flag = true;
        % top
        if all(trees(row,col) > trees(1:row-1,col)) && flag
            trees_seeable = trees_seeable + 1;
            flag = false;
        end
        % bottom
        if all(trees(row,col) > trees(row+1:end,col)) && flag
            trees_seeable = trees_seeable + 1;
            flag = false;
        end
        % left
        if all(trees(row,col) > trees(row,1:col-1)) && flag
            trees_seeable = trees_seeable + 1;
            flag = false;
        end
        % right
        if all(trees(row,col) > trees(row,col+1:end)) && flag
            trees_seeable = trees_seeable + 1;
            flag = false;
        end
        
        % --- part 2 ---
        this_view = 1;
        % search going down
        flag = false;
        kk = row+1;
        partial_view = 0;
        while kk <= dim && not(flag)
            partial_view = partial_view + 1;
            if trees(row,col) <= trees(kk,col)
                flag = true;
            end
            kk = kk +1;
        end
        this_view = this_view * partial_view;
        % search going up
        flag = false;
        kk = row-1;
        partial_view = 0;
        while kk >= 1 && not(flag)
            partial_view = partial_view + 1;
            if trees(row,col) <= trees(kk,col)
                flag = true;
            end
            kk = kk -1;
        end
        this_view = this_view * partial_view;
        % search going right
        flag = false;
        kk = col+1;
        partial_view = 0;
        while kk <= dim && not(flag)
            partial_view = partial_view + 1;
            if trees(row,col) <= trees(row,kk)
                flag = true;
            end
            kk = kk +1;
        end
        this_view = this_view * partial_view;
        % search going left
        flag = false;
        kk = col-1;
        partial_view = 0;
        while kk >= 1 && not(flag)
            partial_view = partial_view + 1;
            if trees(row,col) <= trees(row,kk)
                flag = true;
            end
            kk = kk -1;
        end
        this_view = this_view * partial_view;
        
        if this_view > view
            view = this_view;
        end
    end
end
fprintf(['part 1: ' num2str(trees_seeable) '\n'])
fprintf(['part 2: ' num2str(view) '\n'])