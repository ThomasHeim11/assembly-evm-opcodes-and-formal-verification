// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {MathMasters} from "../src/MathMasters.sol";

contract CompactCodeBase {
    function mulWadUp(uint256 x, uint256 y) external pure returns (uint256) {
        return MathMasters.mulWadUp(x, y);
    }
}
