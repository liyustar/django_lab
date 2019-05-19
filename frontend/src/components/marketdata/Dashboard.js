import React, {Component, Fragment} from 'react';
import SecuInfoForm from "./SecuInfoForm";
import SecuInfos from "./SecuInfos";

class Dashboard extends Component {
  render() {
    return (
      <Fragment>
        <SecuInfoForm />
        <SecuInfos />
      </Fragment>
    );
  }
}

export default Dashboard;