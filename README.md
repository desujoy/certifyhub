# CertifyHub

CertifyHub is a comprehensive platform that simplifies the process of creating, managing, and verifying digital certificates. This project consists of three main components: the backend (smart contracts), the client (web interface), and the API (backend logic and blockchain integration).

## Features
- Create and upload certificate templates.
- Upload CSVs to bulk-generate certificates.
- Edit certificate designs using the Template Editor.
- Verify certificates using the blockchain.

## Directory Structure
```
├── api/ (Flask-Py)
├── backend/ (Foundry DApp)
├── client/ (React-Vite)
└── uploads/
```

## Getting Started

### Prerequisites
Ensure you have the following installed:
- [Node.js](https://nodejs.org/en/download/current) and npm
- [Foundry](https://book.getfoundry.sh/getting-started/installation) (for deploying smart contracts)
- Python
- [pipenv](https://pypi.org/project/pipenv/)

### Setup Instructions

1. **Backend**:
   - Navigate to the `backend` directory.
   - Deploy the smart contracts:
     ```bash
     forge script .\script\01_Deploy.s.sol --broadcast --rpc-url <RPC_URL>
     ```

2. **Client**:
   - Navigate to the `client` directory.
   - Install dependencies and build the project:
     ```bash
     npm install
     npm run build
     ```

3. **API**:
   - Navigate to the `api` directory.
   - Configure the `rpc_url`, `address`, and `master_address` in the `blockchain.py` file:
     ```python
     rpc_url = "http://127.0.0.1:8545" # RPC URL
     address = "0x" # Address of the deployed contract
     master_address = "0x" # Address of the funded account
     ```
   - Install dependencies and run the API server:
     ```bash
     pipenv install
     pipenv run python app.py
     ```

## Usage

1. Access the client interface via the built web application.
2. Upload templates and CSV files to generate certificates.
3. Verify certificates using the verification component.

## Development Workflow

- Smart Contracts: Developed using Foundry and Solidity.
- Web Client: Built with Vite, React, and Tailwind CSS.
- API: Implemented in Python with blockchain integration.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request.

## Acknowledgments
Special thanks to the contributors and the open-source community for making this project possible.

