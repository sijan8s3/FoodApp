function getIntoAnArgument() {
    var args = arguments.slice();
    args.forEach(function(arg) {
        console.log(arg);
    });
}
function getIntoAnArgument(...args) {
    args.forEach(arg => console.log(arg));
}

var args = []; // Empty array, at first.
for (var i = 0; i < arguments.length; i++) {
    args.push(arguments[i])
} /
