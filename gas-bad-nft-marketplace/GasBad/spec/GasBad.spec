/*
* Verification of GasBad
*/
using GasBadNftMarketplace as GasBadNftMarketplace;
using NftMarketplace as nftMarketplace;

methods{
    function getLising(address nftAddress,uint256 tokenId) external returns (INftMarketplace.Listing) envfree;
    function getProceeds(address seller) external returns(uint256);
    function _.safeTransferFrom(address,address,uint256) external => DISPATCHER(true);
    function _.onERC721Recived(address, address, uint256, bytes) external =>  DISPATCHER(true);
}

ghost mathint listingUpdateCount{
    init_state axiom listingUpdateCount == 0;
}
ghost mathint log4Count{
    init_state axiom log4Count == 0;
}

hook Sstore s_listings[KEY address nftAddress][KEY uint256 tokenId].price uint256 price STORAGE {
    listingUpdatesCount = listingUpdatesCount + 1;
}

hook LOG4 (uint offset, uint length, bytes32 t1, bytes32 t2,bytes32 t3, bytes32 t4){
    log4Count = log4Count + 1;
}

/////////////////////////////////////////////////////////////////////
//                      Rules                                 //   //
/////////////////////////////////////////////////////////////////////
invariant anytime_mapping_update_event(){
    listingsUpdateCount <= log4Count;
}

rule call_any_function_should_result_in_each_contract_having_the_same_state(method f,method f2)
{
    require(f.selector = f2.selector);
    env e;
    calldataarg args;
    address listingAddr;
    uint256 tokenId;
    address seller;

    require(gasBadNftMarketplace).getProceeds(e,seller) = nftMarketplace.getProceeds(seller);
    require(gasBadNftMarketplace.getListing(e,listingAddr, tokenId).price == nftMarketplace.getListing
    (listingAddr, tokenId).price); 
    require(gasBadNftMarketplace.getListing(e,listingAddr, tokenId).seller == nftMarketplace.getListing
    (listingAddr, tokenId).seller); 


    //Act
    gasBadNftMarketplace.f(e, args);
    nftMarketplace.f2(e, args)


    assert(gasBadNftMarketplace).getProceeds(e,seller) = nftMarketplace.getProceeds(seller);
    assert(gasBadNftMarketplace.getListing(e,listingAddr, tokenId).price == nftMarketplace.getListing
    (listingAddr, tokenId).price); 
    assert(gasBadNftMarketplace.getListing(e,listingAddr, tokenId).seller == nftMarketplace.getListing
    (listingAddr, tokenId).seller); 
}