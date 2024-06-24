/*
* Verification of NftMock 
*/
using NftMock as nft;

methods{
    function totalSupply() external returns uint256 => ALWAYS(1);
    function mint() external;
    function balanceOf(address) external returns uint256 envfree;
}


invariant totalSupplyIsNotNegative()
    totalSupply() >= 0;

rule minting_mints_one_nft(){
    env e; 
    address minter;

    require e.msg.value == 0;
    require e.msg.sender == minter;

    mathint balanceBefore = nft.balanceOf(minter);

    currentContract.mint(e); 

    assert to_mathint(nft.balanceOf(minter)) == balanceBefore + 1, "Only 1 NFT should be minted";


}


rule sanity {
    env e;
    calldataarg arg;
    method f;
    nft.f(e, arg);
    satisfy true;
}

rule no_change_to_total_supply(method f){
    uint256 totalSupplyBefore = totalSupply();
    env e;
    calldataarg args;
    f(e, args);
    assert totalSupply() == totalSupplyBefore;

}