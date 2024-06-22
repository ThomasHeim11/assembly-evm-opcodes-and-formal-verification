/*
*  Verification of MulWadUp for MathMasters
*/
methods {
    function mathMasterTopHalf(uint256) external returns uint256 envfree;
    function solmateTopHalf(uint256) external returns uint256 envfree;
}


rule solmateTopHalfMatchesMathMastersTopHalf(uint256 x) {
    assert(mathMasterTopHalf(x) == solmateTopHalf(x));
}