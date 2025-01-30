import { Navigate } from "react-router-dom";
import { getUser } from "../hooks/user.actions";

import PropTypes from "prop-types"; 

function ProtectedRoute({ children }) {

    const user = getUser();
    return user ? <>{children}</> : <Navigate to="/login/" />; 
}


ProtectedRoute.propTypes = {
    children: PropTypes.node.isRequired, 
};

export default ProtectedRoute;

