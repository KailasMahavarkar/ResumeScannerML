import React, { useState } from "react";
import Upload from "rc-upload";
import { Pie } from "react-chartjs-2";
import Loader from "react-loader-spinner";
import { PIECOLORS, url } from "../helper";

const Scanpage = () => {
	const [resumeData, setResumeData] = useState();
	const [pieData, setPieData] = useState();
	const [err, setErr] = useState();
	const [running, setRunning] = useState(false);

	const uploadProps = {
		action: url("/scan"),
		method: "POST",
		multiple: false,
		onStart(file) {
			setRunning(true);
			console.log("onStart", file);
		},
		onSuccess(result) {
			setRunning(false);
			setResumeData(result.msg);

            console.log(result);

			if (result.result?.context) {
				const data = {
					labels: Object.keys(result.result.context),
					datasets: [
						{
							label: "# of Votes",
							data: Object.values(result.result.context),
							backgroundColor: PIECOLORS,
							borderColor: [],
							borderWidth: 0,
						},
					],
				};
				setErr();
				setPieData(data);
			} else {
				setRunning(false);
				setErr("Data is not valid type");
				setPieData();
			}
		},
		onError(err) {
			console.log("onError", err);
		},
		beforeUpload(file, fileList) {
			console.log(file, fileList);
		},
	};

	const DisplayData = (props) => {
		return (
			<>
				{props.resumeData ? (
					<section>
						<div className="title">Extracted Text</div>
						<div className="resumedata">{resumeData}</div>
					</section>
				) : null}

				{props.pieData ? (
					<section>
						<div className="title">Pie Chart</div>
						<div className="piechart">
							<Pie data={pieData} />
						</div>
					</section>
				) : null}

				{err ? <section>{err}</section> : null}
			</>
		);
	};

	return (
		<div className="container">
			<div className="main">
				<section>
					<div className="upload_container">
						<Upload {...uploadProps}>
							<button className="custom-file-upload">
								Upload Your Resume
							</button>
						</Upload>
					</div>
				</section>

				{running ? (
					<section>
						<Loader
							className="spinner"
							type="ThreeDots"
							color="#7727d8"
							height={100}
							width={100}
						/>
					</section>
				) : (
					<DisplayData resumeData={resumeData} pieData={pieData} />
				)}
			</div>
		</div>
	);
};

export default Scanpage;
