// src/pages/Home.tsx
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-4xl font-bold my-4">Welcome to CertifyHub</h1>
      <p className="text-lg text-gray-700 mb-4">
        A platform for creating, managing, and verifying digital certificates.
      </p>

      <div className="flex flex-wrap justify-center gap-4">
        <Link to="/templates" className="p-3 bg-blue-500 text-white rounded">
          Manage Templates
        </Link>
        <Link to="/generate" className="p-3 bg-green-500 text-white rounded">
          Generate Certificates
        </Link>
        <Link to="/verify" className="p-3 bg-yellow-500 text-white rounded">
          Verify Certificate
        </Link>
      </div>
    </div>
  );
}
