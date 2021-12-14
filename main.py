import pandas as pd


def convert_to_csv(filename):
    headers = []
    column_names = open('ranges.txt', 'r')
    lines = column_names.readlines()
    for line in lines:
        header = line.split(':')
        headers.append(header[0])
    headers.append('extra')
    dataframe = pd.read_csv('test.txt', delimiter=' ')
    dataframe.columns = headers
    dataframe = dataframe.drop(labels='extra', axis=1)
    dataframe.to_csv('test.csv', index=None)


def read_files(actual, predictions):
    actual_file = open(actual, "r")
    prediction_file = open(predictions, 'r')
    lines_actual = actual_file.readlines()
    lines_predicted = prediction_file.readlines()
    actual_values = []
    predicted_values = []
    for line in lines_actual:
        values = line.split(" ")
        values.pop()
        actual_values.append(values.pop())
    for line in lines_predicted:
        values = line.split('\n')
        values.pop()
        predicted_values.append(values.pop())
    return actual_values, predicted_values


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_to_csv('test.txt')
    actual, predicted = read_files('actual.txt', 'predictions.txt')
    count = 0
    if len(actual) != len(predicted):
        print('length not equals')
        exit(0)

    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            count += 1
    accuracy = (count / len(actual)) * 100
    print(accuracy)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
