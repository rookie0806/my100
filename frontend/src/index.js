import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import I18n from "redux-i18n";
import { ConnectedRouter } from "connected-react-router";
import store, { history } from "redux/configureStore";
import App from "components/App";
//import App from './App';
import { translations } from "translations";
import * as serviceWorker from './serviceWorker';
console.log(store.getState())
ReactDOM.render(
  <Provider store={store}>
    <I18n translations={translations} initialLang="en" fallbackLang="en">
      <ConnectedRouter history={history}>
        <App />
      </ConnectedRouter>
    </I18n>
  </Provider>,
  document.getElementById('root')
);
serviceWorker.register();