import "../src/scss/main.css";
import { MODE, SERVER } from "./helper";

import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Homepage from "./components/homepage";
import Scanpage from "./components/scanpage";
import Reqpage from "./components/reqpage";
import Resumepage from "./components/resumepage";
import Navbar from "./components/navbar";
import { useEffect } from "react";

function App() {

    useEffect(() => {
        console.log("mode -->", MODE)
        console.log("server -->", SERVER)
    }, [])

	return (
		<Router>
            <Route exact path="*" component={Navbar} />
			<Switch>
				<Route exact path="/" component={Homepage} />
				<Route exact path="/scan" component={Scanpage} />
				<Route exact path="/req" component={Reqpage} />
				<Route exact path="/read/:id" component={Resumepage} />
			</Switch>
		</Router>
	);
}

export default App;
