/*
* Verification of MulWadUp for MathMasters
*/
methods{
    function mulWadUp (uint256 x, uint256 y) external returns uint256 envfree;
}


rule ckeck_testMulWadUpFuzz(uint256 x, uint256 y) {
        if (x == 0 || y == 0 || y <= type(uint256).max / x) {
            uint256 result = MathMasters.mulWadUp(x, y);
            uint256 expected = x * y == 0 ? 0 : (x * y - 1) / 1e18 + 1;
            assert(result == expected);
        }
    }