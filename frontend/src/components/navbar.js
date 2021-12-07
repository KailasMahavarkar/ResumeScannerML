import React from "react";
import { Link, useHistory } from "react-router-dom";

const Navbar = () => {
	let history = useHistory();


	const scanHandler = () => {
		history.push("/scan");
	};
	const fetchHandler = () => {
		history.push("/req");
	};

	return (
		<div className="navbar">
			<div
				className="navbar__logo"
				onClick={() => console.log("logo clicked")}
			>
				<Link to="/">
					<a className="alink">ResumeScanner</a>
				</Link>
			</div>

			<div className="navbar__menu tablet">
				<Link to="/scan">
					<div className="navbar__menu__item" onClick={scanHandler}>
						Scan Resume
					</div>
				</Link>

				<Link to="/req">
					<div className="navbar__menu__item" onClick={fetchHandler}>
						Fetch Resume
					</div>
				</Link>
			</div>
		</div>
	);
};

export default Navbar;
