/**
 * @author Chenxu Zhao 21/Feb/2017
 * @version 0.0.1
 * @since 21/Feb/2017
 */

import cheerio from 'cheerio';

/**
 * Transfer a cheerio object to a jrio object
 * 1. Add an attribute named 'level'
*/
export function jrio(cheerioObject) {
    this.addLevel(cheerioObject, 0);
}

/**
 * Add an attribute named 'level' in the tree
 * @param: cheerioObject: a DOM tree
*/
export function addLevel(cheerioObject, level) {
    let node = cheerioObject;
    cheerioObject.attr('level', level.toString());
    cheerioObject.children().forEach((child) => {
        this.addLevel(child, level + 1);
    });
}
