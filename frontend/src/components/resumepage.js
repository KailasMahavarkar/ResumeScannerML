import React, { useState } from "react";
import { useHistory, useLocation } from "react-router-dom";
import axios from "axios";
import { useEffectAsync } from "../helper";
import { Pie } from "react-chartjs-2";
import { isEmpty, PIECOLORS, url } from "../helper";

const pieDisplay = (data) => {
	const pie = {
		labels: Object.keys(data),
		datasets: [
			{
				label: "# of Votes",
				data: Object.values(data),
				backgroundColor: PIECOLORS,
				borderColor: [],
				borderWidth: 0,
			},
		],
	};
	return pie;
};

const Resumepage = () => {
	const [resumeData, setResumeData] = useState();
	const location = useLocation();
	const idx = location.pathname.split("/").at(-1);
	const [pieData, setPieData] = useState();
	const history = useHistory();

	useEffectAsync(async () => {
		const temp = JSON.parse(localStorage.getItem("resumeRes"));


		if (!isEmpty(temp) && (idx === temp.id)) {
			setResumeData(temp);
			setPieData(pieDisplay(temp.probability));

		} else {
            console.log('else -->')
			try {
				const result = await axios.post(url(`/read`), {
					id: idx,
				});
                console.log(result.data.result.probability);
				if (result) {
					localStorage.setItem(
						"resumeRes",
						JSON.stringify(result.data.result)
					);
					setPieData(
						pieDisplay(result.data.result.probability)
					);
					setResumeData(result.data.result);
				}
			} catch (error) {
                localStorage.removeItem("resumeRes");
                history.push(`/read/1`);
			}
		}
	}, [idx]);

	const backClickHandler = () => {
		localStorage.removeItem("resumeRes");
		history.push(`/read/${Number(idx) - 1}`);
	};

	const nextClickHandler = () => {
		localStorage.removeItem("resumeRes");
		history.push(`/read/${Number(idx) + 1}`);
	};

	return (
		<div className="container">
			<div className="main">
				{resumeData ? (
					<>
						<section>
							<div className="resumeblock">
								<div className="resumeblock__id">
									{resumeData.id}
								</div>
								<div className="resumeblock__role">
									{resumeData.role}
								</div>
								<div className="resumeblock__inner">
									<div className="resumeblock__inner__text">
										{resumeData.resumetext}
									</div>
									{pieData ? (
										<>
											<div className="resumeblock__inner__piechart">
												<Pie data={pieData} />
											</div>
										</>
									) : null}
								</div>
							</div>
						</section>
						<div className="controls">
							<div
								className="nextback"
								onClick={backClickHandler}
							>
								Back
							</div>
							<div
								className="nextback"
								onClick={nextClickHandler}
							>
								Next
							</div>
						</div>
					</>
				) : (
					"loading ..."
				)}
			</div>
		</div>
	);
};

export default Resumepage;
