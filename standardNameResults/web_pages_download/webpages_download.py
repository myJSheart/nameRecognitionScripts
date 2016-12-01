import os
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import glob
all_json_files = glob.glob('/Users/chenxuzhao/Desktop/nameRecognitionProject/standardNameResults/web_pages_download/json/*.json')

destination_file_path_prefix = '/Users/chenxuzhao/Desktop/nameRecognitionProject/standardNameResults/web_pages_download/targets/'

for orgnial_json_file_name in all_json_files:
    with open(orgnial_json_file_name) as orginal_json_file:
        orginal_json = json.load(orginal_json_file)

    if orginal_json['is-directory-page'] == 'F':
        continue

    file_name_with_extension = os.path.basename(orgnial_json_file_name)
    file_name_without_extension = os.path.splitext(file_name_with_extension)[0]
    new_dir = destination_file_path_prefix + file_name_without_extension

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # download 'base-url' web pages
    try:
        base_url = orginal_json['base-url']
        print('Directory Page:' + base_url)
        response = urllib2.urlopen(base_url)
        webContent = response.read()
        f = open(new_dir + "/" + 'directory.html', 'wb')
        f.write(webContent)
        f.close
    except:
        orginal_json['cannot_download'] = 'F'
        print('Directory Page' + orginal_json['base-url'] + 'cannot be downloaded')

    orginal_json_outlinks_area = orginal_json['outlinks']
    for link_area in orginal_json_outlinks_area:
        if link_area['is-target'] == 'F':
            continue

        # download web pages
        try:
            outlink_url = link_area['outlink-url']
            print('Download: ' + outlink_url)
            response = urllib2.urlopen(outlink_url)
            webContent = response.read()
            import uuid
            filename = str(uuid.uuid4())
            f = open(new_dir + '/' + filename + '.html', 'wb')
            f.write(webContent)
            f.close
            link_area['html_file'] = filename + '.html'
        except:
            print('cannot download:' + link_area['outlink-url'])

    with open(new_dir + '/mapping.json', 'w') as out_file:
        json.dump(orginal_json, out_file)

print('All Down')
