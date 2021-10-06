def read_data(filename):
    data1 = []       # revise name 'data' to 'data1' because of the variable name overlap
    with open(filename, 'r') as file:
        for line in file:
            values = []
            if line.startswith('#'):
                continue
            for word in line.split(','):
                values.append(int(word))
            data1.append(values)
    return data1


def add_weighted_average(data2, weight):    # revise name 'data' to 'data2' because of the variable name overlap
    for row in data2:
        avg = int(row[0]) * weight[0] + int(row[1]) * weight[1]
        row.append(avg)

def analyze_data(data3):             # revise name 'data' to 'data3' because of the variable name overlap
    mean = sum(data3) / len(data3)
    var = sum([ x ** 2 for x in data3]) / len(data3) - mean ** 2
    data3_sorted = sorted(data3)
    mid_num = len(data3) // 2
    median = data3_sorted[mid_num]
    return mean, var, median, min(data3), max(data3)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2:
        print('### Individual Score')
        add_weighted_average(data, [40/125, 60/100])
        if len(data[0]) == 3:
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
        print()

        print('### Exam Score Analysis')
        col_n = len(data[0])
        col_name = ['Midterm', 'Final', 'Total']
        colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
        for c, score in enumerate(colwise_data):
            mean, var, median, min_, max_ = analyze_data(score)
            print(f'* {col_name[c]}')
            print(f'  * Mean: **{mean:.3f}**')
            print(f'  * Variance: {var:.3f}')
            print(f'  * Median: **{median:.3f}**')
            print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')
