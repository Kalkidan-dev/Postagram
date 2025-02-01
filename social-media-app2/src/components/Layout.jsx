import PropTypes from "prop-types";
import Navigationbar from "./Navbar";

function Layout(props) {
    return (
        <div>
        <Navigationbar />
        <div className="container m-5">{props.children}</div>
        </div>
    );
}


Layout.propTypes = {
    children: PropTypes.node.isRequired, 
};

export default Layout;
