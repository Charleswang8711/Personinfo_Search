import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";

const App = () => (

   <DataProvider endpoint="api/personinfo" />
 
);

ReactDOM.render(<App />, document.getElementById('api'));


