// src/pages/Verify.tsx
import VerifyCertificate from "../components/VerifyCertificate";

export default function Verify() {
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-3xl font-bold my-4">Verify Certificates</h1>
      <VerifyCertificate />
    </div>
  );
}
