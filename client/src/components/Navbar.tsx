// src/components/Navbar.tsx
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="flex justify-center bg-gray-800 p-4">
      <Link to="/" className="text-white px-4">Home</Link>
      <Link to="/templates" className="text-white px-4">Templates</Link>
      <Link to="/generate" className="text-white px-4">Generate</Link>
      <Link to="/verify" className="text-white px-4">Verify</Link>
    </nav>
  );
}
