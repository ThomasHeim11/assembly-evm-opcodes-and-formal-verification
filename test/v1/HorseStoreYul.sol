// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.8.20;

import {Base_TestV1} from "./Base_TestV1.sol";
import {HorseStore} from "../../src/horseStorev1/HorseStoreYul.sol";

contract HorseStoreSolc is Base_TestV1 {
    function setUp() public override {
        horseStore = new HorseStore();
    }
}
