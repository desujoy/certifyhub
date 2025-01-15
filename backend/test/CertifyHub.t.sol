// SPDX-License-Identifier: MIT
pragma solidity ^0.8.25;

import "forge-std/Test.sol";
import "../src/CertifyHub.sol";

contract CertifyHubTest is Test {
    CertifyHub certifyHub;

    function setUp() public {
        certifyHub = new CertifyHub();
    }

    function testGenerateCertificate() public {
        string memory candidate_name = "John Doe";
        string memory template = "Certificate Template";

        certifyHub.generateCertificate(candidate_name, template);

        bytes32 certificate_id = keccak256(
            abi.encodePacked(candidate_name, template)
        );

        (string memory _candidate_name, string memory _template) = certifyHub
            .getCertificate(certificate_id);

        assertEq(_candidate_name, candidate_name);
        assertEq(_template, template);
    }

    function testGenerateCertificates() public {
        string[] memory candidate_names = new string[](2);
        candidate_names[0] = "John Doe";
        candidate_names[1] = "Jane Doe";
        string memory template = "Certificate Template";

        certifyHub.generateMultiCertificate(candidate_names, template);

        for (uint256 i = 0; i < candidate_names.length; i++) {
            bytes32 certificate_id = keccak256(
                abi.encodePacked(candidate_names[i], template)
            );

            (
                string memory _candidate_name,
                string memory _template
            ) = certifyHub.getCertificate(certificate_id);

            assertEq(_candidate_name, candidate_names[i]);
            assertEq(_template, template);
        }
    }

    function testDuplicateCertificate() public {
        string memory candidate_name = "John Doe";
        string memory template = "Certificate Template";

        certifyHub.generateCertificate(candidate_name, template);
        vm.expectRevert();
        certifyHub.generateCertificate(candidate_name, template);
    }

    function testDuplicateCertificates() public {
        string[] memory candidate_names = new string[](2);
        candidate_names[0] = "John Doe";
        candidate_names[1] = "Jane Doe";
        string memory template = "Certificate Template";

        certifyHub.generateMultiCertificate(candidate_names, template);
        vm.expectRevert();
        certifyHub.generateMultiCertificate(candidate_names, template);
    }

    function testGetCertificate() public {
        string memory candidate_name = "John Doe";
        string memory template = "Certificate Template";

        bytes32 certificate_id = keccak256(
            abi.encodePacked(candidate_name, template)
        );

        vm.expectRevert();
        certifyHub.getCertificate(certificate_id);
    }

    function testVerifyCertificate() public {
        string memory candidate_name = "John Doe";
        string memory template = "Certificate Template";

        bytes32 certificate_id = keccak256(
            abi.encodePacked(candidate_name, template)
        );

        certifyHub.generateCertificate(candidate_name, template);

        bool isVerified = certifyHub.isVerified(certificate_id);

        assertEq(isVerified, true);
    }

    function testVerifyCertificates() public {
        string[] memory candidate_names = new string[](2);
        candidate_names[0] = "John Doe";
        candidate_names[1] = "Jane Doe";
        string memory template = "Certificate Template";

        certifyHub.generateMultiCertificate(candidate_names, template);

        for (uint256 i = 0; i < candidate_names.length; i++) {
            bytes32 certificate_id = keccak256(
                abi.encodePacked(candidate_names[i], template)
            );

            bool isVerified = certifyHub.isVerified(certificate_id);

            assertEq(isVerified, true);
        }
    }

    function testVerifyInvalidCertificate() view public {
        string memory candidate_name = "John Doe";
        string memory template = "Certificate Template";

        bytes32 certificate_id = keccak256(
            abi.encodePacked(candidate_name, template)
        );

        bool isVerified = certifyHub.isVerified(certificate_id);

        assertEq(isVerified, false);
    }
}
