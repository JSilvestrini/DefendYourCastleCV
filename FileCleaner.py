import os

def rename():
    for filename in os.listdir('positive'):
        full_path = os.path.join('positive', filename)
        new_filename = filename.replace(' ', '')
        new_full_path = os.path.join('positive', new_filename)
        os.rename(full_path, new_full_path)

def generate_negative_file():
    with open('neg.txt', 'w') as f:
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')

if __name__ == '__main__':
    rename()
    generate_negative_file()