!pip install matplotlib matplotlib_venn
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

A = {'a','b','c','k','m','n','p','q','r','v','w','x'}
B = {'d','e','f','k','m','n','s','t','u','v','w','x'}
C = {'g','h','j','p','q','r','s','t','u','v','w','x'}

venn = venn3([A, B, C], ('A', 'B', 'C'))
venn3_circles([A, B, C])

# Implementations
# Methods to organize data points
data = [
    [2000, 5, 1, 2804500],
    [2000, 4, 1, 2803600],
    [2000, 3, 1, 2802700],
    [2000, 2, 1, 2801800],
    [2000, 1, 1, 2800900],
    [3000, 5, 1, 3704500],
    [3000, 4, 1, 3703600],
    [3000, 3, 1, 3702700],
    [3000, 2, 1, 3701800],
    [3000, 1, 1, 3700900],
    [4000, 5, 1, 4604500],
    [4000, 4, 1, 4603600],
    [4000, 3, 1, 4602700],
    [4000, 2, 1, 4601800],
    [4000, 1, 1, 4600900],
    [2000, 5, 0, 1804500],
    [2000, 4, 0, 1803600],
    [2000, 3, 0, 1802700],
    [2000, 2, 0, 1801800],
    [2000, 1, 0, 1800900],
    [3000, 5, 0, 2704500],
    [3000, 4, 0, 2703600],
    [3000, 3, 0, 2702700],
    [3000, 2, 0, 2701800],
    [3000, 1, 0, 2700900],
    [4000, 5, 0, 3604500],
    [4000, 4, 0, 3603600],
    [4000, 3, 0, 3602700],
    [4000, 2, 0, 3601800],
    [4000, 1, 0, 3600900],
    [1000, 5, 1, 1904500],
    [1000, 4, 1, 1903600],
    [1000, 3, 1, 1902700],
    [1000, 2, 1, 1901800],
    [1000, 1, 1, 1900900],
    [1000, 5, 0, 904500],
    [1000, 4, 0, 903600],
    [1000, 3, 0, 902700],
    [1000, 2, 0, 901800],
    [1000, 1, 0, 900900]
]

# Convert data into binary categories and calculate averages
def avg(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)

def filter_binary(dataPoints):
    organized_data = {
        "000": [],
        '100': [],
        "010": [],
        "001": [],
        "110": [],
        "101": [],
        "011": [],
        "111": []
    }

    for data in dataPoints:
        sqft = "1" if data[0] > 2000 else "0"
        rooms = "1" if data[1] > 2 else "0"
        parking = "1" if data[2] == 1 else "0"

        data_string = sqft + rooms + parking
        organized_data[data_string].append(data[3])

    for key, values in organized_data.items():
        organized_data[key] = avg(values)

    return organized_data

#compute
mappedCosts = filter_binary(data)

# venn diagram
venn.get_label_by_id('100').set_text(f'{mappedCosts["100"]:.2f}')  # Only in A
venn.get_label_by_id('010').set_text(f'{mappedCosts["010"]:.2f}')  # Only in B
venn.get_label_by_id('001').set_text(f'{mappedCosts["001"]:.2f}')  # Only in C
venn.get_label_by_id('110').set_text(f'{mappedCosts["110"]:.2f}')  # A & B, not C
venn.get_label_by_id('101').set_text(f'{mappedCosts["101"]:.2f}')  # A & C, not B
venn.get_label_by_id('011').set_text(f'{mappedCosts["011"]:.2f}')  # B & C, not A
venn.get_label_by_id('111').set_text(f'{mappedCosts["111"]:.2f}')  # A & B & C

plt.show()
