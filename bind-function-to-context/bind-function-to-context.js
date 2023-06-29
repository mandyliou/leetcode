/**
 * @param {Object} obj
 * @return {Function}
 */
Function.prototype.bindPolyfill = function(obj) {
    const originalFunc = this;
    return function(...args){
        return originalFunc.apply(obj, args);
    }
    
}