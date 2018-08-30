import csv
from tqdm import tqdm

classes_coded = []
classes_names = []

for l in csv.reader(open('class-descriptions-boxable.csv')):
    # print(l)
    classes_coded.append(l[0])
    classes_names.append(l[1])
    # break

print(len(classes_names))

# 601 classes, not 600...

input_file = csv.DictReader(open("train-annotations-bbox.csv"))

for line in tqdm(list(input_file)):
    # print(line)
    # print(line['LabelName'],classes_coded.index(line['LabelName']))
    with open('train/%s.txt'%line['ImageID'],'w') as f:
        f.write(','.join([str(classes_coded.index(line['LabelName'])),line['XMin'],line['YMin'],str(float(line['XMax'])-float(line['XMin'])),str(float(line['XMax'])-float(line['YMin']))])+'\n')
    # break

input_file = csv.DictReader(open("validation-annotations-bbox.csv"))

for line in tqdm(list(input_file)):
    # print(line)
    # print(line['LabelName'],classes_coded.index(line['LabelName']))
    with open('val/%s.txt'%line['ImageID'],'w') as f:
        f.write(','.join([str(classes_coded.index(line['LabelName'])),line['XMin'],line['YMin'],str(float(line['XMax'])-float(line['XMin'])),str(float(line['XMax'])-float(line['YMin']))])+'\n')
    # break
