/**
 * @author Chenxu Zhao
 * @version 0.0.1
 * @since 21/Feb/2017
 */

import cheerio from 'cheerio';
import _ from 'underscore';

/**
 * @desc a class that provides many motheds to process DOM tree
 */
export default class DOMTreeProcess {
  constructor() {
    super();
  }

  /**
   * find the lowest common ancestor of two nodes
   * @param {cheerio} nodeOne a node in DOM tree
   * @param {cheerio} nodeTwo a node in DOM tree
   * @param {cheerio} cheDom a DOM tree
   * @return the lowest common ancestor of two nodes
   */
  lowestCommonAncestor(nodeOne, nodeTwo, cheDom) {
    while (nodeOne.parents.length > nodeTwoLevel.parents.length) {
      nodeOne = nodeOne.parent;
    }

    while (nodeOne.parents.length < nodeTwoLevel.parents.length) {
      nodeTwo = nodeTwo.parent;
    }

    while (nodeOne !== nodeTwo) {
      nodeOne = nodeOne.parent;
      nodeTwo = nodeTwo.parent;
    }

    return nodeOne;
  }

  /**
   * Get class names of a node
   * @param node    a cheerio DOM tree
   * @return {string} a string of class name(s)
   */
  getClassName(node) {
    return node.attr('class');
  }

  /**
   * Return an Array of node which has the same class in the DOM tree
   * @param {string} className   one or more class names
   * @example 'table', 'table cell', 'table cell text'
   * @param {cheerio} cheDom     a DOM tree
   * @return {Array}  DOMArray   an array of similar nodes.
   */
  sameClassNodes(className, cheDom) {
    let classNames = className.split(' ');
    let DOMArray = [];
    let cheClassNames = cheDom.attr('class').split(' ');

    if (_.difference(cheClassNames, classNames).length === 0) {
      DOMArray.push(cheDom);
    }

    if (cheDom.children.length > 0) {
      cheDom.children().forEach((child) => {
        DOMArray = DOMArray.concat(this.sameClassNodes(className, child));
      });
    }

    return DOMArray;
  }

  /**
   * get a score with represents the similarities between two nodes
   * @param {cheerio} nodeOne       a node
   * @param {cheerio} nodeTwo       a node
   * @param {float} score           similar scores.
   */
  getSimilarityScore(nodeOne, nodeTwo) {

  }
};
