/**
 * @author Chenxu Zhao
 * @since 22/Feb/2017
 */

export default class WebLocalStorage {
  /**
   * dowload a web page
   * @param {string} url  an url
   * @param {string} localStorageDirectory a file floder to store web pages
   */
  downloadWebpage(url, localStorageDirectory) {
    try {
      fs.access(localStorageDirectory);
      console.log(`Downloading web pages to ${path}`);
      const command = `wget --page-requisite ${url} -P ${localStorageDirectory}`;
      const result = child_process.execSync(command);
    } catch (e) {
      console.log(`An Error Occur when Downloading web pages: ${e}`);
    }
  }

  /**
   * Download a file
   * @param {string} url url of a html file
   * @param {string} localStorageFloder directory to save the html file
   */
  downloadFile(url, localStorageFloder) {
    const http = require('http');
    const fs = require('fs');

    const file = fs.createWriteStream(localStorageFloder);
    return new Promise(
      
    );
  }
};
