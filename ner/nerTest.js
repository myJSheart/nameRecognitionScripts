/*
* 1. Read all files from '/Users/chenxuzhao/Desktop/nameRecognitionProject/ner/json'
* 2. Calculate the name result of 'ancher_text' and 'true_name_title'
* 3. Calculate the similarities between 'ancher_text', 'true_name_title' and 'true_name'
* 4. Record the results in '/Users/chenxuzhao/Desktop/nameRecognitionProject/ner/results'
*/

// Step 1 Read all files from '/Users/chenxuzhao/Desktop/nameRecognitionProject/ner/json'
const Promise = require('bluebird');
const jsonFloder = '/Users/chenxuzhao/Desktop/nameRecognitionProject/private/tagged_files/json/';
const destination_prefix = '/Users/chenxuzhao/Desktop/nameRecognitionProject/ner/results/';
const fs = require('fs');
const files_array = fs.readdirSync(jsonFloder);
const jsonfile = require('jsonfile');
const ner = Promise.promisifyAll(require('ner'));
const async = require('asyncawait/async');
const await = require('asyncawait/await');

let target_num = 0;
let hit_target_num_anchor_text = 0;
let hit_target_num_true_name_title = 0;
let hit_target_num_true_name = 0;

const json_file_results = async.iterable(() => {

  files_array.forEach((file, index) => {
    console.log('file index -------------------------- ' + index+ '/' + files_array.length + ' ## ' + file);
    // json object that read from the file
    const file_json = jsonfile.readFileSync(jsonFloder + file);
    // Check whether this page is a target page
    if (file_json['is-directory-page'] === 'T') {
      // The outlinks area in json
      const outlinks_area = file_json['outlinks'];
      // ################ start ###################
      outlinks_area.forEach(link_area => {
        if (link_area['is-target'] === 'T') {
          target_num++;

          const anchor_text = link_area['anchor_text'];
          const true_name_title = link_area['true_name_title'];
          const true_name = link_area['true_name'];

          try {
            link_area['anchor_text_ner'] = await(ner.getAsync({ port: 8080, host: 'localhost' }, anchor_text.replace(/[0-9+]/g, '').trim() ));
            // console.dir(link_area['anchor_text_ner']);
            link_area['anchor_text_ner'] = link_area['anchor_text_ner'].entities.PERSON;
            if (link_area['anchor_text_ner'].length !== 0) {
              hit_target_num_anchor_text++;
              // console.dir(link_area['anchor_text_ner']);
              // console.log(hit_target_num_anchor_text);
            }
            link_area['true_name_title_ner'] = await(ner.getAsync({ port: 8080, host: 'localhost' }, true_name_title.replace(/[0-9+]/g, '').trim() ));
            // console.dir(link_area['true_name_title_ner']);
            link_area['true_name_title_ner'] = link_area['true_name_title_ner'].entities.PERSON;
            if (link_area['true_name_title_ner'].length !== 0) {
              hit_target_num_true_name_title++;
            }
            link_area['true_name_ner'] = await(ner.getAsync({ port: 8080, host: 'localhost' }, true_name.replace(/[0-9+]/g, '').trim() ));
            // console.dir(link_area['true_name_ner']);
            link_area['true_name_ner'] = link_area['true_name_ner'].entities.PERSON;
            if (link_area['true_name_ner'].length !== 0) {
              hit_target_num_true_name++;
            }
          } catch (e) {
            console.dir(e);
          }
        }
      });
      // ################ end ####################
    }

    // Write files
    console.log(file);
    jsonfile.writeFileSync(destination_prefix + file, file_json);
    console.log('target_num --- ' + target_num);
    console.log('hit_target_num_anchor_text --- ' + hit_target_num_anchor_text);
    console.log('hit_target_num_true_name_title --- ' + hit_target_num_true_name_title);
    console.log('hit_target_num_true_name --- ' + hit_target_num_true_name);
  });
  // console.log('target_num --- ' + target_num);
  // console.log('hit_target_num_anchor_text' + hit_target_num_anchor_text);
  // console.log('hit_target_num_true_name_title' + hit_target_num_true_name_title);
  // console.log('hit_target_num_true_name' + hit_target_num_true_name);
  //
  // return [{
  //   'target_num': target_num,
  //   'hit_target_num_anchor_text': hit_target_num_anchor_text,
  //   'hit_target_num_true_name_title': hit_target_num_true_name_title,
  //   'hit_target_num_true_name': hit_target_num_true_name,
  // }];
});

