import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Registration from "./pages/Registration";
import Login from "./pages/Login";
import ProtectedRoute from "./routes/ProtectedRoute";


function App() {
    return (
        <Routes>
            <Route path="/" element={<ProtectedRoute><Home /></ProtectedRoute>} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Registration />} />
        </Routes>
    );
}

export default App;


