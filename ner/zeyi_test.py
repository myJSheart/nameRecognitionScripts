# If one name score is larget than 0.6501, I think this string contains a name
import os
import requests
import json
import glob
all_json_files = glob.glob(
    '/Users/chenxuzhao/Desktop/nameRecognitionProject/private/tagged_files/json/*.json')

results_json_file_prefiex = '/Users/chenxuzhao/Desktop/nameRecognitionProject/ner/zeyi_results/'

ZEYI_SERVER_PREFIX = 'http://10.100.230.224:8084/NameRecServer/nameString?name='

THRESHOLD = 0.6501

target_num = 0
anchor_text_num = 0
true_name_title_num = 0
true_name_num = 0

for json_file_name in all_json_files:
    with open(json_file_name) as init_json_file:
        init_json = json.load(init_json_file)

    if init_json['is-directory-page'] == 'F':
        continue

    outlinks_area = init_json['outlinks']

    for link_area in outlinks_area:
        if link_area['is-target'] == 'T':
            target_num += 1
            anchor_name_score = link_area['anchor_name_score']
            # Calculate whether an anchor_name_score has a name
            anchor_name_score_array = anchor_name_score.strip().split('\t')
            if anchor_name_score_array.__len__() != 0:
                for anchor_score in anchor_name_score_array:
                    if anchor_score is None or anchor_score == '':
                        continue
                    if float(anchor_score) >= THRESHOLD:
                        anchor_text_num += 1
                        break
            link_area['anchor_name_score'] = anchor_name_score_array
            # Calculate whether a true_name_title has a name
            true_name_title_score = requests.get(ZEYI_SERVER_PREFIX + link_area['true_name_title'])
            true_name_title_score_array = true_name_title_score.content.decode('utf-8').strip().split('\t')
            if true_name_title_score_array.__len__() != 0:
                for title_score in true_name_title_score_array:
                    if title_score is None or title_score == '':
                        continue
                    if float(title_score) >= THRESHOLD:
                        true_name_title_num += 1
                        break
            link_area['true_name_title_score'] = true_name_title_score_array
            # Calculate whether a true_name has a name
            true_name_score = requests.get(ZEYI_SERVER_PREFIX + link_area['true_name'])
            true_name_score_array = true_name_score.content.decode('utf-8').strip().split('\t')
            if true_name_score_array.__len__() != 0:
                for name_score in true_name_score_array:
                    if name_score is None or name_score == '':
                        continue
                    if float(name_score) >= THRESHOLD:
                        true_name_num += 1
                        break

            link_area['true_name_score'] = true_name_score_array

    # result_name = json_file_name.split('/')[json_file_name.split('/').__len__() - 1]
    # with open(results_json_file_prefiex + result_name, 'w') as out_file:
    #     json.dump(init_json, out_file)

print('target_num --- ' + str(target_num) + '\n' + 'anchor_text_num --- ' + str(anchor_text_num))
print('true_name_title_num --- ' + str(true_name_title_num) + '\n' + 'true_name_num --- ' + str(true_name_num))
