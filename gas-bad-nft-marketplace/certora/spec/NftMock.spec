/*
* Verification of NftMock 
*/
methods{
    function totalSupply() external returns uint256 envfree;
}


invariant totalSupplyIsNotNegative()
    totalSupply() >= 0;


// rule sanity{
//     satisfy true;
// }