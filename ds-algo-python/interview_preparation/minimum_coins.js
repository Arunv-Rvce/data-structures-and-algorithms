var MinimumCoins = /** @class */ (function () {
    function MinimumCoins() {
    }
    MinimumCoins.prototype.findMinimunCoins = function (denominations, n) {
        var result = null;
        for (var i = 0; i < denominations.length; i++) {
            if (denominations[i] < n) {
                var subResult = this.findMinimunCoins(denominations, n - denominations[i]);
                if (result === null || subResult + 1 < result)
                    result = subResult + 1;
            }
        }
        return result;
    };
    return MinimumCoins;
}());
var mc = new MinimumCoins();
var denominations = [9, 6, 5, 1];
console.log(mc.findMinimunCoins(denominations, 11));