const program = async(
  () => {
    const iterator = json_file_results();
    await (iterator.forEach(console.log));

    return 'Down';
  }
);

program()
  .then(
    (results) => {
      console.log(results);
    }
  );
  // .then(() => {
  //   console.log('cccccc');
  // })
  // .then((results) => {
  //   console.dir(results + 'ccc');
  // })
  // .catch((error) => {
  //   console.log(error);
  // });

// let itemnum = 0;
// files_array.forEach(file => {
//   const outlinks_file = jsonfile.readFileSync(jsonFloder + file);
//   if (outlinks_file['is-directory-page'] === 'T') {
//     const outlinks = outlinks_file['outlinks']
//     // Step 2 Calculate the name result of 'ancher_text' and 'true_name_title'
//     outlinks.forEach(link => {
//       itemnum++;
//       // console.log(itemnum);
//       if (link['is-target'] === 'T') {
//         const anchor_text = link['anchor_text'];
//         const true_name_title = link['true_name_title'];
//         const true_name = link['true_name'];
//         const ner = require('ner');
//           if (anchor_text === '' || true_name_title === ''
//             || typeof(anchor_text) === 'undefined' || typeof(true_name_title) === 'undefined') {
//             return;
//           }
//           ner.get({
//             port: 8080,
//             host: 'localhost'
//           }, anchor_text, (err, res) => {
//             console.log('ancher_text -- ' + anchor_text);
//             if (typeof(res) === 'undefined')
//               return;
//             const anchor_text_ner = res.entities.PERSON; // ancher_text ner results
//             link['anchor_text_ner'] = anchor_text_ner;
//             // console.log(anchor_text_ner);
//             ner.get({
//                 port: 8080,
//                 host: 'localhost'
//               }, true_name_title, (err, res) => {
//                 // console.log('true_name_title --- ' + true_name_title);
//                 if (typeof(res) === 'undefined')
//                   return;
//                 const true_name_title_ner = res.entities.PERSON;
//                 link['true_name_title_ner'] = true_name_title_ner;
//                 // console.log(true_name_title_ner);
//
//                 console.log(itemnum + '----' + outlinks.length);
//                 // if (itemnum === outlinks.length) {
//                 //   console.log(itemnum + " , " + outlinks.length);
//                 //   // write files
//                 //   const destination_prefix = '/Users/chenxuzhao/Desktop/nameRecognitionProject/ner/results/';
//                 //   const file_name = destination_prefix + file;
//                 //   jsonfile.writeFileSync(file_name, outlinks_file);
//                 //   itemnum = 0;
//                 // }
//
//               }
//             );
//           });
//       }
//     });
//     itemnum = 0;
//   }
//   console.log(file);
// });


// const ner = require('ner');
//
// const nameString = 'Wikipedia is a free-access, free-content Internet encyclopedia, supported and hosted by the non-profit Wikimedia Foundation. Those who can access the site can edit most of its articles.[5] Wikipedia is ranked among the ten most popular websites,[4] and constitutes the Internets largest and most popular general'
//
// ner.get({
//     port:8080,
//     host:'localhost'
// }, nameString, function(err, res){
//     console.log(res.entities.PERSON);
//     //=> { LOCATION: [ 'Wikipedia' ], ORGANIZATION: [ 'Wikimedia Foundation'] }
// });
