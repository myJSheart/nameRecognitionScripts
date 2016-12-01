import json
file_name = 'f922c9dc-de0f-4de8-945e-b58ffd95ed20.json'
with open(file_name) as orginal_file:
    orginal_json = json.load(orginal_file)

anchor_text_all = orginal_json['outlinks']
for anchor_text in anchor_text_all:
    if anchor_text['is-target'] == 'T':
        try:
            anchor_text['true_name'] = anchor_text['anchor_text'].split('_SS_URLSIM_ANCHOR_DELIMITER_TAG_')[1].strip()
        except:
            anchor_text['true_name'] = anchor_text['anchor_text'].split('_SS_URLSIM_ANCHOR_DELIMITER_TAG_')[0].strip()    
        anchor_text['true_name_title'] = anchor_text['true_name']
        # anchor_text['true_name_title'] = anchor_text['true_name_title'].split(
        #     '_SS_URLSIM_ANCHOR_DELIMITER_TAG_')[0].strip()
        # anchor_text['true_name'] = anchor_text['true_name_title'].replace('PhD', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('Ph.D.', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('FCP', '')
        # anchor_text['true_name'] = anchor_text['true_name'].rstrip(', ')

    with open(file_name + '.json', 'w') as out_file:
        json.dump(orginal_json, out_file)

        # remove title
        # anchor_text['true_name'] = anchor_text['true_name'].replace('Dr ', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('Professor ', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('Assoc Professor ', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('Mr ', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('Ms ', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('Dr. ', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('Prof. ', '')
        # remove the title at the end
        # anchor_text['true_name'] = anchor_text['anchor_text'].split(',')[0]
        # anchor_text['true_name'] = anchor_text['true_name'].replace('_SS_URLSIM_ANCHOR_DELIMITER_TAG_', '')
        # remove the title at the beginning
        # name_array = anchor_text['anchor_text'].split()
        # name_string = ''
        # for i in range(1, name_array.__len__()):
        #     name_string = name_string + name_array[i] + ' '
        # name_string = name_string.rstrip()
        # anchor_text['true_name'] = name_string
        # split name by tags
        # anchor_text['true_name_title'] = anchor_text['anchor_text'].split(' photo_SS_URLSIM_ANCHOR_DELIMITER_TAG_')[1]
        # anchor_text['true_name'] = anchor_text['true_name_title'].split(',')[0]
        # remove words
        # anchor_text['true_name'] = anchor_text['anchor_text'].replace('\n    ', ' ')
        # anchor_text['true_name_title'] = anchor_text['anchor_text'].replace('\n    ', ' ')
        # split by ','
        # anchor_text['true_name'] = anchor_text['true_name_title'].split(',')[0]

        # anchor_text['true_name'] = anchor_text['true_name_title'].replace('MSc', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('dr.', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('PhD', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('DDS.', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('prof.', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('drs', '')
        # anchor_text['true_name'] = anchor_text['true_name'].replace('M.A.', '')
