import { Navigate } from "react-router-dom";
import PropTypes from "prop-types"; 

function ProtectedRoute({ children }) {
    const auth = JSON.parse(localStorage.getItem("auth"));

    return auth && auth.user ? (
        <>{children}</>
    ) : (
        <Navigate to="/login/" />
    );
}

// Add PropTypes validation
ProtectedRoute.propTypes = {
    children: PropTypes.node.isRequired, 
};

export default ProtectedRoute;
