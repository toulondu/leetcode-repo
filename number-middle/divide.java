class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend == 0) return 0;
        if(divisor == 1) return dividend;
        if(divisor == -1) {
            if(dividend == Integer.MIN_VALUE) return Integer.MAX_VALUE;
            return -dividend;
        }
        boolean isneg = dividend < 0 && divisor > 0 || divisor < 0 && dividend > 0;
        if(dividend > 0) dividend = -dividend;
        if(divisor > 0) divisor = -divisor;
        int ans = div(dividend, divisor);
        if(isneg) return -ans;
        return ans;
    }
    // a:被除数  b:除数   都是负数。  保证不适用long, 且中间不会出现越界的数出现。
    int div(int a, int b){
        if(a > b) return 0; // 负数 符号要变
        int num = 1;
        int tb = b;
        while((a >> 1) < tb){  // 如果对b翻倍，就可能越界， 所以算则 a减半。不能用 <= 号  由于 a>>1可能牺牲精度，本来是 tb*2不满足的情况变满足
            num <<= 1;
            tb <<= 1;   // 由于 a/2 > tb  而a没有越界（负数边界） 所以 2*tb也不会越界
        }
        return num + div(a-tb, b);
    }
}