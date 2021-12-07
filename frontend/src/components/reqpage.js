import React, { useState, useEffect } from "react";
import axios from "axios";
import Table from "rc-table";
import { Link } from "react-router-dom";
import Loader from "react-loader-spinner";
import { url } from "../helper";

const Reqpage = () => {
	const [reqText, setReqText] = useState();
	const [reqData, setReqData] = useState();
	const [columns, setColumn] = useState();
	const [running, setRunning] = useState(false);

	const reqChangeHandler = ({ target: { value } }) => {
		setReqText(value);
	};

	useEffect(() => {
		setReqText(localStorage.getItem("reqText"));
	}, []);

	const reqSubmitHandler = async () => {
		setReqText();
		setReqData();
		setColumn();
		localStorage.removeItem("reqText");

		setRunning(true);
		const result = await axios.post(url("/req"), {
			text: reqText,
		});

		const xcolumn = [
			{
				title: "ID",
				dataIndex: "id",
				key: "id",
				className: "cells reqid",
			},
			{
				title: "RANK",
				dataIndex: "rank",
				key: "rank",
				className: "cells reqrank",
			},
			{
				title: "RESUMETEXT",
				dataIndex: "resumetext",
				key: "resumetext",
				className: "cells",
				render: (value, row, index) => (
					<div className="reqtext">
						{row.resumetext.length > 150
							? row.resumetext.substring(0, 150) + "....."
							: row.resumetext}
					</div>
				),
			},
			{
				title: "RESUMELINK",
				dataIndex: "resumelink",
				key: "resumelink",
				className: "cells",
				render: (value, row, index) => (
					<Link to={`/read/${row.id}`}>
						<div className="reqlink">Read Resume</div>
					</Link>
				),
			},
		];

		setReqData(result.data.result);
		setColumn(xcolumn);
		localStorage.setItem("reqText", reqText);

		setRunning(false);
	};

	return (
		<div className="container">
			<div className="main">
				<div className="reqcontainer">
					<section>
						<div className="reqtitle">
							Enter Company Requirements
						</div>
					</section>
					<section>
						<textarea
							name="textarea"
							id="textarea"
							placeholder="Company Requirements"
							value={reqText}
							onChange={reqChangeHandler}
							cols="30"
							rows="10"
						></textarea>
						<button
							type="text"
							className="reqbutton"
							value="submit"
							onClick={reqSubmitHandler}
						>
							Submit
						</button>
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
					) : reqData ? (
						<section>
							<Table columns={columns} data={reqData} />
						</section>
					) : null}
				</div>
			</div>
		</div>
	);
};

export default Reqpage;
