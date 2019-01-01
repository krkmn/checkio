data = {1, 2, 3, 4, 5, 7, 8, 12}
sorted_data = sorted(data)

begin_i = [sorted_data[0]]
end_i = []

for i in range(len(sorted_data)-1):
    if (sorted_data[i+1]-sorted_data[i] > 1):
        begin_i.append(sorted_data[i+1])
        end_i.append(sorted_data[i])

end_i.append(sorted_data[-1])

return_list = list(zip(begin_i, end_i))
