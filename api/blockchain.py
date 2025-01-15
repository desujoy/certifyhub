rpc_url = "http://127.0.0.1:8545"

address = "0xA6Db00B8B7D2296810939Fff4bdCDc9A200D1F55"

master_address = "0xc8387e91f1E6fC8BF072dE7ba50660d3B2A3DdDe"

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
