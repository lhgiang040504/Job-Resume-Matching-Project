import { Routes, Route } from "react-router-dom";
import CandidateManagement from "../pages/CandidateManagement";
import JobManagement from "../pages/JobManagement";
import ChatbotManagement from "../pages/ChatbotManagement";

function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<JobManagement />} />
      <Route path="/job-management" element={<JobManagement />} />
      <Route path="/candidate-management" element={<CandidateManagement />} />
      <Route path="/chatbot-management" element={<ChatbotManagement />} />
    </Routes>
  );
}

export default AppRouter;
