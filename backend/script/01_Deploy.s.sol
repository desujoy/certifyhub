// SPDX-License-Identifier: MIT
pragma solidity ^0.8.25;

import {Script} from "forge-std/Script.sol";
import {CertifyHub} from "../src/CertifyHub.sol";

contract Deploy is Script {
    function run() external {
        vm.broadcast();
        new CertifyHub();
    }
}
