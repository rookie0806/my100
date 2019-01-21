import React from "react";
import PropTypes from "prop-types";
import { Route, Switch, withRouter } from "react-router";
import "./styles.module.scss";
import Auth from "components/Auth";
import Footer from "components/Footer";
import Navigation from "components/Navigation";
import Feed from "components/Feed";
import Explore from "components/Explore";
import Search from "components/Search";
import { connect } from "react-redux";
const App = props => [
  props.isLoggedIn ? <Navigation key={1} /> : null,
  props.isLoggedIn ? <PrivateRoutes key={2} /> : <PublicRoutes key={2} />,
  <Footer key={3} />
];

App.propTypes = {
  isLoggedIn: PropTypes.bool.isRequired
};

const PrivateRoutes = props => (
  <Switch>
    <Route exact path="/" component={Feed} />
    <Route path="/explore" component={Explore} />
    <Route path="/search/:searchTerm" component={Search} />
  </Switch>
);

const PublicRoutes = props => (
  <Switch>
    <Route path="/recover" render={() => "recover password"} />
    <Route path="/" component={Auth} />
  </Switch>
);

export default withRouter(connect()(App))
