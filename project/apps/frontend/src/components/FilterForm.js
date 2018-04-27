import React, { Component } from "react";
import PropTypes from "prop-types";
import Table from "./Table"


class Form extends Component {
 
  static propTypes = {
    data: PropTypes.array.isRequired,
  };

  state = {
    name: "",
    email: "",
    data: [],
    submit: false
    
  };
  
  handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };
  
  handleSubmit = e => {
    e.preventDefault();
    const { name, email } = this.state;

    var info = [];
    var search = [];

    info = this.props.data;

      if(name !== "" || email != "")
      {

        (info => { info.map( el => { 

         if((name === el.name) || (email === el.email))
         {
            search.push(el);
            return;
         }
        
         })})(info);

      }
      else
      {
        search = info;

      }
      console.log(search);

      (data => this.setState({ data: data,submit: true }))(search);
   
  };

  render() {
    const { name, email,data,submit} = this.state;
    //let  data = this.state.data;
    return (
      submit ? 
      (
        <div>
        <div className="column">
         <form onSubmit={this.handleSubmit}>
          <div className="field">
            <label className="label">Name</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="name"
                onChange={this.handleChange}
                value={name}
                
              />
            </div>
          </div>
          <div className="field">
            <label className="label">Email</label>
            <div className="control">
              <input
                className="input"
                type="email"
                name="email"
                onChange={this.handleChange}
                value={email}
              
              />
            </div>
          </div>
         
          <div className="control">
            <button type="submit" className="button is-info">
              Search
            </button>
          </div>
          </form>
        </div>
        <div className="column">
        <Table data={data} />
        </div>
       </div>
      )
      :
      (
        <div>
        <div className="column">
         <form onSubmit={this.handleSubmit}>
          <div className="field">
            <label className="label">Name</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="name"
                onChange={this.handleChange}
                value={name}
                
              />
            </div>
          </div>
          <div className="field">
            <label className="label">Email</label>
            <div className="control">
              <input
                className="input"
                type="email"
                name="email"
                onChange={this.handleChange}
                value={email}
              
              />
            </div>
          </div>
         
          <div className="control">
            <button type="submit" className="button is-info">
              Search
            </button>
          </div>
          </form>
        </div>
        <div className="column">
          <Table data={this.props.data} />
        </div>
        </div>
      )

    );
  }
}

export default Form;
