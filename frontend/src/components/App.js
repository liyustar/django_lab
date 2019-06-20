import React, {Component, Fragment} from "react";
import ReactDOM from "react-dom";
import Header from "./layout/Header";
import Dashboard from "./marketdata/Dashboard";
import { Provider } from 'react-redux';
import store from "../store";

import SelectInput from "./base/SelectInput";
import Board from "./game/Board";
import Post from "./demo/Post";
import PostForm from "./demo/PostForm";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <Header />
          <div className="container">
            <Dashboard />
          </div>
          <p>haha</p>
          {/*<Board />*/}
          <PostForm />
          <hr />
          <Post />
        </Fragment>
      </Provider>
    )

  }
}

ReactDOM.render(<App />, document.getElementById("app"));
