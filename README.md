# CertifyHub

CertifyHub is a blockchain-based certificate generation and validation system built using Solidity. It leverages blockchain technology to ensure the security, authenticity, and immutability of certificates.

## Features

- **Certificate Generation**: Generate unique certificates for candidates.
- **Batch Certificate Generation**: Generate multiple certificates in a single transaction.
- **Certificate Validation**: Verify the authenticity of a certificate on the blockchain.
- **Transparency**: Publicly verifiable certificates to enhance trust.

## Contract Details

### TrustEaseCertify

The `TrustEaseCertify` contract includes the following functions:

- **generateCertificate**: Generates a unique certificate for a candidate.
- **generateMultiCertificate**: Generates multiple certificates in a single transaction.
- **getCertificate**: Retrieves the details of a certificate using its ID.
- **isVerified**: Checks if a certificate exists and is valid.

### Solidity Code

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.25;

contract TrustEaseCertify {
    struct Certificate {
        string candidate_name;
        string template;
    }
    mapping(bytes32 => Certificate) public certificates;
    event certificateGenerated(bytes32 certificate_id);

    function generateCertificate(
        string memory _candidate_name,
        string memory _template
    ) public {
        bytes32 _certificate_id = keccak256(
            abi.encodePacked(_candidate_name, _template)
        );
        require(
            bytes(certificates[_certificate_id].candidate_name).length == 0,
            "Certificate with this ID already exists"
        );

        Certificate memory cert = Certificate({
            candidate_name: _candidate_name,
            template: _template
        });

        certificates[_certificate_id] = cert;

        emit certificateGenerated(_certificate_id);
    }

    function generateMultiCertificate(
        string[] memory _candidate_name,
        string memory _template
    ) public {
        for (uint256 i = 0; i < _candidate_name.length; i++) {
            bytes32 _certificate_id = keccak256(
                abi.encodePacked(_candidate_name[i], _template)
            );

            if (
                bytes(certificates[_certificate_id].candidate_name).length != 0
            ) {
                revert();
            }

            Certificate memory cert = Certificate({
                candidate_name: _candidate_name[i],
                template: _template
            });

            certificates[_certificate_id] = cert;

            emit certificateGenerated(_certificate_id);
        }
    }

    function getCertificate(bytes32 _certificate_id)
        public
        view
        returns (string memory _candidate_name, string memory _template)
    {
        Certificate memory cert = certificates[_certificate_id];

        require(
            bytes(certificates[_certificate_id].candidate_name).length != 0,
            "Certificate with this ID does not exist"
        );

        return (cert.candidate_name, cert.template);
    }

    function isVerified(bytes32 _certificate_id) public view returns (bool) {
        return bytes(certificates[_certificate_id].candidate_name).length != 0;
    }
}
```

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/)
- [Truffle](https://www.trufflesuite.com/truffle)
- [Ganache](https://www.trufflesuite.com/ganache) (for local development)
- [MetaMask](https://metamask.io/) (for interacting with the deployed contract)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/certifyhub.git
   cd certifyhub
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Compile the smart contracts:
   ```bash
   truffle compile
   ```

4. Deploy the smart contracts to your local blockchain:
   ```bash
   truffle migrate
   ```

### Usage

1. Open Ganache and make sure it's running.

2. Interact with the deployed contract using Truffle console:
   ```bash
   truffle console
   ```

3. Generate a certificate:
   ```javascript
   let instance = await TrustEaseCertify.deployed();
   await instance.generateCertificate("John Doe", "Template1");
   ```

4. Verify a certificate:
   ```javascript
   let isValid = await instance.isVerified("certificate_id");
   console.log(isValid);
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

- [OpenZeppelin](https://openzeppelin.com/) for their great library of smart contract templates.
- [Truffle](https://www.trufflesuite.com/) for providing an excellent development framework.
- [Ethereum](https://ethereum.org/) for the blockchain platform.
