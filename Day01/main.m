clc; clear; close all;
%% take data
lines = readlines('input_data.txt');

%% convert data
most_calories = [0 0 0];
current_calories = 0;
for line = 1:length(lines)
    if lines(line) ~= ""
        current_calories = current_calories + str2double(lines(line));
    else
        if any(current_calories > most_calories)
            most_calories(4) = current_calories;
            most_calories = sort(most_calories,'descend');
            most_calories = most_calories(1:end-1);
        end
        current_calories = 0;
    end
end
fprintf(['Point 1: ' int2str(most_calories(1)) '\n'])
fprintf(['Point 2: ' int2str(sum(most_calories)) '\n'])