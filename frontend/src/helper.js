import { useEffect } from "react";

const SERVER = "http://localhost:5000";

const jp = (path1, path2) => path1 + path2;

const url = (endpoint) => {
	return `${SERVER}${endpoint}`;
};

const randomID = (min = 0, max = 255) =>
	Math.floor(Math.random() * (max - min) + min);

const isEmpty = (arg) => {
	if (arg == null) {
		return true;
	} else if (typeof arg === "undefined") {
		return true;
	} else if (arg.length === 0) {
		return true;
	} else if (typeof arg === "object" && Object.keys(arg).length === 0) {
		return true;
	}
	return false;
};

const useEffectAsync = (effect, inputs) => {
	useEffect(() => {
		effect();
	}, inputs);
};

const PIECOLORS = [
	"rgba(255, 0, 0, 1)",
	"rgba(255, 175, 0, 1)",
	"rgba(213, 243, 11, 1)",
	"rgba(27, 170, 47, 1)",
	"rgba(38, 215, 174, 1)",
	"rgba(124, 221, 221, 1)",
	"rgba(95, 183, 212, 1)",
	"rgba(0, 126, 214, 1)",
	"rgba(119, 39, 216, 1)",
	"rgba(199, 88, 208, 1)",
];

export { jp, SERVER, isEmpty, url, randomID, useEffectAsync, PIECOLORS };
