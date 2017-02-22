import requests
from bs4 import BeautifulSoup


class DownLoadWebsite:
    def download_file(self, url, file_name):
        """ Download a file to a given directory

        Args:
            url: (string) file's url
            file_name: (string) destination saved file's name (including path)
            'chenxu/mp3/good.mp3'

        Returns:
            Saved information if success
            Error information if some errors occur
        """
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(response.content)
                return 'Saved' + url + 'in' + file_name
        else:
            return 'Error occurs when downloading ' + url + '\
             with an error code' + response.status_code

    def download_html(self, url, file_name):
        """ Download a html file

        Args:
            url: (string) file's url
            file_name: (string) destination saved file's name (including path)

        Returns:
            Saved information if success
            Error information if some errors occur
        """
        return self.download_file(url, file_name)

    def get_css_from_html(self, file_name):
        """ Save all css files and styles in files from a give html file

        Args:
            file_name: (string)

        Returns:
            All files' paths
        """
