import React, {Component} from 'react';
import Square from "./Square";

class Board extends Component {

  renderSquare(i) {
    return <Square value={i} />;
  }

  render() {
    return (
      <div>
        <table>
          <tr>
            {this.renderSquare(0)}
            {this.renderSquare(1)}
            {this.renderSquare(2)}
          </tr>
          <tr>
            <td><Square value="3" /></td>
            <td><Square value="4" /></td>
            <td><Square value="5" /></td>
          </tr>
          <tr>
            <td><Square value="6" /></td>
            <td><Square value="7" /></td>
            <td><Square value="8" /></td>
          </tr>
        </table>
      </div>
    );
  }
}

export default Board;