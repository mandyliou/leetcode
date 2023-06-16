/**
 * @return {Object}
 */
var createInfiniteObject = function() {
    return new Proxy({}, {
        get(target, property) {
            return function() {
                return property;
            };
        }
    });
   
};

/**
 * const obj = createInfiniteObject();
 * obj['abc123'](); // "abc123"
 */