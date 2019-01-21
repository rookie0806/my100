import { combineReducers, createStore, applyMiddleware } from "redux";
import {routerMiddleware } from 'connected-react-router'
import { composeWithDevTools } from "redux-devtools-extension";
import { connectRouter } from 'connected-react-router'
import createHistory from "history/createBrowserHistory";
import thunk from "redux-thunk";
import user from "redux/modules/user";
import photos from "redux/modules/photos";
import { i18nState } from "redux-i18n";

const env = process.env.NODE_ENV;

const history = createHistory();

const middlewares = [thunk, routerMiddleware(history)];

console.log(history)
if (env === "development") {
  const { logger } = require("redux-logger");
  middlewares.push(logger);
}

const reducer = combineReducers({
  user,
  photos,
  i18nState,
  router: connectRouter(history)
});

let store;

if (env === "development") {
  store = initialState =>
    createStore(reducer, composeWithDevTools(applyMiddleware(...middlewares)));
} else {
  store = initialState => createStore(reducer, applyMiddleware(...middlewares));
}

export { history };

export default store();
