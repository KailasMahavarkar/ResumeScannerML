import React from "react";
import { useHistory } from "react-router-dom";


const Homepage = () => {
	const history = useHistory();

	const reqClickHandler = () => {
		history.push("/req");
	};
	const scanClickHandler = () => {
		history.push("/scan");
	};

	return (
        <div className="container">
			<div className="main">
				<section>
					<div className="header">
						<h3>Resume Scanner</h3>
						<p>
							Writing a resume is not a trivial task, especially
							when it comes to the right selection of keywords.
						</p>
						<p>
							People spend hours writing and formatting the
							perfect resume hoping it to be read by a talent
							acquisition professional and, eventually, help them
							land a job interview.
						</p>
						<p>
							Unfortunately, around 75% of resumes submitted are
							never seen by a human eye.
						</p>
					</div>
				</section>
				<section>
					<div className="resumescanner">
						<div
							className="resumescanner__item"
							onClick={scanClickHandler}
						>
							Scan Your Resume
						</div>

						<div
							className="resumescanner__item"
							onClick={reqClickHandler}
						>
							Enter Company Requirements
						</div>
					</div>
				</section>
			</div>
		</div>
	);
};

export default Homepage;
