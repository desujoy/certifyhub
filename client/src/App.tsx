// src/App.tsx
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Templates from "./pages/Templates";
import Generate from "./pages/Generate";
import Verify from "./pages/Verify";
import Navbar from "./components/Navbar";
import { useState } from "react";
import { CSV } from "./definitions";
function App() {
  const [template, setTemplate] = useState("");
  const [csv, setCsv] = useState<CSV>({
    name: "",
    fields: [],
  });
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/templates" element={<Templates template={template} setTemplate={setTemplate} />} />
        <Route path="/generate" element={<Generate template={template} csv={csv} setCsv={setCsv} />} />
        <Route path="/verify" element={<Verify />} />
      </Routes>
    </Router>
  );
}

export default App;
