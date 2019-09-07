class MinimumCoins {
    findMinimunCoins(denominations: Array<number>, n: number): number {
        let result: number = null;
        for (let i=0; i < denominations.length; i++) {
            if (denominations[i] < n) {
                let subResult: number = this.findMinimunCoins(denominations, n - denominations[i]);
                if (result === null || subResult + 1 < result)
                    result = subResult + 1;
            }
        }
        return result;
    }
}

let mc = new MinimumCoins();
let denominations: Array<number> = [9, 6, 5, 1];
console.log(mc.findMinimunCoins(denominations, 17));
