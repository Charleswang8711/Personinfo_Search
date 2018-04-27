import React, { Component } from "react";
import PropTypes from "prop-types";
import Table from "./Table"
import FilterForm from "./FilterForm"


class DataProvider extends Component {

  static propTypes = {
    endpoint: PropTypes.string.isRequired,
  };

  state = {
    data: [],
    loaded: false,
    placeholder: "Loading..."
   
  };

  componentDidMount() {
    fetch(this.props.endpoint)
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ placeholder: "Something went wrong" });
        }
        return response.json();
      })
      .then(data => this.setState({ data: data, loaded: true }));
  }

  render() {
    const { data, loaded, placeholder } = this.state;
    return loaded ? <FilterForm data={data} /> : <p>{placeholder}</p>;
  }
}

export default DataProvider;
