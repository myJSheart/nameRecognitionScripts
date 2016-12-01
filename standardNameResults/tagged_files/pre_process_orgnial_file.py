import json
import requests
import re
import struct
from pprint import pprint

# read all files' name from given directory
import glob
all_files = glob.glob('/Users/chenxuzhao/Desktop/nameRecognitionProject/standardNameResults/*.html')

# process every file
for single_file in all_files:
    # read file to a json object(orginal_file)
    with open(single_file) as single_file_stream:
        orginal_json = json.load(single_file_stream)

    # if the page is not a directory, skip it
    if orginal_json['is-directory-page'] == 'F':
        print(orginal_json['base-url'])
        continue
    # get the outlinks area
    orginal_json_outlinks = orginal_json['outlinks']

    for single_link in orginal_json_outlinks:
        if single_link['is-target'] == 'F':
            continue
        anchor_name_score = re.split(r'\t+', single_link['anchor_name_score'])
        # check whether an anchor is a name
        is_name = False
        for anchor_seg_score in anchor_name_score:
            try:
                float(anchor_seg_score)
            except:
                anchor_seg_score = '0'
            if float(anchor_seg_score) > 0.6:
                is_name = True
                break
        single_link['true_name_title'] = single_link['anchor_text']
        single_link['true_name'] = single_link['anchor_text']

    # write results into a json file
    file_name = single_file.split('.')[0]
    with open(file_name + '.json', 'w') as out_file:
        json.dump(orginal_json, out_file)
    # # read the outlinks area
    # orginal_outlinks = orginal_data["outlinks"]
    #
    # for link in orginal_outlinks:
    #     anchor_text_name = link['anchor_text'].split('_SS_URLSIM_ANCHOR_DELIMITER_TAG_')[0]
    #     prefix_url = 'http://10.100.230.224:8084/NameRecServer/nameString?name='
    #     score_name_rec = requests.get(prefix_url + anchor_text_name).content
    #     score_each_seg = re.split(b'\t+', score_name_rec)
    #     is_name = False
    #     for score in score_each_seg:
    #         if not score:
    #             score = '0'
    #         if float(score) > 0.60:
    #             is_name = True
    #         else:
    #             is_name = False
    #             break
    #
    #     if is_name is True:
    #         link['true_name'] = anchor_text_name
    #
    # orginal_data['outlinks'] = orginal_outlinks
    #
    # with open('target_preprocess_file_2.json', 'w') as target_preprocess_file:
    #     json.dump(orginal_outlinks, target_preprocess_file)
