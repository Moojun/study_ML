import glob, csv
import matplotlib.pyplot as plt

def read_data(filename):
    files = glob.glob(filename)
    all_data = []
    for file in files:
        with open(file, 'r') as f:          # Construct a file object
            csv_reader = csv.reader(f)      # Construct a CSV reader object
            data = []
            for line in csv_reader:
                if line and not line[0].strip().startswith('#'):  # If 'line' is valid and not a header
                    data.append([int(val) for val in line])         # Append 'line' to 'data' as numbers
            all_data = all_data + data                              # Merge 'data' to 'all_data'
    return all_data


if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # Derive midterm, final, and total scores
    midterm_kr = [ x[0] for x in class_kr ]
    final_kr = [ x[1] for x in class_kr ]
    total_kr = [ row[0] * 40/125 + row[1] * 60/100 for row in class_kr ]
    midterm_en = [ y[0] for y in class_en ]
    final_en = [ y[1] for y in class_en ]
    total_en = [ row[0] * 40/125 + row[1] * 60/100 for row in class_en ]

    # Plot midterm/final scores as points
    plt.title('Score distribution between midterm and final exam\n of both Korean and English classes')     # Add title
    plt.plot(midterm_kr, final_kr, 'r.', label='Korean')
    plt.plot(midterm_en, final_en, 'b+', label='English')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')

    # add x and y range
    plt.xlim([0, 125])
    plt.ylim([0, 100])


    plt.legend()
    plt.grid()
    #plt.show()

    # Plot total scores as a histogram
    plt.figure()        # figure() 사용 후 맨 마지막에만 show() 함수를 사용하면 여러 창이 동시에 띄어짐.

    plt.title('Score distribution of total score both Korean and English classes')  # Add title
    plt.hist(total_kr, range=(0, 100), bins = 20, color='r', label = 'Korean')
    plt.hist(total_en, range=(0, 100), bins = 20, color='b', alpha = 0.5, label = 'English')
    plt.xlabel('Total scores')
    plt.ylabel('The number of students')
    plt.legend(loc='upper left')
    plt.xlim([0, 100])

    plt.show()
