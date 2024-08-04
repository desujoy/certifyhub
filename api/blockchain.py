address = "0xC43e51908a1550F2f57ee408dd17366D37F2AF36"

abi = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "certificate_id",
                "type": "bytes32",
            }
        ],
        "name": "certificateGenerated",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "name": "certificates",
        "outputs": [
            {"internalType": "string", "name": "candidate_name", "type": "string"},
            {"internalType": "string", "name": "template", "type": "string"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "string", "name": "_candidate_name", "type": "string"},
            {"internalType": "string", "name": "_template", "type": "string"},
        ],
        "name": "generateCertificate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "string[]", "name": "_candidate_name", "type": "string[]"},
            {"internalType": "string", "name": "_template", "type": "string"},
        ],
        "name": "generateMultiCertificate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_certificate_id", "type": "bytes32"}
        ],
        "name": "getCertificate",
        "outputs": [
            {"internalType": "string", "name": "_candidate_name", "type": "string"},
            {"internalType": "string", "name": "_template", "type": "string"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_certificate_id", "type": "bytes32"}
        ],
        "name": "isVerified",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
]
