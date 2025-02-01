// src/pages/Generate.tsx
import { useState } from "react";
import CertificateEditor from "../components/CertificateEditor";
import CSVUploader from "../components/CSVUploader";
import CSVList from "../components/CSVList";
import { CSV } from "../definitions";

export default function Generate() {
  const [csv, setCsv] = useState<CSV>({ name: "", fields: [] });
  const [template, setTemplate] = useState("");

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-3xl font-bold my-4">Generate Certificates</h1>
      <CertificateEditor template={template} csv={csv} />
      <CSVUploader />
      <CSVList setCsv={setCsv} />
    </div>
  );
}
